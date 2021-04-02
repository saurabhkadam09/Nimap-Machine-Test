from django.contrib import admin
from .models import tbl_user
# Register your models here.

class tbl_userAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','email_id','username','password']

admin.site.register(tbl_user,tbl_userAdmin)