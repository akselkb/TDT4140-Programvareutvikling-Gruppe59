from django.shortcuts import render
from django.utils import timezone
from .models import Activity


def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'events/activity_list.html', {'activities': activities})


def create_activity(request):
    return render(request, 'events/activity_create.html')
