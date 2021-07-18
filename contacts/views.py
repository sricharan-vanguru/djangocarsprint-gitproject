from django.core.checks import messages
from contacts.models import Contact
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        user_id = request.POST['user_id']
        car_title = request.POST['car_title']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']

        contact = Contact(car_id=car_id,car_title = car_title,user_id = user_id,
        firstname = firstname,lastname=lastname,customer_need = customer_need ,city = city ,state = state, 
        email = email,phone = phone,message = message)

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'New Car inquiry',
            'You have a new INQUIRY for the car ' + car_title + '. Please login to your admin panel for more info.',
            'vangurusricharan@gmail.com',
            [admin_email],
            fail_silently=False
        )
        contact.save()
        messages.success(request,'Your request has been submittes we will get back to you shortly')
        return redirect('/cars/'+car_id)