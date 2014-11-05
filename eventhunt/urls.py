from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventhunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'login.views.login', name='login'),
    url(r'^events/add/$', 'event.views.add', name='add'),
    url(r'^events/added/$', 'event.views.added', name='added'),
    url(r'^upvote/$', 'eve_upvote.views.eve_upvote', name='upvote'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
