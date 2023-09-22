from django.contrib import admin
from . models import demo

# Register your models here.
@admin.register(demo)

class demoAdmin(admin.ModelAdmin):
    list_display=('id','Name','course_name','course_duration','seat')

# admin.site.register(demo, demoAdmin)
