from django.conf.urls import patterns, url
from grades_a import views

urlpatterns = patterns('',
    url(r'^$', views.home, name = 'home' ),
    url(r'^list/get/(?P<student_id>\d+)/$' , views.student_student),
    url(r'^list/$', views.list, name='list'),
)