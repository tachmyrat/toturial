
# mixin bu haysydyr bir yasan view in icinde getirsek shol view girmek ucin hokman login eden bolmaly eger edilmedik bolsa ony login page ugratyar 
#class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#UserPassesTestMixin- bu haysydyr posty uytgedip bolman dine oz goshan posduny uytgeder yaly edyar
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title','summary', 'body','photo',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title','summary','body','photo',)
# shu ashakdaky kodun manysy haysydyr bir post goyandan authory ozi saylap bilmezden dine goyan postlaryny oz adyndan goymaklyk ucindir
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish dine super user Articlecreateviewe girip biler yaly etdik
    def test_func(self):
        return self.request.user.is_superuser
