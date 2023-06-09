from django.urls import path
from django.contrib.auth import views
from .views import SignupView, CustomLoginView, ProfileView

urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile')
]