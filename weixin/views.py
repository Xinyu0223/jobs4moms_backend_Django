from rest_framework.views import APIView
from rest_framework.response import Response

import requests
import json

from django.contrib.auth.models import User, Group

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# 获取用户数据
class UserData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print('Get data: ')
        return Response({'code': 'get ok', 'items': 'hello world'})

    def post(self, request, format=None):
        user = request.user
        user.profile.items = request.data
        user.save()
        print('Post data: ', user.profile.items)
        return Response({'code': 'post ok'})

# 微信登录
class WeixinLogin(APIView):
    def post(self, request, format=None):
        """
        提供 post 请求
        """
        # 从请求中获得code
        code = json.loads(request.body).get('code')

        # 填写你的测试号密钥
        appid = 'wxcd99b7e10eaa9e21'
        appsecret = '0aa6810eff53feee7526d9415ed095c5'
        # 微信服务接口地址
        base_url = 'https://api.weixin.qq.com/sns/jscode2session'
        # 实际请求

        url = base_url + "?appid=" + appid + "&secret=" + appsecret + "&js_code=" + code + "&grant_type=authorization_code"
        response = requests.get(url)
        # 处理获取的 openid 
        try:
            openid = response.json()['openid']
            session_key = response.json()['session_key']
        except KeyError:
            return Response({'code': 'fail'})
        else:
            # 打印到后端命令行
            print(openid, session_key)

            try:
                user = User.objects.get(username=openid)
            except User.DoesNotExist:
                user = None

            if user:
                user = User.objects.get(username=openid)
            else:
                return Response({
                    'code': 'failure',
                    'refresh': None,
                    'access': None,
                    'user_group': None,
                    'message': 'user not found, please register'
                })

            refresh = RefreshToken.for_user(user)
            print(user.groups.all())
            for g in user.groups.all():
                group_name = g.name
                break

            return Response({
                    'code': 'success',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user_group': group_name,
                    'message': 'login successfully'
                })

class WeixinMomRegister(APIView):
    def post(self, request, format=None):

        data = json.loads(request.body)
        code = data.get('code')

        # 填写你的测试号密钥
        appid = 'wxcd99b7e10eaa9e21'
        appsecret = '0aa6810eff53feee7526d9415ed095c5'
        # 微信服务接口地址
        base_url = 'https://api.weixin.qq.com/sns/jscode2session'
        # 实际请求

        url = base_url + "?appid=" + appid + "&secret=" + appsecret + "&js_code=" + code + "&grant_type=authorization_code"
        response = requests.get(url)
        # 处理获取的 openid 
        try:
            openid = response.json()['openid']
            session_key = response.json()['session_key']
        except KeyError:
            return Response({'code': 'fail'})
        else:
            # 打印到后端命令行
            print(openid, session_key)

            user = User.objects.create(
                    username=openid,
                    password=openid,
                    email = 'test@gmail.com'
                )
            group = Group.objects.get(name='mom')
            user.groups.add(group)

            


