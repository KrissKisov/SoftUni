from django.http import HttpResponse
from django.shortcuts import render
from djangoIntroduction.tasks_app.models import Task


def index(request):

    search_filter = request.GET.get('search_filter', '')

    tasks_list = Task.objects.filter(name__icontains=search_filter)

    context = {
        'search_filter': search_filter,
        'tasks_list': tasks_list,
    }

    return render(request, 'tasks/index.html', context)
