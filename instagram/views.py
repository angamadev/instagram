from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,FormView
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from .forms.contact_form import ContactForm
from .forms.user_forms import LoginForm,UserRegisterForm,registro_view



# Create your views here.
# @method_decorator(login_required,name='dispatch')
class HomeView(TemplateView):
    template_name = 'general/home.html'
    
    
class MyLoginView(LoginView):
    template_name = 'general/login.html'  # Nombre de tu plantilla HTML
    redirect_authenticated_user = True  # Redirige a usuarios ya autenticados
    success_url = reverse_lazy('home')  # URL a la que redirigir después del inicio de sesión exitoso
    # form_class = LoginForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# @login_required
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("home"))


class ContactUsFormView(FormView):
    template_name = 'general/contact.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        
        nombre = form.cleaned_data["nombre"]
        email = form.cleaned_data["email"]
        comentario = form.cleaned_data["comentario"]
        message_content = (f'{nombre} con email {email} ha escrito lo siguiente: {comentario}')
        
        success = send_mail(
            ("formulario de contacto de mi web de Biblioteca"),
            message_content,
            "info@angamadev.com",
            ["angamadev@gmail.com"],
            fail_silently=False,
        )
            
        return super().form_valid(form)
    

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Página a la que redirigir después de cerrar sesión
    # success_url = reverse_lazy('home')  # URL a la que redirigir después del inicio de sesión exitoso

