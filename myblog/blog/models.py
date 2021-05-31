from django.db import models

# Create your models here.

class UserList(models.Model):
    user_name = models.CharField(max_length=32, null=True, unique=True)
    user_password = models.CharField(max_length=200, null=True)
    user_describe = models.CharField(max_length=180)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_list'

class FileList(models.Model):
    File_name = models.CharField(max_length=200, null=True)
    File_content = models.CharField(max_length=200, null=True)
    File_User = models.ForeignKey(to='UserList', on_delete=models.CASCADE, to_field='id')

    class Meta:
        db_table = 'file_list'

    def __str__(self):
        return self.File_name