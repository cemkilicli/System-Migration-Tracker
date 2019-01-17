from django.conf.urls import url
from mig_status import views

app_name ='apidocs'

urlpatterns = [
	url(r'^status/$', views.IndexView.as_view(), name='index')
]