from django.contrib import admin
from .models import Mom, JobType, Employer

# Register your models here.
admin.site.register(Mom)
admin.site.register(JobType)
admin.site.register(Employer)