# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect, reverse
# from django.urls import reverse_lazy
# from django.views import generic
from .forms import RegisterUserForm, LoginUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# from django.core.mail import send_mail


def home(request):
    return render(request, 'registration/home.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginUserForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'No valid input!')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html', {'form': form})

# def send_user_mail(request):
#     mail = send_mail('subject, 'content', 'email_sender', ['email_recipient'], fail_silently=True)
#
#     if mail:
#         messages.success(request, 'We sent')
#         return redirect('files')
#     else:
#         messages.error(request, 'No valid email!')

# class SignUpView(generic.CreateView):
#     form_class = RegisterUserForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/register.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'SignUp'
#         return context
