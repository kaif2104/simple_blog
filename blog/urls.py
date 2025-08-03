# blog/urls.py
from django.urls import path
from .views import (
    home,
    SignUpView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,  # <-- Import this
    PostDeleteView,  # <-- Import this
    CustomLoginView,
    CustomLogoutView,
)

urlpatterns = [
    # URLs from previous tasks
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # Add these two new URLs for Task 7
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    # Custom login/logout views with flash messages
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
]