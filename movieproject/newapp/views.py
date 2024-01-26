from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import Movieform
# Create your views here.
def newproj(request):
    mv=movie.objects.all()
    context={'muvi':mv}
    return render(request, 'index.html',context)

def m(request,movieid):
    i=movie.objects.get(id=movieid)
    return render(request,'m.html',{'i':i})

def update(request,id):
    mov=movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES, instance=mov)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return render(request,'edit.html',{'form':form,'movie':mov})

def add(request):
    if request.method=='POST':
        mname=request.POST.get('moviename')
        mdesc = request.POST.get('moviedesc')
        mpict=request.FILES.get('moviepict')
        mobj=movie(name=mname,desc=mdesc,pict=mpict)
        mobj.save()

    return render(request,'add.html')

def delete(request,id):
    if request.method=='POST':
        mobj=movie.objects.get(id=id)
        mobj.delete()
        return redirect('/')
    return render(request,'delete.html')