import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import CreateActivityForm, FilterForm
from .models import Activity


def activity_list(request):
    activities = Activity.objects.all()
    filter_form = FilterForm(request.GET or None)

    search_query = ''
    filter_query = Q()

    # Shows only upcoming activities
    filter_query &= Q(date__gte=datetime.date.today())

    if filter_form.is_bound and filter_form.is_valid():
        filters = filter_form.cleaned_data
        search_query = filters.get("search")
        if search_query:
            filter_query &= (
                    Q(title__icontains=search_query) |
                    Q(text__icontains=search_query)
            )
        if filters.get("available"):
            filter_query &= (
                Q(is_full=False)
            )
        if filters.get("hide_ntnui"):
            filter_query &= (
                Q(krever_NTNUI_medlemskap=False)
            )
        if filters.get("free"):
            filter_query &= (
                Q(price=0)
            )
    activities = activities.filter(filter_query)

    context = {
        'activities': activities,
        'filter_form': filter_form,
        'query_string': search_query,
    }
    return render(request, 'events/activity_list.html', context)


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
            return redirect('/' + str(activity.id))  # Redirects to the home page
    else:
        form = CreateActivityForm()

    return render(request, 'events/activity_create.html', {'form': form})


def activity_detail_view(request, id):
    activity = Activity.objects.get(id=id)  # Gets right activity
    return render(request, 'events/activity_detail_view.html', {'activity': activity})


def register(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)

    if activity.max_participants is None or activity.registered_users.count() <= activity.max_participants:
        activity.registered_users.add(request.user.id)
        messages.info(request, u'Du er nå meldt på %s.' % activity.title)
    else:
        messages.info(request, u'Arrangementet er fullt %s.' % activity.title)

    return redirect('/')


def unregister(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)

    activity.registered_users.remove(request.user.id)
    messages.info(request, u'Du er nå meldt av %s.' % activity.title)

    return redirect('/')


@login_required
def organized_activities_view(request):
    arranged_activities = Activity.objects.filter(responsible=request.user).filter(date__gte=datetime.date.today())
    upcoming_activities = Activity.objects.filter(registered_users=request.user).filter(date__gte=datetime.date.today())

    return render(request, 'events/activity_upcoming.html',
                  {
                      'arranged_activities': arranged_activities,
                      'upcoming_activities': upcoming_activities
                  })
