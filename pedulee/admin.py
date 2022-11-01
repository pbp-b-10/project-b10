from django.contrib import admin


from .models import Cloth, Profile, Project, Blood

# Register your models here.
admin.site.register(Profile)
admin.site.register(Cloth)
admin.site.register(Project)
admin.site.register(Blood)