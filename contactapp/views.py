from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def sendMessage(request):
    contact_form=ContactForm
    if request.method=='POST':
        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save() 
    context={
        'contact_form':contact_form
    }
    return render(request,'contactapp/contact.html',context)