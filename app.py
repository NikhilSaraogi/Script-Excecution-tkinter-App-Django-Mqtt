import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
from datetime import datetime
from peewee import Model, SqliteDatabase, CharField, ForeignKeyField, DateTimeField, FloatField
import paho.mqtt.client as paho 
from logzero import logger
import json
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk

MQTT_TOPIC_CREATE = "script/create"
MQTT_TOPIC_UPDATE = "script/update"
MQTT_TOPIC_VIEW="script/view"
MQTT_TOPIC_DELETE = "script/delete"
MQTT_TOPIC_EXECUTION = "script/execution"

def on_connect(client, obj, flags, rc):
    logger.info("Connecting to client:"+str(rc))
    if rc != 0:
        logger.info("Connection failed with result code " + str(rc))
        exit()
           
def on_log(client, userdata, obj, buff):
    logger.info("log:"+str(buff))

client = paho.Client()  
client.on_log = on_log
client.on_connect = on_connect

try:
    client.connect('127.0.0.1', 1883)
except:
    logger.info("Error: Could not connect to MQTT broker")


# Database setup
db = SqliteDatabase('script_app.db')

class BaseModel(Model):
    class Meta:
        database = db

class Script(BaseModel):
    name = CharField(unique=True)
    body = CharField()

class ExecutionLog(BaseModel):
    script = ForeignKeyField(Script, backref='executions')
    output = CharField()
    execution_started_at = DateTimeField()
    execution_completed_at = DateTimeField()
    execution_time = FloatField()

def create_script():
    name = script_name_entry.get()
    body = script_body_text.get('1.0', 'end-1c')

    try:
        script = Script.create(name=name, body=body)
        script_listbox.insert(tk.END, script.name)
        script_name_entry.delete(0, tk.END)
        script_body_text.delete('1.0', tk.END)
        body_publish = [{"Script Name" : name, "Code" : body}]
        messagebox.showinfo("Success", f"Script '{name}' created successfully.")
        client.publish(MQTT_TOPIC_CREATE, json.dumps(body_publish))

    except Exception as e:
        messagebox.showerror("Error", "Failed to create script:\n" + str(e))

def delete_script():
    selected_script = script_listbox.get(tk.ACTIVE)
    script = Script.get(Script.name == selected_script)
    script.delete_instance()
    script_listbox.delete(tk.ACTIVE)
    messagebox.showinfo("Success", f"Script '{selected_script}' deleted successfully.")
    body_publish = [{"Script Name" : selected_script}]
    client.publish(MQTT_TOPIC_DELETE, json.dumps(body_publish))

def view_script():
    selected_script = script_listbox.get(tk.ACTIVE)
    script = Script.get(Script.name == selected_script)
    script_body_text.delete('1.0', tk.END)
    script_body_text.insert('1.0', script.body)
    body_publish = [{"Script Name" : selected_script,"Code": script.body}]
    client.publish(MQTT_TOPIC_VIEW, json.dumps(body_publish))

def update_script():
    selected_script = script_listbox.get(tk.ACTIVE)
    new_body = script_body_text.get('1.0', 'end-1c')
    
    try:
        script = Script.get(Script.name == selected_script)
        script.body = new_body
        script.save()
        messagebox.showinfo("Success", f"Script '{selected_script}' updated successfully.")
        body_publish = [{"Script Name" : selected_script,"Code":new_body}]
        client.publish(MQTT_TOPIC_UPDATE, json.dumps(body_publish))
    except Exception as e:
        messagebox.showerror("Error", "Failed to update script:\n" + str(e))


def run_script():
    selected_script = script_listbox.get(tk.ACTIVE)
    if not selected_script:
        messagebox.showwarning("Warning", "No script selected.")
        return
    
    script = Script.get(Script.name == selected_script)
    script_body = script.body.strip()

    if not script_body:
        messagebox.showwarning("Warning", "Script body is empty.")
        return
    
    start_time = datetime.now()
    try:
        process = subprocess.Popen(['python', '-c', script_body], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        output = stdout + '\n' + stderr
    except Exception as e:
        output = str(e)
    
    end_time = datetime.now()
    execution_time = (end_time - start_time).total_seconds()

    ExecutionLog.create(script=script, output=output, execution_started_at=start_time,
                        execution_completed_at=end_time, execution_time=execution_time)

    messagebox.showinfo("Execution Log", output)
    body_publish = [{"Script Name" : selected_script,"Ouput":output}]
    client.publish(MQTT_TOPIC_EXECUTION, json.dumps(body_publish))
    
def load_scripts():
    script_listbox.delete(0, tk.END)  # Clear the listbox before loading scripts
    scripts = Script.select()
    for script in scripts:
        script_listbox.insert(tk.END, script.name)

# Tkinter app setup
app = tk.Tk()
app.title("Script Execution App")

app.geometry("500x650")

style = ThemedStyle(app)
style.set_theme("radiance")  

# Load the logo image
# logo_image = Image.open("logo.jpeg")
# logo_image = logo_image.resize((50, 50))  
# logo_photo = ImageTk.PhotoImage(logo_image)

# # Create a label to display the logo
# logo_label = tk.Label(app, image=logo_photo)
# logo_label.place(x=15, y=10) 


db.connect()
db.create_tables([Script, ExecutionLog])

script_name_label = tk.Label(app, text="Script Name:")
script_name_label.pack()

script_name_entry = tk.Entry(app)
script_name_entry.pack()

script_body_label = tk.Label(app, text="Script Body:")
script_body_label.pack()

script_body_text = scrolledtext.ScrolledText(app, height=20, width=50)
script_body_text.pack()

scrollbar = tk.Scrollbar(app, command=script_body_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
script_body_text.configure(yscrollcommand=scrollbar.set)

create_button = tk.Button(app, text="Create Script", command=create_script)
create_button.pack()

script_listbox = tk.Listbox(app)
script_listbox.pack()

load_scripts()

delete_button = tk.Button(app, text="Delete Script", command=delete_script)
delete_button.pack()

view_button = tk.Button(app, text="View Script", command=view_script)
view_button.pack()

update_button = tk.Button(app, text="Update Script", command=update_script)
update_button.pack()

run_button = tk.Button(app, text="Run Script", command=run_script)
run_button.pack()

app.mainloop()




