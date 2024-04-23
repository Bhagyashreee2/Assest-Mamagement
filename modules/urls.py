from django.urls import path, include
from modules.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView
from .views import UserDetailAPIView, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView, UserLogoutView
from . import views

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name='register'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("profile/", UserProfileView.as_view(), name='profile'),
    path("changepassword/", UserChangePasswordView.as_view(), name='changepassword'),
    path("send-reset-password-email/", SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path("reset-password/<uid>/<token>/", UserPasswordResetView.as_view(), name='reset-password'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:id>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/<int:id>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    # add Asset
    # path('search/', views.search_view, name='search'),
    # path('asset/create/', views.create_asset_view, name='create_asset'),
    # path('asset/<int:pk>/', views.retrieve_asset_view, name='retrieve_asset'),
    # path('asset/<int:pk>/update/', views.update_asset_view, name='update_asset'),
    # path('asset/<int:pk>/delete/', views.delete_asset_view, name='delete_asset'),
    # path('asset/<int:pk>/check_in/', views.check_in_view, name='check_in'),
]
