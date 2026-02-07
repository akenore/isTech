from django.urls import path
from public import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('services/', views.ServiceView.as_view(), name="service"),
    path('works/', views.WorkView.as_view(), name="work"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
