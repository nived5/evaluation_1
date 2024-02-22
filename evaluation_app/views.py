from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from evaluation_app.form import Login_Form, customer_Form, work_manager_Form


# Create your views here.

def front_page(request):
    return render(request,'Front.html')

def dashboard(request):
    return render(request,'dash.html')

def login_view(request):
    if request.method == 'POST':
         username = request.POST.get('uname')
         password = request.POST.get('pass')
         user = authenticate(request,username = username,password = password)
         # print(user)
         if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('')
            elif user.is_workmanager:
                return redirect('dashboard')
            elif user.is_user:
                return redirect('dashboard')
         else:
            messages.info(request,'Invalid credentials')
    return render(request,'login.html')

def user_reg(request):
    form1 = Login_Form()
    form2 = customer_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = customer_Form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit = False)
            user.is_customer = True
            user.save()
            user1 = form2.save(commit = False)
            user1.user = user
            user1.save()
            return redirect('test4')
    return render(request,'registration.html',{'form1':form1,'form2':form2})

def publisher_reg(request):
    form1 = Login_Form()
    form2 = work_manager_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = work_manager_Form(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_workmanager = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('login_view')
    return render(request, 'publisher.html', {'form1': form1, 'form2': form2})