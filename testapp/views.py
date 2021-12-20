from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from testapp.forms import UserForm
from .models import User

# Create your views here.

def add_retriew_data(request):
    if request.method =='POST':
        fm= UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm= UserForm()
    else:
        fm= UserForm()
    data = User.objects.all()
    return render(request, 'addstudent.html', {'form':fm, 'Data':data})

def update_data(request,id):
    if request.method == 'POST':
        data= User.objects.get(pk=id)
        fm= UserForm(request.POST, instance=data)
        if fm.is_valid:
            fm.save()
            
    else:
        data= User.objects.get(pk=id)
        fm= UserForm(instance=data)
    return render(request, 'updatestudent.html', {"form":fm, 'Data':data})


def deletestudent(request,id):
    if request.method =='POST':
        print("hiiiiiiiiiiiiiiiiiii")
        data = User.objects.get(pk=id)
        print('get data sucess')
        data.delete()
        print('delete data sucess')
        return HttpResponseRedirect('/')


