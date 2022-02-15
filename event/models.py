from django.db import models
from account.models import User
from .utils import Event_slug_generate,User_Event_slug_generate
from ckeditor.fields import RichTextField

# Create your models here.

class TransportService(models.Model):
    transport_name = models.CharField(max_length=200)

    def __str__(self):
        return self.transport_name


class Destination(models.Model):
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name

HIRE_GUIDE = {
    ('Yes', 'Yes'),
    ('No', 'No'),
}

CONFIRMATION_STATUS = {
    ('Pending', 'Pending'),
    ('Accept', 'Accept'),
    ('Reject', 'Reject'),
}

class AdminTouristEvent(models.Model):
    event_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    event_description = RichTextField()
    event_price = models.FloatField(null=True)
    traveling_location = models.CharField(max_length=500,null=True,)
    traveling_dates = models.DateField(auto_now=False, null=True)
    guider_confirmation = models.CharField(
        max_length=100, choices=HIRE_GUIDE, default='Yes')
    transport_service = models.ForeignKey(TransportService, on_delete=models.CASCADE,null=True)
    event_image = models.ImageField(upload_to='Admin_Event/images/',null=True)
    publish = models.CharField(
        max_length=100, choices=CONFIRMATION_STATUS, default='Pending')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.event_title
    
    def save(self, *args, **kwargs):
        self.slug = Event_slug_generate(self.event_title)
        super(AdminTouristEvent, self).save(*args, **kwargs) 



class UserTouristEvent(models.Model):
    event_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    event_Description = RichTextField()
    traveling_dates = models.DateField(auto_now=False, null=True)
    total_traveling_person = models.IntegerField()
    event_price = models.FloatField(null=True)
    traveller_location = models.CharField(max_length=500)
    traveller_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    guider_confirmation = models.CharField(
        max_length=100, choices=HIRE_GUIDE, default='Yes')
    transport_service = models.ForeignKey(TransportService, on_delete=models.CASCADE)
    event_image = models.ImageField(upload_to='User_Event/images/',null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.event_title
    
    def save(self, *args, **kwargs):
        self.slug = User_Event_slug_generate(self.event_title)
        super(UserTouristEvent, self).save(*args, **kwargs) 


# Create your models here.
class PaymentDetails(models.Model):
    transaction_id = models.CharField(max_length=500)
    ammount = models.FloatField(max_length=100)
    card_type = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    transaction_date = models.CharField(max_length=100)
    risk_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction_id