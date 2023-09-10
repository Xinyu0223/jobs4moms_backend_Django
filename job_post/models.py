from django.db import models
from weixin.models import Employer



JOB_TYPE_CHOICE = (('全职', '全职'), ('兼职', '兼职'))
IF_REMOTE_CHOICE = (('远程', '远程'), ('线下', '线下'), ('混合模式', '混合模式'))
SALARY_RANGE_CHOICE = (('1000-3000', '1000-3000'), ('3000-5000', '3000-5000'), ('5000-10000', '5000-10000'), ('10000+', '10000+'), ('固定收入', '固定收入')) # 月薪区间 【1-3k，3-5k， 5-10k，10k+，固定收入】
IF_TRAINING_CHOICE = (('是', '是'), ('否', '否'), ('按需提供', '按需提供'))  # 是否提供简单的职前培训 【是，否，根据需求可以安排】
IF_PRIORITIZE_CHOICE = (('是', '是'), ('否', '否'), ('其他', '其他')) # 是否愿意优先提供以上工作给全职妈妈 【是，否，其他】


# Create your models here.
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    employer_id = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True)
    company_name = models.CharField(max_length = 100)
    company_description = models.CharField(max_length = 1000, default='')
    website = models.CharField(max_length = 100)
    industry = models.CharField(max_length = 100)
    job_title = models.CharField(max_length = 100)
    job_type = models.CharField(
        max_length = 20,
        choices = JOB_TYPE_CHOICE,
        default = '全职'
        )
    jd = models.CharField(max_length = 10000)
    working_hour = models.CharField(max_length = 100)
    working_location = models.CharField(max_length = 100)
    if_remote = models.CharField(
        max_length = 20,
        choices = IF_REMOTE_CHOICE,
        default = '线下'
        )
    salary_range = models.CharField(
        max_length = 20,
        choices = SALARY_RANGE_CHOICE,
        default = '1000-3000'
        )
    contact_name = models.CharField(max_length = 100)
    contact_mobile = models.CharField(max_length = 100)
    contact_wechat = models.CharField(max_length = 100)
    contact_email = models.EmailField()
    if_training = models.CharField(
        max_length = 20,
        choices = IF_TRAINING_CHOICE,
        default = '是'
        )
    start_time = models.CharField(max_length=100)
    if_prioritize = models.CharField(
        max_length = 20,
        choices = IF_PRIORITIZE_CHOICE,
        default = '是'
        )
    advice =  models.CharField(max_length = 1000) # 我们欢迎您的更多宝贵意见，支持妈妈有效重回职场
    post_time = models.DateTimeField(auto_now_add=True)


