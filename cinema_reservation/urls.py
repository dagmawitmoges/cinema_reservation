"""
URL configuration for cinema_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from cinema import views

urlpatterns = [
    path('', views.home, name='home'),
   

    path('m-description/', views.movie_description, name='movie_description'),
     path('about/', views.about_us, name='about_us'),
      path('seat/', views.seat_page, name='seat'),
      path('ticket/', views.ticket_page, name='ticket'),
    path('admin/', admin.site.urls),
]

