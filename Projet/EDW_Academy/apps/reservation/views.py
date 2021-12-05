from django.core.mail import send_mail

from apps.core import forms
from apps.eventcalendar.models import Camp, Module
from apps.reservation.models import CampOrder, ModuleOrder
from django.conf import settings
from apps.eventcalendar.models import Camp
from apps.reservation.models import CampOrder
import stripe
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductLandingPageViewCamp(TemplateView):
    template_name = "checkout.html"

    def get_context_data(self, **kwargs):
        orders = CampOrder.objects.get(id=1)
        context = super(ProductLandingPageViewCamp, self).get_context_data(**kwargs)

        context.update({
            "orders": orders,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        })
        return context


class ProductLandingPageViewModule(TemplateView):
    template_name = "checkoutModule.html"

    def get_context_data(self, **kwargs):
        orders = ModuleOrder.objects.get(id=1)
        context = super(ProductLandingPageViewModule, self).get_context_data(**kwargs)

        context.update({
            "orders": orders,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        })
        return context


def chargeCamp(request):
    orders = CampOrder.objects.get(id=1)
    price = 0

    # for order in orders:
    #     price += order.price
    #
    # price = price * 100

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount="500",
            currency='CHF',
            description='order camp',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')


def chargeModule(request):
    orders = ModuleOrder.objects.get(id=38)
    price = 0

    # for order in orders:
    #     price += order.price
    #
    # price = price * 100

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount="500",
            currency='CHF',
            description='module order',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')


def createOrder(request, camp_id):
    camp = Camp.objects.get(pk=camp_id)
    res = CampOrder(user=request.user, camp=camp, paid=False, status='Pending')
    res.save()

    send_mail(
        'Your reservation at Edelweisse',
        'Thanks for booking, if you wanna check ur reservation you can go on your profile and check it on the calendar. If there is any probleme please contact our admins with the Contact Us button on the bottom of your profile page when you are logged. ',
        settings.EMAIL_HOST_USER,
        [request.user.email],
        fail_silently=False
    )

    return redirect('checkoutCamp')


def createModule(request, module_name):
    module = Module.objects.get(title=module_name)
    resmod = ModuleOrder(user=request.user, module=module, paid=False, status='Pending')
    resmod.save()
    return redirect('checkoutModule')