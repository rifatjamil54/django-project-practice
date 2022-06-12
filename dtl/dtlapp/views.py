from django.shortcuts import render

# Create your views here.

def home(request):

    name = 'rifat'
    roll = 101
    deperment = 'computer'
    context = {'name':name,'roll':roll,'deperment':deperment}

    return render(request,'dtlapp/home.html',context)