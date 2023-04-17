from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/create/', RegisterView.as_view(), name='register'),
]