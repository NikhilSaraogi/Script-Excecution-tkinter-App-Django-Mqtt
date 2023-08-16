import paho.mqtt.client as paho
from logzero import logger
import os
import json
import django

MQTT_TOPICS = [
    "script/create",
    "script/update",
    "script/view",
    "script/delete",
    "script/execution",
]

def on_message(client, userdata, message):
    topic = message.topic.split('/')[-1]
    # payload = message.payload.decode()
    body = json.loads(message.payload)
    logger.info(f"Received message on topic {topic}: {body}")
    try:
        # Save the MQTT message to the database
        log = MqttLog(topic=topic, message=body[0])
        log.save()
    except Exception as e:
        logger.error(f"Error saving MQTT log: {e}")

def on_connect(client, userdata, flags, rc):
    logger.info("Connected to MQTT broker")
    for topic in MQTT_TOPICS:
        client.subscribe(topic)
    if rc != 0:
        logger.error("Connection to MQTT broker failed with result code " + str(rc))

def on_log(client, userdata, level, buf):
    logger.info(buf)

client = paho.Client()
client.on_log = on_log
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1', 1883)
client.loop_start()



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MqttLogger.settings")
    django.setup()

    from Mqtt_Logger.models import MqttLog
    from django.core.management import call_command
    client.loop_stop()
    call_command('runserver')
    

