from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize
from job_post.models import Job
from weixin.models import Employer
from django.contrib.auth.models import User
import json

class JobPost(APIView):
    def get(self, request, format=None):
        """
        提供 get 请求
        """
        
        keyword =  request.GET['search']
        id = request.GET['id']

        print(keyword)
        print(id)

        if keyword == '' and id == '':
            job_posts = Job.objects.all().values()
        elif keyword and id == '':
            job_posts = Job.objects.filter(
                job_title__contains=keyword
            ).values()
        elif keyword == '' and id:
            job_posts = Job.objects.filter(job_id=id).values()

        
        #data = serialize("json", job_posts, fields=('job_id','job_title', 'jd', 'company_name'))

        #print(type(data))
        return Response({"data": job_posts}, content_type="application/json")
    
    def post(self, request, format=None):

        data = json.loads(request.body)
        form = data.get('form')
        user_id = data.get('employer')

        job = Job.objects.create(
            company_name = form['company_name'],
            company_description = form['company_description'],
            website = form['website'],
            industry = form['industry'],
            job_title = form['job_title'],
            jd = form['jd'],
            working_hour = form['working_hour'],
            working_location = form['working_location'],
            contact_name = form['contact_name'],
            contact_mobile = form['contact_mobile'],
            contact_wechat = form['contact_wechat'],
            contact_email = form['contact_email'],    
            start_time = form['start_time'],
            advice = form['advice']
        )

        # job.employer_id = Employer.objects.filter(username=user_id)
        job.if_remote = (form['if_remote'], form['if_remote'])
        job.salary_range = (form['salary_range'], form['salary_range'])
        job.if_training = (form['if_training'], form['if_training'])
        job.if_prioritize = (form['if_prioritize'], form['if_prioritize'])

        job.save()


        return Response({
                'code': 'success',
                'message': 'job submitted successfully'
            })

