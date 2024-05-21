from django.urls import path

from .views import PostCreateView, PostListView, PostUpdateView, PostDeleteView, PublicPostListView

app_name = 'post'

urlpatterns = [
    path('', PublicPostListView.as_view(), name='public_post_list'),
    path('create_post', PostCreateView.as_view(), name='post_create'),
    path('home', PostListView.as_view(), name='home_page'),
    path('post/<slug:id>', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:id>/delete', PostDeleteView.as_view(), name='post_delete'),
]
