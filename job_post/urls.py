from django.urls import path
from job_post.views import JobPost

app_name = 'job_post'

urlpatterns = [
    path('job_post/', JobPost.as_view(), name='job_post'),
]