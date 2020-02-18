from django.shortcuts import render

from events.forms import CreateActivityForm
from .models import Activity


def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'events/activity_list.html', {'activities': activities})


def create_activity(request):
    form = CreateActivityForm()
    return render(request, 'events/activity_create.html', {'form': form})
