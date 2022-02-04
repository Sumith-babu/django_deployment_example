from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        un=request.POST['username']
        p1=request.POST['password']
        user =auth.authenticate(username=un,password=p1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'check the login credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        un=request.POST['username']
        em=request.POST['email']
        p1=request.POST['password1']
        p2=request.POST['password2']
        if p1==p2:
            if User.objects.filter(username=un).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request,"email already used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=un,password=p1,first_name=fn,last_name=ln,email=em)
                user.save()
                messages.info(request,"user created")
                return redirect('login.html')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')