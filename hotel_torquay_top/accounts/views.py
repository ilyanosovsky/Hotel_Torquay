from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import SignupForm
from django.urls import reverse_lazy

# Create your views here.
class SignupView(CreateView):
    form_class = SignupForm
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy('homepage')
        return reverse_lazy('profile', kwargs={'pk' : user.pk})
    
class ProfileView(View):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        return render(request, 'profile.html', {'user' : user})
    
    
