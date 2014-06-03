from django.contrib import admin

# Register your models here.
from messurements.models import Pressure, Weight, UserProfile,Basic, Sleep, Exercise, Meal

admin.site.register(Pressure)
admin.site.register(Weight)
admin.site.register(UserProfile)
admin.site.register(Basic)
admin.site.register(Sleep)
admin.site.register(Exercise)
admin.site.register(Meal)
