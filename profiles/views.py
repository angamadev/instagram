from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import UserProfile
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
@method_decorator(login_required,name='dispatch')
class ProfileListView(ListView):
    model = UserProfile
    template_name = 'profiles/profile.html'
    context_object_name = "userprofiles"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["perfiles"] = UserProfile.objects.all()
        return context


@method_decorator(login_required,name='dispatch')
class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'profiles/profile_detail.html'
    context_object_name = "userprofile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["perfiles"] = UserProfile.objects.all()
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
        response = super().form_valid(form)
        messages.success(self.request, '¡La formacion ha sido Modificada correctamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('profiles/profile_detail.html')
