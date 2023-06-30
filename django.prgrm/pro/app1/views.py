from django.shortcuts import render
from app1.models import CustomUser,Book,images
from django.contrib.auth import authenticate,login,logout
from app1.forms import CustomForms,Bookform
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def signup(request):
        form=CustomForms()
        if(request.method=="POST"):
           form=CustomForms(request.POST)
           if(form.is_valid()):
              form.save()
              return home(request)
        return render(request,'signup.html',{"form":form})

def user_login(request):
    if (request.method=="POST"):
        username1=request.POST['username']
        password1=request.POST['password']
        user=authenticate(username=username1,password=password1)
        if user:
            login(request,user)
            request.session['user']=user.username
            return home(request)
        else:
            return HttpResponse("invalid user")
    return render(request,"user_login.html")
def AddData(request):
    data=Bookform()
    if(request.method=="POST"):
        data=Bookform(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            return home(request)
    return render(request,'lll.html',{"k":data})


def list(request):
    b=Book.objects.all()
    return render(request,'as.html',{"s":b})

def delete_book(request,p):
    b=Book.objects.get(pk=p)
    b.delete() 
    return list(request)


def view_book(request,p):
    b=Book.objects.get(pk=p)
    return render(request,'view.html',{'i':b})
def edit_book(request,p):
    b=Book.objects.get(pk=p)
    form=Bookform(instance=b)
    if (request.method == "POST"):
        form=Bookform(request.POST,request.FILES,instance=b)
        if (form.is_valid()):
            form.save()
            return home(request)
    return render(request,'lll.html',{'k':form})
def about(request):
    i=images.objects.all()
    return render(request,'about.html',{"img":i})
def search(request):
    if(request.method=="POST"):
        srch=request.POST['search']
        if srch:
            match=Book.objects.filter(Q(title__icontains=srch)|Q(author__icontains=srch))
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                 messages.error(request,"No result found")
                
        else:
           return search(request)
    return render(request,'search.html')

