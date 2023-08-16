from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Mqtt_Logger.urls')),
    #  path('mqtt-logs/', views.mqtt_logs_view, name='mqtt-logs'),
]
