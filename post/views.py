from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView

from .forms import PostCreateForm
from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('post:post_create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.is_draft is False:
            form.instance.published_at = timezone.now()
        return super().form_valid(form)


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'posts.html'
    context_object_name = 'objects'
    paginator_class = Paginator
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).all()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'post.html'
    slug_field = 'id'
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse('post:post_update', kwargs={'id': self.object.id})

    def get_object(self, queryset=None):
        return Post.objects.filter(user=self.request.user, id=self.kwargs['id']).first()
