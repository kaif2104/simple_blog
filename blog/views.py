# blog/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

# Import models and generic views needed
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView # Make sure UpdateView & DeleteView are here
from django.views.generic import DetailView

# Import Mixins for authorization
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Add this import


# This is the view for your home page
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


# This is the view for your signup page
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully! Please log in.')
        return super().form_valid(form)


# This is the view for creating a blog post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your blog post has been created successfully!')
        return super().form_valid(form)


# This is the view for displaying a single blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# This is the view for updating a post (Task 7)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_edit.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Your blog post has been updated successfully!')
        return super().form_valid(form)


# This is the view for deleting a post (Task 7)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your blog post has been deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Custom Login View with flash messages
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)


# Custom Logout View with flash messages
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, 'You have been logged out successfully!')
        return super().dispatch(request, *args, **kwargs)