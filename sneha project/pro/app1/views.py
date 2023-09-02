from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')
def service(request):
#   
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')    
