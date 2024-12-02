from django.contrib import admin
from user.models import*
# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display=['id','email','first_name','last_name','blood_group_type']

    list_filter = ['blood_group_type']

admin.site.register(User,UserAdmin)