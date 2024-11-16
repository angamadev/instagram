from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .models import Post
from django.contrib import messages
from django.urls import reverse_lazy
from instagram.forms.post_create_form import PostCreateForm
from django.utils.translation import gettext_lazy as _lazy
from django.utils.translation import gettext as _



# Create your views here.
class PostCreateView(CreateView):
    model=Post
    form_class = PostCreateForm
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS,_('Post creado correctamente!'))
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')
    
class PostListView(TemplateView):
    template_name = 'posts/post_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publicaciones"] = Post.objects.filter()
        return context
