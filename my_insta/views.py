from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def timelines(request):
    return render(request, 'timelines.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')
