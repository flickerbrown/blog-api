from django.urls import path
from .views import CreateUserView, LoginView, BlogList, BlogDetail

urlpatterns = [
  # User routes
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),

  # Blog routes
  path('blogs/', BlogList.as_view(), name='blog-list'),  # List all blogs and create a blog
  path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),  # Retrieve, update, and delete a specific blog
]