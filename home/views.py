from django.shortcuts import render,redirect
from django.views import View
from . models import Contact

# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request, 'index.html')
    
class AboutView(View):
    def get(self,request):
        return render(request, 'about.html')
    
class ContactView(View):
    def get(self,request):
        return render(request, 'contact.html')
    
    def post(self,request):
        name = request.POST.get('name')
        phone = request.POST.get('phone') 
        Contact.objects.create(name = name, phone = phone)
        return redirect('/')   