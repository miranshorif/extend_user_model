from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.update_profile),
    path('accounts/login/', LoginView.as_view(), name='login'),
]
