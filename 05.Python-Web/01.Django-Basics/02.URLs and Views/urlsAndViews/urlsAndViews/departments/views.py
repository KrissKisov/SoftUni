import json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from urlsAndViews.departments.models import Department


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")


def view_with_name(request, variable):
    # return HttpResponse(f"<h1>Parametar: {parametar}<?h1>")
    return render(request, 'departments/name_template.html', {'variable': variable})


# def view_with_name(request, parametar):
#     return HttpResponse(f"<h1>Parametar: {parametar}<?h1>", content_type="text/plain")
#
#
# def view_with_name(request, parametar):
#     # return HttpResponse(json.dumps({"Parametar": parametar}), content_type="application/json")
#     return JsonResponse({"Parametar": parametar})


def view_with_path(request, parametar):
    return HttpResponse(f"<h1>Parametar from path: {parametar}<?h1>")


def view_with_int_pk(request, pk):
    return HttpResponse(f"<h1>Int pk: {pk}</h1>")


def view_with_slug(request, pk, slug):

    # department = Department.objects.filter(pk=pk, slug=slug).first()
    #
    # if not department:
    #     raise Http404("Department not found")

    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f"<h1>From slug => id:{department.pk}, department: {department}</h1>")


def view_show_archive(request, archive_year):
    return HttpResponse(f"<h1>The archive year: {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')


def redirect_to_view(request):
    return redirect('index')
