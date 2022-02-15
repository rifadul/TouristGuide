from django.shortcuts import render,redirect
from event.models import AdminTouristEvent,UserTouristEvent


# Create your views here.
def homePage(request):
    template_name = 'index.html'
    context ={}
    events = AdminTouristEvent.objects.all().filter(publish='Accept')
    # user_events = UserTouristEvent.objects.all()
    latest_event = AdminTouristEvent.objects.filter(publish='Accept').order_by('-id')[:1]
    print('test 1oo',latest_event)
    last_ten_in_ascending_order = reversed(latest_event)
    print('test 1',last_ten_in_ascending_order)

    print(latest_event)
    context = {
        'events':events,
        # 'user_events':user_events,
        'latest_event':last_ten_in_ascending_order,
    }
    return render(request, template_name,context)


