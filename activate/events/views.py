from django.shortcuts import render, redirect

from events.forms import CreateActivityForm
from .models import Activity


def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'events/activity_list.html', {'activities': activities})


def create_activity(request):
    # User is rejected if they are not logged in
    if request.user is None or request.user.is_anonymous:
        return activity_list(request)

    if request.method == 'POST':
        form = CreateActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)  # Create activity object, but do not commit it to the database just yet
            activity.responsible = request.user  # Add the currently logged in user as 'responsible' for this activity
            activity.save()  # Save the activity to the database

            # TODO : We should probably redirect to the detailed activity page when successfully creating an activity
            return redirect('/')  # Redirects to the home page
    else:
        form = CreateActivityForm()

    return render(request, 'events/activity_create.html', {'form': form})


def activity_detail_view(request,index):
    activity_current = Activity.objects.get(index)
    return render(request, '', {'activity_current': activity_current})
