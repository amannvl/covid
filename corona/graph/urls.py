from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="home"),
    path('selectCountry', views.drillDownACountry, name='drillDown'),
]
