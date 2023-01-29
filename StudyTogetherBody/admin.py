from django.contrib import admin

from .models import Room,messages,topic
admin.site.register(Room)
admin.site.register(messages)
admin.site.register(topic)