from django.shortcuts import render

# Create your views here.
def timelines(request):
    working = 'working'
    return render(request, 'timelines.html', {'working':working})
