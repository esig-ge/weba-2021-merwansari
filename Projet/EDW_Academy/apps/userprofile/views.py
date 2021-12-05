from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

from .forms import LoginForm, SignUpForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.



def loginView(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'The email address or password is not valid')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return render('logout')


def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            userFirstName = form.cleaned_data.get('first_name')
            userLastName = form.cleaned_data.get('last_name')
            userEmail = form.cleaned_data.get('email')
            form.save(userFirstName)
            form.save(userEmail)
            messages.success(request,
                             'The profile \'' + userLastName + ' ' + userFirstName + '\' has been successfully '
                                                                                     'created !')
            email_subject ='Your account was succefully created'
            EmailMessageInscription = render_to_string('Email_template.html', {'name':userFirstName})
            send_mail(
                email_subject,
                EmailMessageInscription,
                settings.EMAIL_HOST_USER,
                [userEmail],
                fail_silently=False

            )

            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def myaccount(request):
    user = request.user

    context = {
        'user': user
    }
    return render(request, 'myaccount.html', context)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_changed')


def password_changed(request):
    return render(request, 'password_changed.html', {})

# def success(request, uid):
#     template = render_to_string('templates/Email_template.html', {'name' :request.user.profile.first_name})
#
#     email = EmailMessage(
#         'Merci de votre inscription chez Edelweiss Gaming Academy!' ,
#         template,
#         settings.EMAIL_HOST_USER,
#         [request.user.profile.email],
#         fail_silently=False,
#         )
