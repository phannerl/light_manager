from django.contrib import admin
from .models import Home, Light, Room, LightHistory
# Register your models here.


admin.site.register(Home)
admin.site.register(Room)
admin.site.register(Light)
admin.site.register(LightHistory)