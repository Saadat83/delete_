# тут прописываем логику кода
from audioop import reverse
from multiprocessing import context
from urllib import request
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
# from requests import request
from blog.models import Post
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    )
 

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'object_list'
    
class PostCreateView(CreateView):
    model = Post
    fields = ['tittle', 'content', 'author', 'post_date', 'image']


    def form_valid(self, form):
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context

class PostUpdateView(UpdateView):
    model = Post
    fields = ['tittle', 'content', 'image']

    def form_valid(self, form):
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog-home")
    # fields = ['tittle', 'content', 'image']

    # def product_delete_view(request, id):
    #     obj = get_object_or_404(Post, id=id)
    #     if request.method == "POST":
    #         obj.delete()
    #         return redirect('/')
    #     context = {
    #         "object": obj
    #     }
    #     return render (request, "blog/post_confirm_delete.html", context)

    # def form_valid(self, form):
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)