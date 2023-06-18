from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class JobType(models.Model):
    JOB_CHOICES = (
        ('视觉平面设计', '视觉平面设计'), ('UI/IX等网站/小程序设计', 'UI/IX等网站/小程序设计'), ('行政/项目运营管理', '行政/项目运营管理'),
        ('摄影摄像', '摄影摄像'), ('语言翻译类', '语言翻译类'), ('销售岗位', '销售岗位'), ('社交媒体内容撰写', '社交媒体内容撰写'),
        ('小视频编辑制作', '小视频编辑制作'), ('文字编辑整理', '文字编辑整理'), ('其他', '其他'),
    )
    name = models.CharField(max_length=20,choices=JOB_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Mom(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    city = models.CharField(max_length = 100)
    age_group = (('18以下', '18以下'), ('18-25', '18-25'), ('26-30', '26-30'), ('31-40', '31-40'), ('41-50', '41-50'), ('51-60', '51-60'), ('60以上', '60以上'))
    telephone = models.CharField(max_length=100, null=True, blank=True)

    nb_child = (('1', '1'), ('2', '2'), ('3以上', '3以上'),)
    job_type = models.ManyToManyField(JobType)
    job_type_ps = models.CharField(max_length = 100)
    ## 妈妈友好工作的维度打分 
    dim_0 = models.IntegerField()
    dim_1 = models.IntegerField()
    dim_2 = models.IntegerField()
    dim_3 = models.IntegerField()
    dim_4 = models.IntegerField()
    dim_5 = models.IntegerField()
    dim_6 = models.IntegerField()
    dim_7 = models.IntegerField()
    dim_8 = models.IntegerField()
    dim_9 = models.IntegerField()
    dim_10 = models.IntegerField()

    expect_salary = models.CharField(max_length = 100)
    advice = models.CharField(max_length = 1000)


class Employer(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    company_name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    industry = models.CharField(max_length = 100)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    wechat = models.CharField(max_length=100, null=True, blank=True)


