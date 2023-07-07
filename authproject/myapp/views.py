from django.shortcuts import render
from .models import Contact,User
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            remarks=request.POST['remarks']
        )
        msg="Contact Saved Successfully"
        contacts=Contact.objects.all().order_by('-id')[:3]
        print(contacts)
        return render(request,'contact.html',{'msg':msg,'contacts':contacts})
    else:
        
        return render(request,'contact.html')

def signup(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Address Already Registered.Try Again"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                )
                msg="User Sign Up Successfully"
                return render(request,'login.html',{'msg':msg})
            else:
                msg="Password and Confirm Password does not matched"
                return render(request,'signup.html',{'msg':msg})
    
    else:
        return render(request,'signup.html')

def login(request):
    return render(request,'login.html')