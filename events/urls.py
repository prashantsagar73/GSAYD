from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from events import views

urlpatterns= [
    #  path('', views.home,name ="Blog_home"),
    path('', PostListView.as_view(), name ="events_home"),
    path('user/<str:username>', UserPostListView.as_view(), name ="user_events"),
    path('events/<int:pk>/', PostDetailView.as_view(), name ="events_detail"),
    path('events/<int:pk>/update/', PostUpdateView.as_view(), name ="events_update"),
    path('events/<int:pk>/delete/', PostDeleteView.as_view(), name ="events_delete"),
    path('events/new/', PostCreateView.as_view(), name="create_events"),
] 