from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,FormView
from .models import Post,Comments
from django.contrib import messages
from instagram.forms.post_create_form import PostCreateForm
from instagram.forms.comment_create_form import CommentCreateForm

from django.utils.translation import gettext_lazy as _lazy
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect,JsonResponse


# Create your views here.
@method_decorator(login_required,name='dispatch')
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
    
@method_decorator(login_required,name='dispatch')
class PostListView(TemplateView):
    template_name = 'posts/post_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publicaciones"] = Post.objects.all()
        return context
    
@method_decorator(login_required,name='dispatch')
class PostDetailView(DetailView,FormView):
    
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    form_class = CommentCreateForm
    
    def form_valid(self, form):
        form.instance.post = self.get_object()
        form.instance.user = self.request.user
        form.save()  # Agrego esta línea para guardar el comentario
        messages.add_message(self.request, messages.SUCCESS,_('Comentario añadido correctamente!'))
        return super(PostDetailView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse("posts:post_detail", args=[self.get_object().pk])

@login_required
def post_like(request,pk):
    post = Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        messages.add_message(request, messages.INFO, "Ya no te gusta esta publicacion.")
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        messages.add_message(request, messages.INFO, "Me gusta la publicacion")
    
    return HttpResponseRedirect(reverse("posts:post_detail", args=[pk]))
    
@login_required
def post_like_ajax(request,pk):
    post = Post.objects.get(pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        return  JsonResponse(
            {
                'message':'Ya no te gusta esta publicacion.',
                'liked': False,
                'nLikes': post.likes.all().count()
            }
        )
    else:
        post.likes.add(request.user)
        return  JsonResponse(
            {
                'message':'Me gusta la publicacion.',
                'liked': True,
                'nLikes': post.likes.all().count()
            }
        )
