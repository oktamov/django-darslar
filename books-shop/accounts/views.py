from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from accounts.forms import CustomAuthenticationForm


class AccountLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "accounts/login.html"




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
