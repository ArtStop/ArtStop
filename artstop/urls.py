"""artstop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .settings import MEDIA_ROOT,MEDIA_URL
from stops import views as stops_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', stops_views.Home.as_view(), name='home'),
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^stops/(?P<pk>[0-9]+)/$', stops_views.StopDetailView.as_view(), name='stop-detail'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),#, app_namespace='ratings')),
    path('stops/<int:pk>/comment/', stops_views.add_comment_to_stop, name='add_comment_to_stop'),
    path('comment/<int:pk>/approve/', stops_views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', stops_views.comment_remove, name='comment_remove'),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)
