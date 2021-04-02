from django.db import models

# Create your models here.
class tbl_user(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    email_id = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255, primary_key=True)
    password = models.CharField(max_length = 255)

    class Meta:
        db_table = 'tbl_user'