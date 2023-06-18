from django.urls import path
from weixin.views import WeixinLogin, WeixinMomRegister

app_name = 'weixin'

urlpatterns = [
    path('login/', WeixinLogin.as_view(), name='login'),
    path('mom-register/', WeixinMomRegister.as_view(), name='mom-register'),
]