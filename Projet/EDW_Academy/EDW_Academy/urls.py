"""EDW_Academy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.core.views import home, camps, games, courses, discover_camp, improve_camp, get_json_game_data, get_json_camp_data, ticket
from apps.reservation.views import createOrder, ProductLandingPageViewCamp, chargeCamp, ProductLandingPageViewModule, chargeModule, createModule
from apps.userprofile.views import loginView, signupView, myaccount, PasswordsChangeView, password_changed
from apps.eventcalendar.views import calendarView
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

# from apps.reservation.views import (
#     CreateCheckoutSessionView,
#     SuccessView,
#     CancelView,
# )

urlpatterns = [

    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('camps/', camps, name='camps'),
    path('courses/', courses, name='courses'),
    path('games/', games, name='games'),
    path('discover_camp', discover_camp, name='discover_camp'),
    path('improve_camp', improve_camp, name='improve_camp'),
    # path('reservation/success/', success, name='success'),

    path('games-json/', get_json_game_data, name='games-json'),
    path('camps-json/<str:game>/', get_json_camp_data, name='camps-json'),
    path('improve-camp-order/<int:camp_id>/', createOrder, name="createorder"),
    path('create-course/<str:module_name>', createModule, name="createmodule"),
    path('ticket/', ticket, name='ticket'),

    #CampOrders

    path('checkout/', ProductLandingPageViewCamp.as_view(), name='checkoutCamp'),
    path('charge/', chargeCamp, name='chargeCamp'),

    #ModuleOrders

    path('checkoutModule/', ProductLandingPageViewModule.as_view(), name='checkoutModule'),
    path('chargeModule/', chargeModule, name='chargeModule'),



    # path('cancel/', CancelView.as_view(), name='cancel'),
    # path('success/', SuccessView.as_view(), name='success'),
    # path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),

    #Calendar



    # Authentification

    path('myaccount/', calendarView, name='myaccount'),
    path('login/', loginView, name='login'),
    path('signup/', signupView, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # Changement de mot de passe

    path('change_password/', PasswordsChangeView.as_view(template_name='change_password.html'), name='changepassword'),# changer de mot de passe dans le dashboard
    path('password_changed/', password_changed, name='password_changed'), # page qui apparait lorsque le mot de passe a été changé

    #Reset le mot de passe

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="reset_password"), # Affichage formulaire pour indiquer l'email

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent_message.html'), name="password_reset_done"), # Message de confirmation de l'envoi du mail

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name="password_reset_confirm"), # Formulaire pour choisir un mot de passe

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name="password_reset_complete") # Message de confirmation du changement de mot de passe

] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
