from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from events import views

urlpatterns= [
    #  path('', views.home,name ="Blog_home"),
     path('', PostListView.as_view(), name ="events_home"),
     path('events/<int:pk>/', PostDetailView.as_view(), name ="events_detail"),
     path('events/<int:pk>/update/', PostUpdateView.as_view(), name ="events-update"),
     path('events/<int:pk>/delete/', PostDeleteView.as_view(), name ="events-delete"),
     path('events/new/', PostCreateView.as_view(), name ="events-create"),
] 