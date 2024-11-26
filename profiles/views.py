from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView, ListView,FormView
from .models import UserProfile,Follow
from posts.models import Post
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ProfileFollow

# Create your views here.
@method_decorator(login_required,name='dispatch')
class ProfileListView(ListView):
    model = UserProfile
    template_name = 'profiles/profile_list.html'
    context_object_name = "profiles"
        
    def get_queryset(self):
        return UserProfile.objects.all().exclude(user=self.request.user)


@method_decorator(login_required,name='dispatch')
class ProfileDetailView(DetailView, FormView):
    model = UserProfile
    template_name = 'profiles/profile_detail.html'
    context_object_name = "userprofile"
    form_class = ProfileFollow

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["perfil"] = UserProfile.objects.all()
        context["publicaciones"] = Post.objects.all()
        return context
    
    def form_valid(self, form):
        profile_pk = form.cleaned_data.get('profile_pk')
        action = form.cleaned_data.get('action')
        following = UserProfile.objects.get(pk=profile_pk)
        
        if action == 'follow':
            Follow.objects.get_or_create(
                follower = self.request.user.profile,
                following = following                
            )
            messages.add_message(self.request, messages.SUCCESS,f'Siguiendo a {following.user.username}')
        elif action == 'unfollow':
            Follow.objects.filter(
                follower = self.request.user.profile,
                following = following                
            ).delete()
            messages.add_message(self.request, messages.SUCCESS,f'Dejando de seguir a {following.user.username}')
            
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("profiles:profile_detail",args=[self.get_object().pk])

    
    
@method_decorator(login_required,name='dispatch')
class ProfileUpdateView(UpdateView):
    model = UserProfile
    fields = [
        "user",
        "bio",
        "profile_picture",
        "birth_date",        
        ]
    template_name = 'profiles/profile_update.html'
    context_object_name = "profile"
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,'¡Perfil editado correctamente!')
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("profiles:profile_detail",args=[self.object.pk])
    
    def dispatch(self, request, *args, **kwargs):
        user_profile = self.get_object()
        if user_profile.user != self.request.user:
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)
