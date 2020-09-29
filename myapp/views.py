from django.shortcuts import render


# Create your views here.
def filter(request):
    return render(request,"filter.html",{"data":"chandramouli",'a':10,'b':25,'c':12})
