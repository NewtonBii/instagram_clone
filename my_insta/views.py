from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewStatusForm
from .models import Image, Comments, Profile
import json

# Create your views here.
def timelines(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    print(images)
    return render(request, 'timelines.html', {'images':images, 'profiles':profiles})

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')
def new_status(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewStatusForm(request.POST, request.FILES)
        if form.is_valid():
            status = form.save()
            status.user = current_user
            status.save()
        HttpResponseRedirect('timelines')
    else:
        form = NewStatusForm()
    return render(request, 'new_status.html', {"form": form})
