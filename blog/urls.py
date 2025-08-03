# blog/urls.py
from django.urls import path
from .views import (
    home,
    SignUpView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    custom_logout_view,
    PasswordChangeView,
    PasswordChangeDoneView,
)

urlpatterns = [
    # URLs from previous tasks
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # Post edit and delete URLs
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    # Enhanced authentication URLs
    path('logout/', custom_logout_view, name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]