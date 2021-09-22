from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Events

# Create your views here.

class PostListView(ListView):
    model = Events
    template_name = "events/events_home.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'posts'
    ordering =['-date_time']

class PostDetailView(DetailView):
    model = Events
    template_name = 'events/post_detail.html' 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Events
    fields =['title','content']
    template_name = 'events/post_forms.html' 


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Events
    fields =['title','content']    
    template_name = 'events/post_forms.html' 


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False       

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Events
    template_name = 'events/post_confirm_delete.html' 
    success_url= "/"  

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  

