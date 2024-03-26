import string

from django.contrib import auth
from django.contrib.auth.models import User
import requests
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
import random


# Create your views here.
def hello1(request):
    return HttpResponse("<center><font color='blue'>Welcome to TTM Homepage</font color></center>")
def hello(request):
    return render(request,'hello123.html')
def newhomepage(request):
    return render(request,'newhomepage.html')
def travelpackage(request):
    return render(request,'travelpackage.html')
def print1(request):
    return render(request,'printtoconsole.html')
def printtoconsole(request):
    if request.method == "POST":
        user_input = request.POST['Harika']
        print(f'User input:{user_input}')
    #return HttpResponse("Form submitted Successfully")
    a1={'user_input':user_input}
    return render(request,'printtoconsole.html',a1)

def random123(request):
   ran1 = ''.join(random.sample(string.digits, k=6))
   print(ran1)
   a2={'ran1':ran1}
   return render(request, 'random123.html', a2)

def RandomOtp(request):
    if request.method == "POST":
        input1 = request.POST['input1']
        input2 = int(input1)
        result_str = ''.join(random.sample(string.digits, k=input2))
        print(result_str)
        context = {'result_str': result_str}
    return render(request, 'RandomOtp.html', context)

def rand1(request):
    return render(request, 'RandomOtp.html')
def getdate1(request):
    return render(request,'get_date.html')


import datetime
from django.shortcuts import render

def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date =date_value + datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
        return render(request,'get_date.html',{'form':form})

def tzfunctioncall(request):
    return render(request, 'pytzExample.html')

# def tzfunctionlogic(request):
#     list1 =['Africa/juba','America/chicago']
#     if request.method == "POST":
#         input1 = request.POST['input1']
#         time1=pytz.timezone(input1)
#         print("Current Time is:")

def formExmp(request):
    return render(request, 'formExample.html')
from .models import*
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1 ="Email already exists. Choose another one"
            return render(request, 'formExample.html')
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request, 'formExample.html')



#-------piechart--------------
import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'PieChart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'PieChart.html', {'form': form})

def Pie(request):
    return render(request, 'PieChart.html')

def Pics(request):
    return render(request, 'BeautifulPics.html')

import requests
def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '6f329cb4617cdebb502f7ae74c50fac4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'Weather.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'Weather.html', {'error_message': error_message})


def WeatherCall(request):
    return render(request, 'Weather.html')





from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        pass2= request.POST['password']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
        else:
            messages.info(request,'password do not match')
            return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')