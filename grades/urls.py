from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'grades_p.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/' , include('grades_a.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
