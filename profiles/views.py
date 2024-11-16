from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView # ListView
from .models import UserProfile,Follow
from django.urls import reverse_lazy,reverse
from django.contrib import messages


# Create your views here.
# @method_decorator(login_required,name='dispatch')
# class ProfileListView(ListView):
#     model = UserProfile
#     template_name = 'profiles/profile.html'
#     context_object_name = "userprofiles"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["perfiles"] = UserProfile.objects.all()
#         return context


@method_decorator(login_required,name='dispatch')
class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'profiles/profile_detail.html'
    context_object_name = "userprofile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["perfil"] = UserProfile.objects.all()
        return context
    
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
