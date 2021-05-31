from rest_framework import serializers
from .models import UserList, FileList

class UserListInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserList
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = '__all__'

class FileListInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileList
        fields = '__all__'


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileList
        fields = '__all__'

