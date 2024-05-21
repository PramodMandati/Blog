from django.urls import path

from .views import PostCreateView, PostListView, PostUpdateView

app_name = 'post'

urlpatterns = [
    path('create_post', PostCreateView.as_view(), name='post_create'),
    path('home', PostListView.as_view(), name='home_page'),
    path('post/<slug:id>', PostUpdateView.as_view(), name='post_update'),
]
