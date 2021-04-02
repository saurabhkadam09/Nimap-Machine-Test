from django.db import models
from administrator.models import tbl_user
# Create your models here.
class tbl_client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_client'

class tbl_project(models.Model):
    project_name = models.CharField(max_length = 255)
    client = models.ForeignKey(tbl_client,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255,default='admin')

    class Meta:
        db_table = 'tbl_project'

class tbl_project_user(models.Model):
    project = models.ForeignKey(tbl_project,on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_project_user'