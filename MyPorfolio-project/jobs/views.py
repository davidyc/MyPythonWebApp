from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def main(request):
    jobs = Job.objects
    return render(request, 'jobs/index.html', {'jobs': jobs})

def details(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/details.html',{'job': job_detail})
