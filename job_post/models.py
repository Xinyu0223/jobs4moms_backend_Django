from django.db import models


# Create your models here.
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length = 100)
    website = models.CharField(max_length = 100)
    industry = models.CharField(max_length = 100)
    job_title = models.CharField(max_length = 100)
    jd = models.CharField(max_length = 1000)
    working_hour = models.CharField(max_length = 100)
    working_location = models.CharField(max_length = 100)
    if_remote = (('远程', '远程'), ('线下', '线下'), ('混合模式', '混合模式'))
    salary_range = (('1000-3000', '1000-3000'), ('3000-5000', '3000-5000'), ('5000-10000', '5000-10000'), ('10000+', '10000+'), ('固定收入', '固定收入')) # 月薪区间 【1-3k，3-5k， 5-10k，10k+，固定收入】
    contact_name = models.CharField(max_length = 100)
    contact_mobile = models.CharField(max_length = 100)
    contact_wechat = models.CharField(max_length = 100)
    contact_email = models.EmailField()
    if_training = (('是', '是'), ('否', '否'), ('按需提供', '按需提供'))  # 是否提供简单的职前培训 【是，否，根据需求可以安排】
    start_time = models.CharField(max_length=100)
    if_prioritize = (('是', '是'), ('否', '否'), ('其他', '其他')) # 是否愿意优先提供以上工作给全职妈妈 【是，否，其他】
    advice =  models.CharField(max_length = 1000) # 我们欢迎您的更多宝贵意见，支持妈妈有效重回职场

