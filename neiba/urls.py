from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    url('^$',views.home,name= 'home '),
    url(r'^$profile/',views.profile,name='profile'),
    url(r'profile/edit$', views.edit_profile, name='edit'),
    url(r'business$', views.business, name='business'),
    url(r'business/new$', views.new_biz, name='new_biz'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)