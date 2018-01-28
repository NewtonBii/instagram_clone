from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
 url(r'^$', views.timelines, name='allTimelines'),
 url(r'^accounts/profile/', views.profile, name ='myProfile'),
 url(r'^new/status$', views.new_status, name='newStatus'),
 url(r'^user/(\d+)', views.user_profile, name='userProfiles'),
 url(r'^comments$', views.submit_comment, name='submitComment'),
 url(r'^image/(\d+)', views.single_image, name='singleImage')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
