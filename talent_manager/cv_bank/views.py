from django.shortcuts import render

# Create your views here.
def cv_bank_home(request):
    return render(request,'cv_bank/home.html')

def add_profile(request):
    return render(request,'cv_bank/add-profile.html')
