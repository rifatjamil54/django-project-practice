from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
    if request.method == 'POST':
        v_name = request.POST.get('name')
        v_roll = request.POST.get('roll')
        v_number = request.POST.get('registration_number')
        v_year = request.POST.get('year')
        if v_name != '' and v_roll != '' and v_number != '' and v_year != '':
            Student.objects.create(m_name = v_name,m_roll = v_roll,m_number = v_number,m_year = v_year)
            return redirect('/show')

    return render(request,'studentapp/index.html')




def show(request):
    context = {
        'students':Student.objects.all()
     }
    return render(request,'studentapp/show.html',context)  

def edit(request, id):

    student_info_edit = Student.objects.get(id=id)# call singel id for editing

    if request.method == 'POST':

        v_name = request.POST.get('name')
        v_roll = request.POST.get('roll')
        v_number = request.POST.get('registration_number')
        v_year = request.POST.get('year')
        if v_name != '' and v_roll != '' and v_number != '' and v_year != '':
            Student.objects.filter(id=id).update(m_name = v_name,m_roll = v_roll,m_number = v_number,m_year = v_year)
            return redirect('/show')

    return render(request,'studentapp/edit.html',context={'student_info_edit':student_info_edit})

def delete(request,id):
    student_info_delete = Student.objects.get(id=id)
    student_info_delete.delete()
    return redirect("/show")
    

