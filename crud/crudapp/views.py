from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def index(request):
    if request.method == 'POST':
        emp_id = request.POST.get('id')
        emp_name = request.POST.get('name')
        emp_email = request.POST.get('email')
        if emp_id != '' and emp_name != '' and emp_email != '':
            User.objects.create(e_id = emp_id, e_name = emp_name, e_email = emp_email)
            return redirect('/show')




    return render(request,'crud/index.html')


def show(request):
    context = {'user': User.objects.all()}
    return render(request,'crud/show.html', context)

def edit(request,id):
    user_info = User.objects.get(id=id)

    if request.method == 'POST':
        emp_id = request.POST.get('id')
        emp_name = request.POST.get('name')
        emp_email = request.POST.get('email')
        if emp_id != '' and emp_name != '' and emp_email != '':
            User.objects.filter(id=id).update(e_id = emp_id, e_name = emp_name, e_email = emp_email)
            return redirect('/show')
    else:
        return render(request,'crud/edit.html',context={'user_info': user_info})
def destroy(request, id):  
    user = User.objects.get(id=id)  
    user.delete()  
    return redirect("/show")  