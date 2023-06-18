from django.urls import path
from weixin.views import WeixinLogin, WeixinMomRegister, WeixinEmployerRegister

app_name = 'weixin'

urlpatterns = [
    path('login/', WeixinLogin.as_view(), name='login'),
    path('mom-register/', WeixinMomRegister.as_view(), name='mom-register'),
    path('employer-register/', WeixinEmployerRegister.as_view(), name='employer-register'),
]