from django.contrib import admin
from .models import Cloth, Groceries, Profile, Project, Volunteer, Blood

# Register your models here.
admin.site.register(Profile)
admin.site.register(Cloth)
admin.site.register(Project)
admin.site.register(Volunteer)
admin.site.register(Groceries)
admin.site.register(Blood)