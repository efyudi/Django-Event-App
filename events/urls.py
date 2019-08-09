from django.urls import path, re_path
from . import views

urlpatterns = [
    #path('<int:year>/<str:month>/', views.sepcified_date, name='specified_date'),
    path('add_venue/', views.add_venue, name='add_venue'),
    re_path(r'^(?P<year>20(0[0-9]|[0-9]{2}))/(?P<month_number>0?[1-9]|1[0-2])/',
            views.sepcified_date, name='specified_date'),
    path('', views.default_home, name='default_home'),

]
