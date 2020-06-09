from django.shortcuts import render
from fifthapp.forms import studentForm
from fifthapp.models import student

# Create your views here.
def index(request):
    return render(request, 'fifthapp/index.html')

def media(request):
    return render(request, 'fifthapp/media.html')
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')

    student1=student.objects.all()
    student1.objects.filter(name = name)
    student1.objects.filter(roll=roll)
    if name in student1:
        print('username is matched')
        return redirect('/index')
    elif roll in student1:
        print('roll is also matched')
        return redirect('/index')
    else:
        print('login failed')
        return render(request,'/login')


    return render(request, 'fifthapp/login.html')

def add(request):
    form=studentForm()
    if request.method =='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            roll=request.POST.get('roll')
            branch=request.POST.get('branch')
            year=request.POST.get('year')
            email=request.POST.get('email')
            password=request.POST.get('password')
            student.name=name
            student.roll=roll
            student.branch=branch
            student.year=year
            student.email=email
            student.password=password
            form.save()
        return list(request)
    return render(request, 'fifthapp/add.html', {'form':form})


def list(request):
    student_list=student.objects.all()
    return render(request,'fifthapp/list.html', {'student_list':student_list})
