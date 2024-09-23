from django.urls import path, re_path
from urlsAndViews.departments import views


urlpatterns = [
    path('', views.index, name='index'),
    path('softuni/', views.redirect_to_softuni),
    path('redirect-to-view/', views.redirect_to_view),
    path('<int:pk>', views.view_with_int_pk),  # must be before '<str:...>'
    path('<int:pk>/<slug:slug>/', views.view_with_slug),
    path('<str:variable>/', views.view_with_name),  # matches till '/'
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.view_show_archive),
    path('<path:parametar>/', views.view_with_path),  # matches after '/' as well
]
