from django.shortcuts import render,redirect
from .models import Event
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def bookings(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'bookings.html')
def events(request):
    dict_eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'events.html', dict_eve)