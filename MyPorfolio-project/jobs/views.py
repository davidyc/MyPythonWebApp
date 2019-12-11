from django.shortcuts import render, get_object_or_404
from .models import Job, Developer

# Create your views here.
def main(request):
    jobs = Job.objects
    devs = Developer.objects
    return render(request, 'jobs/index.html', {'jobs': jobs, 'devs': devs})

def details(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/details.html',{'job': job_detail})

def devinfo(request, dev_id):
    dev_detail = get_object_or_404(Developer, pk=dev_id)
    return render(request, 'jobs/devinfo.html',{'dev': dev_detail})
