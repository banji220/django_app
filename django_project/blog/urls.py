from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from  . import views
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    #! <pk> -----> mean PrimaryKey or the ID of a Post
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="create"),
    path('about/', views.about, name="blog-about"),
]
