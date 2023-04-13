from django.shortcuts import render,redirect

from .models import OurUser

# Create your views here.
def homepage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        opt=request.POST.get('opt')
        mes=request.POST.get('msg')

        obj=OurUser.objects.create(first_name=name,last_name=last_name,email=email,number=number, option=opt,message=mes)
        obj.save()

        message='Thank You for Contacting us...'
        print(name,last_name,number,opt,mes)
        return redirect('/')


        return render(request, 'index.html',{'mes':message})
    return render(request, 'index.html')

def project(request):
    return render(request, 'projects.html')

def cal(request):
    return render(request, 'cal.html')