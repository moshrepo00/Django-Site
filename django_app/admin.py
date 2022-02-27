from django.contrib import admin

# Register your models here.
from .models import Athlete, Team, Coach

admin.site.register(Athlete)
admin.site.register(Team)
admin.site.register(Coach)
