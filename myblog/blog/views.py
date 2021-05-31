from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import UserList, FileList
from rest_framework.response import Response
from .serailzers import UserListSerializer, UserListInfoSerializer, FileListInfoSerializer, FileListSerializer
from django.contrib.auth.hashers import make_password, check_password


import os

# Create your views here.

class UserAll(generics.ListAPIView):
    queryset = UserList.objects.all()
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(data={
            "code":200,
            "msg":"成功获取",
            "data":serializer.data
        })


class UserRegister(generics.CreateAPIView):
    serializer_class = UserListSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            rec_data = {
                "code":200,
                "msg": "ok",
            }
            data['user_password'] = make_password(data['user_password'], 'abc', 'pbkdf2_sha256')
            UserList(**data).save()
            return Response(data=rec_data)
        except Exception as e:
            print(e)
            rec_data = {
                "code":200,
                "msg": 'error',
            }
            return Response(data=rec_data)

class UserLogin(generics.CreateAPIView):
    serializer_class = UserListSerializer
    def post(self, request, *args, **kwargs):
        user_info = request.data
        r_name = user_info['user_name']
        r_psk = make_password(user_info['user_password'], 'abc', 'pbkdf2_sha256')
        c_res = UserList.objects.filter(user_name=r_name, user_password=r_psk)
        if len(c_res) == 0:
            return Response(data={"coade":200,"msg": "用户名密码错误", 'result': False})
        # res = check_password(r_psk, c_res[0].user_password)
        return Response(data={"code":200,"msg":"登录成功",'result':True})

class CreateDir(generics.CreateAPIView):
    serializer_class = FileListSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        dirname = data['File_name']
        user_id = UserList.objects.get(id=data['File_User'])
        
        try:
            check = FileList.objects.filter(File_name=dirname, File_User=user_id)
            if len(check) > 0:
                return Response(data={
                    'code':200,
                    'msg':'名称重复',
                })
            os.mkdir(os.path.join("F:\\A测试测试", dirname))
            data['File_User'] = user_id
            FileList(**data).save()
            return Response(data={
                "code":200,
                "msg":"创建成功",
            })
        except Exception as e:
            return Response(data={
                "code":200,
                "msg":"输入正确的创建信息",
                "error_info":str(e)
            })

class DirList(generics.ListAPIView):
    serializer_class = FileListSerializer
    def get(self, request, *args, **kwargs):
        user =  UserList.objects.get(id=kwargs['user_id'])
        queryset = FileList.objects.filter(File_User=kwargs['user_id'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)

        print(type(queryset))
        return Response(data={
            "code":200,
            "msg":"ok",
            "data": serializer.data
        }
        )

class DirDetial(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        
        print(request.data)

        return Response(data={
            'code':200,
            'msg':'ok',
        })








