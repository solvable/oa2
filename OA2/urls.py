"""OA2 URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from oa.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(),name="index"),
    path('gallery/', GalleryView.as_view(),name="gallery"),
    path('gallery/<proj>', ProjectView.as_view(), name="project"),
    path('systems/', SystemView.as_view(), name='systems'),
    path('security/', SecurityView.as_view(), name='security'),
    path('remote_start/', RemoteStartView.as_view(), name='remote-start'),
    path('nav_systems/', NavSystemView.as_view(), name='nav-systems'),
    path('detailing/', DetailingView.as_view(), name='detailing'),
    path('tint/', TintView.as_view(), name ='tint'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('privacy/', PrivacyView.as_view(), name='privacy')
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)