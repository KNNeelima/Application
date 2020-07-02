from django.shortcuts import render
from testapp.forms import ApplicatonForm,SignUpForm
from testapp.models import AppForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.


def index_view(request):
    return render(request,'testapp/index.html')

@login_required
def rg1_view(request):
    form=ApplicatonForm()
    if request.method=="POST":
        form=ApplicatonForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Data is inserting into the table")
            return Thanks_view(request)
    return render(request,'testapp/rg.html',{'form':form})
# def rg_view(request):
#     form=ApplicatonForm()
#     if request.method=="POST":
#         form=ApplicatonForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             print("Data is going to table")
#             return index_view(request)
#     return render(request,'testapp/rg.html',{'form':form})

def Thanks_view(request):
    return render(request,'testapp/Thanks.html')



def list_of_applicaions(request):
    application_list=AppForm.objects.all()
    return render(request,'testapp/list.html',{'application_list':application_list})


def logout_view(request):
    return render(request,'testapp/logout.html')


def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request,'testapp/signup.html',{'form':form})
