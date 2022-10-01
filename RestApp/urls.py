from django.urls import path
from RestApp import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name="hm"),
	path('about/',views.about,name="ab"),
	path('contact/',views.contact,name="ct"),
	path('reg/',views.usrreg,name="reg"),
	path('login/',v.LoginView.as_view(template_name="app/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
	path('profile/',views.pfle,name="pf"),
	path('profileupdate/',views.pfleupd,name="pfup"),
	path('order/',views.order,name="order"),
	path('feedback/',views.feedback,name="fd"),
	path('chge/',views.changepwd,name="chpd"),
	path('itmd/<int:s>/',views.itemvew,name="itmvu"),
]