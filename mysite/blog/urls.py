from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$',views.post_list,name='post_list'),#assinging
	#a view post_list to the ^$ URL
	#^$ means empty string will match
	#name is used to identify the view.



]