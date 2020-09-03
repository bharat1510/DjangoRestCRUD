from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^api/student/$', views.student_list),
	url(r'^api/student/(?P<pk>[0-9]+)$', views.student_details),
	url(r'^api/student/gender$', views.student_gender),
]
