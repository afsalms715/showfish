from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import bookShop
from .forms import bookform
# Create your views here.
def home(request):
    obj=bookShop.objects.all()
    return render(request,'home.html',{'books':obj})

def detail(request,id):
    obj=bookShop.objects.get(id=id)
    return render(request,'details.html',{'book':obj})

def add(request):
    form = bookform(request.POST or None, request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    print(form)
    return render(request,'add.html',{'form':form})
def update(request,id):
    obj=bookShop.objects.get(id=id)
    form=bookform(request.POST or None, request.FILES or None,instance=obj)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request,'update.html',{'form':form})

def delete(request,id):
    obj=bookShop.objects.get(id=id)
    obj.delete()
    return redirect('home')

def search(request):
    key=request.GET['search']
    print(key)
    obj=bookShop.objects.filter(name=key).exists()
    if obj:
        obj2 = bookShop.objects.get(name=key)
        return render(request, 'details.html', {'book': obj2})
    else:
        messages.info(request,"not found")
        return redirect('home')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invaliid username or password')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
