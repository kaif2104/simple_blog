# blog/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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


# This is the view for creating a blog post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
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


# This is the view for deleting a post (Task 7)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# Custom logout view with proper session cleanup
@login_required
def custom_logout_view(request):
    username = request.user.username
    logout(request)
    messages.success(request, f'Goodbye {username}! You have been successfully logged out.')
    return redirect('home')


# Password change view
class PasswordChangeView(LoginRequiredMixin, generic.FormView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your password has been changed successfully!')
        return super().form_valid(form)


# Password change done view
class PasswordChangeDoneView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'registration/password_change_done.html'