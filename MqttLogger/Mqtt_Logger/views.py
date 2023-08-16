from django.shortcuts import render
from .models import MqttLog

def mqtt_logs(request):
    logs = MqttLog.objects.all()
    return render(request, 'Mqtt_Logger/mqtt_logs.html', {'logs': logs})
