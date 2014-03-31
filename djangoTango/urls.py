from django.conf.urls import patterns, include, url
# This module allows access to the variables defined
# within projects settings.py
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoTango.views.home', name='home'),
    # url(r'^djangoTango/', include('djangoTango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^rango/', include('rango.urls')), # Add this new tuple!
)

if settings.DEBUG:
	urlpatterns+= patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )
