from django.urls import path
from club.views import PostListView, PostDetailView, ClubCreateView, PostUpdateView, PostDeleteView, UserPostListView
from club import views

urlpatterns= [
    #  path('', views.home,name ="Blog_home"),
    path('', PostListView.as_view(), name ="clubs_home"),
    path('user/<str:username>', UserPostListView.as_view(), name ="user_clubs"),
    path('clubs/<int:pk>/', PostDetailView.as_view(), name ="clubs_detail"),
    path('clubs/<int:pk>/update/', PostUpdateView.as_view(), name ="clubs_update"),
    path('clubs/<int:pk>/delete/', PostDeleteView.as_view(), name ="clubs_delete"),
    path('clubs/new/', ClubCreateView.as_view(), name="create_clubs"),
] 