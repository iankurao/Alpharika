from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns=[
    url('^$', views.index, name="home"),
    url(r'^talent/$', views.talent_management, name='Talent'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
