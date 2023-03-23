from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path(r'api', include(('api.urls',"api"), namespace='wechatapi')),
]

urlpatterns += staticfiles_urlpatterns()

