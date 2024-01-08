from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.http import require_POST

from .models import Article, Comment
from .forms import CommentForm

class ArticleListView(LoginRequiredMixin, generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article/list.html'
class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article/detail.html'
    extra_context = {
        'form': CommentForm()
    }


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Article
    context_object_name = 'article'
    fields = ('title', 'slug', 'summary', 'body', 'photo')
    template_name = 'article/update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        author = self.get_object().author
        return author == self.request.user or self.request.user.is_superuser
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy('article_list')
    template_name = 'article/delete.html'

    def test_func(self):
        author = self.get_object().author
        return author == self.request.user or self.request.user.is_superuser
class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo')
    template_name = 'article/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_admin


@require_POST
def create_comment(request, pk, slug):
    article = get_object_or_404(Article,
                                pk=pk,
                                slug=slug)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            author = request.user
            Comment.objects.create(
                author=author,
                article=article,
                text=form.cleaned_data['text']
            )

            return redirect('article_detail', pk, slug)












