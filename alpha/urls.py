from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns=[
    url('^$', views.index, name="home"),
    url(r'^talent/$', views.talent_management, name='Talent'),
    url(r'^lisa/$', views.lisa_kiarie, name='Lisa'),
    url(r'^lisa/about$', views.about, name='About'),
    url(r'^lisa/blogs$', views.lisa_blogs, name='Blogs'),
    url(r'^lisa/faq$', views.faq, name='Faq'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
