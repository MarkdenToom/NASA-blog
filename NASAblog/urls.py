"""NASAblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    # Comments here just for future reference so I know why these lines didn't work and where I found the fix:
    # url(r'^login/$', views.LoginView.as_view(template_name=template_name), name='login'),
    # path(r'accounts/login/', views.login, name='login'),
    # path(r'accounts/logout/', views.logout, name='logout', kwargs={'next_page': '/'})]
    # https://stackoverflow.com/questions/50188485/noreversematch-at-post-new-reverse-for-post-detail-not-found-post-detail-i
    path('accounts/login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
