from django.shortcuts import render,redirect
from .models import UserTouristEvent,AdminTouristEvent
from .form import AdminTouristEventForm
from .models import PaymentDetails
import requests
import socket
from django.urls import reverse
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
# Create your views here

def TouristEventView(request):
    if request.user.is_authenticated:
        template_name = 'event/Create-Event.html'
        context ={}
        
        if request.method=='POST':
            form = AdminTouristEventForm(request.POST or None, request.FILES)
            if form.is_valid():
                event_creator = request.user
                event_title  = form.cleaned_data['event_title']
                event_description  = form.cleaned_data['event_description']
                traveling_dates  = form.cleaned_data['traveling_dates']
                # total_traveling_person  = form.cleaned_data['total_traveling_person']
                traveling_location = form.cleaned_data['traveling_location']
                event_price = form.cleaned_data['event_price']
                # traveller_destination = form.cleaned_data['traveller_destination']
                guider_confirmation = form.cleaned_data['guider_confirmation']
                transport_service = form.cleaned_data['transport_service']
                event_image = request.FILES['event_image']
                data  = AdminTouristEvent(event_creator=event_creator,event_title=event_title,event_description=event_description,traveling_dates=traveling_dates,traveling_location=traveling_location,event_price=event_price,guider_confirmation=guider_confirmation,transport_service=transport_service,event_image=event_image)
                data.save()
                return redirect('profile')
        else:
            form = AdminTouristEventForm()
            context={
                'form': form
            }
        return render(request,template_name,context)
    else:
        return redirect('signin')


def event_profile_view(request):
    if request.user.is_authenticated:
        template_name = 'event\profile-event.html'
        events = AdminTouristEvent.objects.filter(event_creator=request.user)
        context = {
            'events':events,
            } 
        return render(request, template_name,context)
    else:
        return redirect('signin')


def event_requriement(request):
    if request.user.is_authenticated:
        template_name = 'event/event_requirement.html'
        context = {}
        if request.method == 'POST':
            pass
        else:
            slug=request.GET.get('slug')
            print(slug)
            event = AdminTouristEvent.objects.get(slug=slug)
            context={
                'event':event
            }
            return render(request, template_name,context)        
    else:
        return redirect('signin')





def payment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            print(name)
            email = request.POST.get('email')
            print(email)
            people = request.POST.get('people')
            print(people)
            price = int(people) *354
            user = name
            store_id = 'pecel616d784f482e9'
            store_password = 'pecel616d784f482e9@ssl'
            payment_status_url = request.build_absolute_uri(reverse("payment_status")) 

            print(payment_status_url)
            mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_password)

            mypayment.set_urls(success_url=payment_status_url, fail_url=payment_status_url, cancel_url=payment_status_url, ipn_url=payment_status_url)

            mypayment.set_product_integration(total_amount=Decimal(price), currency='BDT', product_category='Mixed ', product_name='doctor', num_of_item=people, shipping_method='YES', product_profile='None')

            mypayment.set_customer_info(name=user, email=email, address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')

            mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')

            response_data = mypayment.init_payment()
            print (response_data)
            return redirect(response_data['GatewayPageURL'])
        return redirect('home')
    return redirect('signin')

@csrf_exempt
def payment_status(request):
    if request.method == 'POST' or request.method == 'post':
        print(request.POST)
        payment_data = request.POST
        transaction_id = payment_data['tran_id']
        ammount = payment_data['amount']
        card_type = payment_data['card_type']
        status = payment_data['status']
        transaction_date = payment_data['tran_date']
        risk_title = payment_data['risk_title']
        data = PaymentDetails(transaction_id=transaction_id,ammount=ammount,card_type=card_type,payment_status=status,transaction_date=transaction_date,risk_title=risk_title)
        print(data)
        data.save()

        return render(request,'payment/succes.html')

