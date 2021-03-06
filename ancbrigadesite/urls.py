from django.conf.urls import patterns, include, url
from django.contrib import admin
from ancbrigadesite.views import home, anc_info, about, share, authority, elections, bigmap

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^about$', about),
	url(r'^share$', share),
	url(r'^authority$', authority),
	url(r'^elections$', elections),
	url(r'^map$', bigmap),
	url(r'^(?P<anc>[0-9][A-Za-z])$', anc_info),

	# Django admin
	url(r'^admin/', include(admin.site.urls)),

	# Backend
	url(r'^upload-document$', 'ancbrigadesite.backend_views.upload_document'),
	url(r'^document/(\d+)/edit$', 'ancbrigadesite.backend_views.edit_document'),
	url(r'^document-annotations', include('annotator.urls')),

	# Externals
	url(r'^tinymce/', include('tinymce.urls')),

    # Examples:
    # url(r'^$', 'ancbrigadesite.views.home', name='home'),
    # url(r'^ancbrigadesite/', include('ancpage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
