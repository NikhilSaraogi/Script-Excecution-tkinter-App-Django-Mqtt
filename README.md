# Script-Excecution-tkinter-App-Django-Mqtt

Creating a tkinter app in which one can create python scripts, user should be able to create, delete, update or view that script

- where script list is shown user should get a play button to run that script locally.
- after execution whether script has thrown error or it has been executed successfully it should be captured in database.

Requirements for doing these :
- Subprocess (for executing python script)
- Pewee ORM

- Tables for this part of task should be as given below

1. Table Name : Script
Fields :
- Script Name
- Script Body

2. Table Name : ExecutionLog
Fields :
- script ( foreign key )
- output
- execution_started_at
- execution_completed_at
- execution_time ( in how many seconds script has been executed )
<br>
<img width="519" alt="Screenshot 2023-08-16 at 9 20 26 PM" src="https://github.com/NikhilSaraogi/Script-Excecution-tkinter-Django-Mqtt/assets/35253854/ee5bd89c-417d-488d-8409-79198e949638">
<img width="494" alt="Screenshot 2023-08-16 at 9 21 10 PM" src="https://github.com/NikhilSaraogi/Script-Excecution-tkinter-Django-Mqtt/assets/35253854/c97c43f8-1385-4ee1-b11a-a001009894e1">
<br>

2 ) Creating One Django App to Show The Data In Django Templates To User

- whenever user create script from tkinter app that should be propagated to this Django app.
- whenever user performs some actions on it like updating script or deleting script from tkinter app that should also happen on this Django app
- after script execution execution log of that script should be propagated this this Django app.

Requirement for doing these :
- MQTT
<br>
<img width="1407" alt="Screenshot 2023-08-16 at 9 22 13 PM" src="https://github.com/NikhilSaraogi/Script-Excecution-tkinter-Django-Mqtt/assets/35253854/749b1bc1-a4c2-451b-a575-367b113f20df">




