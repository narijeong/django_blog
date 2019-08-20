# TODO: delete the next line after using path() instead of url()
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
]
# # TODO: uncomment after finishing
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('<int:year>/<int:month>/<int:day>/<char:title>', views.post_detail, name='post_detail'),
# ]