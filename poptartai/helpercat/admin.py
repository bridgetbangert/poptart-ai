from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(WorkExperienceMetadata)
admin.site.register(WorkExperience)
admin.site.register(ProjectsMetadata)
admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(Education)
