from django.shortcuts import render

# Create your views here.
def timelines(request):
    return render(request, 'timelines.html')
