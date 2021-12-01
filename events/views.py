from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Events
from django.contrib.auth.models import User

# Create your views here.

class PostListView(ListView):
    model = Events
    template_name = "events/events_home.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'event'
    ordering =['-date_time']
    # paginate_by = 9

class PostDetailView(DetailView):
    model = Events
    template_name = 'events/events_details.html' 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Events
    fields =['title','content']
    template_name = 'events/events_forms.html' 


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Events
    fields =['title','content']    
    template_name = 'events/events_update.html' 


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        Events = self.get_object()
        if self.request.user == Events.author:
            return True
        return False       

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Events
    template_name = 'events/confirm_delete.html' 
    success_url= "/"  

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  

class UserPostListView(ListView):
    model = Events 
    template_name = "events/user_events_page.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'events'
    ordering =['-date_time']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Events.objects.filter(author=user).order_by('-date_time')

