"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from pages.views import home_view,lost_view,found_view,about_view
from lost.views import lost_view
from lost.views import lost_enter
from lost.views import found_enter
from lost.views import found_view
#register
from users.views import register,profile
#login
from django.contrib.auth import views as auth_views
#profile image
from django.conf import settings
from django.conf.urls.static import static
from users.views import lost
from users.views import found
from users.views import updateProfile
from users.views import post_delete_view,post_delete_view1
from users.views import specific_post_view,specific_post_view1,activelost,activefound


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('reportLost/',lost_enter,name='enter_lost'),
    path('lostlist/',lost_view,name='lost_list'),
    path('foundList/',found_view,name='found_list'),
    path('reportFound/',found_enter,name='enter_found'),
    path('about/',about_view,name='about_us'),
   
    #register
    path('register/',register,name='register'),
    #login
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile/',profile,name='profile'),
    path('profile/my_lost_things/',lost,name='lost_specific'),
    path('profile/my_found_things/',found,name='found_specific'),
    path('profile/update/',updateProfile,name='update_info'),
    path('profile/my_found_things/active/<int:id>/delete/',post_delete_view,name='product-delete-f'),
    path('profile/my_lost_things/active/<int:id>/delete/',post_delete_view1,name='product-delete-l'),
    path('profile/my_found_things/active/<int:id>/',specific_post_view,name='specific-post-view-f'),
    path('profile/my_lost_things/active/<int:id>/',specific_post_view1,name='specific-post-view-l'),
    path('profile/my_lost_things/active/',activelost,name='lost_specific_active'),
    path('profile/my_found_things/active/',activefound,name='found_specific_active'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)