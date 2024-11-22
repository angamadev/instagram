from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,FormView
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from .forms.contact_form import ContactForm
from .forms.user_forms import UserRegisterForm #,registro_view
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.models import User
from profiles.models import UserProfile
from posts.models import Post


# Create your views here.
# @method_decorator(login_required,name='dispatch')
class HomeView(TemplateView):
    template_name = 'general/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["perfiles"] = UserProfile.objects.all()
        context["last_posts"] = Post.objects.all().order_by('-created_at')[:5]
        return context

    
class RegisterView(CreateView):
    model=User
    form_class = UserRegisterForm
    template_name = 'general/registro.html'

    def form_valid(self, form):
        form.instance.created_by= self.request.user
        messages.add_message(self.request, messages.SUCCESS,_('Usuario Registrado correctamente!'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('login')

class MyLoginView(LoginView):
    template_name = 'general/login.html'  # Nombre de tu plantilla HTML
    redirect_authenticated_user = True  # Redirige a usuarios ya autenticados
    success_url = reverse_lazy('home')  # URL a la que redirigir después del inicio de sesión exitoso
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request,messages.SUCCESS,_('Usuario Logueado correctamente!'))
        return response


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     return context

# @login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO,_('Sesion cerrada correctamente'))
    return redirect(reverse_lazy("home"))


class ContactUsFormView(FormView):
    template_name = 'general/contact.html'
    form_class = ContactForm
    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        nombre = form.cleaned_data["nombre"]
        email = form.cleaned_data["email"]
        comentario = form.cleaned_data["comentario"]
        message_content = (f'{nombre} con email {email} ha escrito lo siguiente: {comentario}')
        success = send_mail(
            ("formulario de contacto de mi web de Instaconquer"),
            message_content,
            "info@angamadev.com",
            ["angamadev@gmail.com"],
            fail_silently=False,
        )
        messages.add_message(self.request,messages.SUCCESS, "Mensaje enviado correctamente")
        return super().form_valid(form)
    
    
class CustomLogoutView(LogoutView):
    next_page = 'login'  # Página a la que redirigir después de cerrar sesión
    success_url = reverse_lazy('home')  # URL a la que redirigir después del inicio de sesión exitoso

