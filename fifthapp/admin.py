from django.contrib import admin
from fifthapp.models import student
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=['name','roll','branch','year','email','password']
admin.site.register(student,studentAdmin)
