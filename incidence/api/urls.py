from django.urls import re_path
from . import views
#app name
app_name = 'incidence-api'

urlpatterns = [
	# incidence views
	re_path(r'^$', views.IncidenceListApiView.as_view() , name='list'), # incidence list urls
	re_path(r'^create/$', views.IncidenceCreateApiView.as_view() , name='create'), # incidence create urls	
	re_path(r'^(?P<slug>[\w-]+)/$', views.IncidenceDetailApiView.as_view(), name='detail'), # incidence detail url
	re_path(r'^(?P<slug>[\w-]+)/edit/$', views.IncidenceUpdateApiView.as_view(), name='update'), # inclidence update url
	re_path(r'^(?P<slug>[\w-]+)/delete/$', views.IncidenceDeleteApiView.as_view(), name='delete'), # incidence delete url

	# state views
	# re_path(r'^state-list/$', views.StateListApiView.as_view(), name='state-list'), # state list urls
	# re_path(r'^state-list/(?P<pk>\d+)/$', views.StateDetailApiView.as_view(), name='state-detail'),


]

