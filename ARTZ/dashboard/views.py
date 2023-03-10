from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from dashboard.models import Patient, Doctor
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):  
    if request.method == 'POST':
        # print("I am working")
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        username = request.POST['username'] 
        password = request.POST['password']
        password2 = request.POST['password2'] 
        user_type = request.POST['user_type']
        
        
        
        count = 11
        if len(phone) != count:
            messages.info(request, 'Invalid Phone Number! Must be 10 digits')
            return redirect('register')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already in Use')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already in Use')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
                user.save()

                if user_type == "patient":
                    new_patient = Patient(user=user, first_name=firstname, last_name=lastname, phone_number=phone)
                    new_patient.save()
                    
                else:
                    user_type == "doctor"
                    new_doctor = Doctor(user=user, first_name=firstname, last_name=lastname)
                    new_doctor.save()                  
                return redirect('login')
        else:
            messages.info(request, 'Password not the same!')
            return redirect('register')
        
       
    else:
        return render(request, 'register.html') 
   

def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user == Doctor:
                return redirect('staffDashboard')
            else:
                user == Patient
                return redirect('userDashboard')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

