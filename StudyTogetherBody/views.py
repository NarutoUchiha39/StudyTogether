from django.shortcuts import render,redirect
from .models import Room
from .RForms import Roomform

def room(request,pk):
   
    room = Room.objects.get(id=pk)
    context = {'id':room}
    return render(request,'StudyTogetherBody/Room.html',context)

def Home(request):
    rooms = Room.objects.all().order_by('-id')
    print(rooms[1].updated)
    context = {'rooms':rooms}
    return render(request,'StudyTogetherBody/Home.html',context)

def forms(request):
    forms = Roomform()
    if(request.method=="POST"):
        formss = Roomform(request.POST)
        if(formss.is_valid):
            formss.save()
            return redirect('Home')
    context = {'forms':forms}
    return render(request,'StudyTogetherBody/rooms_form.html',context)

def updateRoom(request,pk):
    room1 = Room.objects.get(id=pk)
    forms = Roomform(instance=room1)
    if(request.method=="POST"):
        forms = Roomform(request.POST,instance=room1)
        if(forms.is_valid):
            forms.save()
            return redirect("Home")
    context = {'forms':forms}
    return render(request,'StudyTogetherBody/rooms_form.html',context)


def deleteRoom(request,pk):

    forms = Room.objects.get(id=pk)
    context = {'forms':forms}
    if(request.method == "POST"):
        forms.delete()
        return redirect("Home")
    return render(request,"StudyTogetherBody/DeleteConfirm.html",context)

    




