from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewStatusForm

# Create your views here.
def timelines(request):
    return render(request, 'timelines.html')

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
    else:
        form = NewArticleForm()
    return render(request, 'timelines.html', {"form": form})
