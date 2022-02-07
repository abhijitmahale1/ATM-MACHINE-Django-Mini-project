from django.shortcuts import render,HttpResponse,redirect
from .models import  Account 

# Create your views here.

def index(request):
	return render(request,"index.html")

def login(request):
	return render(request,"login.html")

#register        
def reg(request):
		#return render(request,"login.html")
    if request.method=="POST":
        fname=request.POST["fname"]
        anum=request.POST["anum"]
        num = request.POST["num"]
        email = request.POST["email"]
        password = request.POST["password"]

        app=Account(fname=fname,anum=anum,num=num,email=email,password=password)
        app.save()  #insert

        # return HttpResponse("Register succfull")
        return redirect("login")
    else:
        return HttpResponse("Fail")

#login
def logincheck(request):
    if request.method=="POST": 
        email=request.POST["email"] 
        password=request.POST["password"]   

        data=Account.objects.all().filter(email=email,password=password)

       # if len(data)==1:
    if data:
            request.session["username"]=email #Session Start
            return redirect("dashboard")
            #return HttpResponse("Success")
    else:
            return redirect ('/login')
            #return HttpResponse("Fail")

def dashboard(request):
    # data=Account.objects.all() 
    # return render(request,'dashboard.html',{'data':data})
    if request.session.get('username') is not None:
        return render(request,"dashboard.html") 
    else:
        return redirect("login")


def edit(request):
    email=request.session.get('username')
    data=Account.objects.all().filter(email=email)
    return render(request,"update.html",{'data':data})
    

def update(request):
    if request.method=="POST":
        email=request.POST['email']
        num=request.POST['num']
    
        password=request.POST['password']
            
        #update

        Account.objects.filter(email=email).update(num=num,email=email,password=password) 


        return redirect("/dashboard")
    else:
        return HttpResponse("Fail")


def debit(request):
    email=request.session.get('username')
    d=Account.objects.all().filter(email=email)
    return render(request,"withdraw.html",{'d':d})

def deb(request):
    if request.method=="POST":
        email=request.POST['email']
        debit=request.POST['debit']
        t=Account.objects.all().filter(email=email)
        for i in t:
            w=i.balance-int(debit)
            Account.objects.all().filter(email=email).update(balance=w)
            return redirect("withdraw")
        else:
            return HttpResponse("fail")


def withdraw(request):
    email=request.session.get('username')
    w=Account.objects.all().filter(email=email)
    return render(request,'balance.html',{'w':w})

def logout(request):
    del request.session["username"]
    return redirect("login")

        
    
