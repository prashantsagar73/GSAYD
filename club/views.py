from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Club
from django.contrib.auth.models import User

# Create your views here.

class PostListView(ListView):
    model = Club
    template_name = "clubs/clubs_home.html" 
    context_object_name = 'club'
    ordering =['-date_time']
    # paginate_by = 9

class PostDetailView(DetailView):
    model = Club
    template_name = 'clubs/clubs_details.html' 

class ClubCreateView(LoginRequiredMixin, CreateView):
    model = Club
    fields =['title','content']
    template_name = 'clubs/clubs_forms.html' 


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Club
    fields =['title','content']    
    template_name = 'clubs/clubs_update.html' 


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        Club = self.get_object()
        if self.request.user == Club.author:
            return True
        return False       

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Club
    template_name = 'clubs/clubs_confirm_delete.html' 
    success_url= "/"  

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  

class UserPostListView(ListView):
    model = Club
    template_name = "clubs/user_clubs.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'clubs'
    ordering =['-date_time']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Club.objects.filter(author=user).order_by('-date_time')
