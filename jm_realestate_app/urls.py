from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from jm_realestate_app import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
	path('',views.home,name="home"),
	path('userlogin',views.userlogin),
	path('adminlogin',views.adminlogin),
	path('adminpage1',views.adminpage1),
	path('userdetails',views.userdetails),
	path('enquirydetails',views.enquirydetails),
	path('viewproperty',views.viewproperty),
	path('postproperty',views.postproperty),
	path('sell',views.sell),
	path('getreports',views.getreports),
	path('sellersignup',views.sellersignup),
	path('homeviewpage',views.homeviewpage),
	path('landviewpage',views.landviewpage),
	path('storeuser',views.storeuser),
	path('checklogin',views.checklogin),
	path('property',views.property,name="property"),
	path('logout_user',LogoutView.as_view(next_page="home"),name="logout"),
	path('searchbox',views.searchbox),
	path('searchbox1',views.searchbox1),
	path('usersearch',views.usersearch),
	path('deleteuser/<int:user_id>',views.deleteuser),
	path('deletepost/<int:id>',views.deletepost),
	path('postfullview/<int:id>',views.postfullview,name="postfullview"),
	path('editpostproperty/<int:id>',views.editpostproperty),
	path('edit',views.edit),
	path('reports',views.reports),
	path('tobuy/<int:id>',views.tobuy),
	path('adminviewfulldetails/<int:id>',views.adminviewfulldetails),
	path('earning/<int:id>',views.earning),
	path('checkadminlogin',views.checkadminlogin),
	path('adminlogout',views.adminlogout),
]
