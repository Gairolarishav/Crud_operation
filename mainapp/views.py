from django.shortcuts import render,redirect
from django.http import HttpResponse
from mainapp.models import Item
from django.contrib import messages

# Create your views here.
def form(request):
    itemlist=Item.objects.all()
    content= {
            'itemlist':itemlist
        }
    return render (request,"form.html",content)

def additem(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('lname') and request.POST.get("description") :
          name = request.POST.get('name')
          lname = request.POST.get('lname')
          desc = request.POST.get('description')
          data = Item(name = name,lname = lname,desc = desc)
          data.save()
          messages.info(request,"Item added successfully")
        else:
          messages.info(request,"Plz fill all information")
        
        itemlist=Item.objects.all()
        content= {
            'itemlist':itemlist
        }
    return render (request,"form.html",content)

def deleteitem(request,Itemid):
    item=Item.objects.get(id = Itemid)
    item.delete()
    messages.info(request,"Item deleted successfully")
    return redirect ('form')

def edititem(request,Itemid):
    sel_item=Item.objects.get(id = Itemid)
    itemlist=Item.objects.all()
    content={
        'sel_item':sel_item,
        'itemlist':itemlist
    }
    return render (request,"form.html",content)

def updateitem(request,Itemid):
    update_item=Item.objects.get(id = Itemid)
    if request.method=='POST':
      update_item.name = request.POST.get('name')
      update_item.lname = request.POST.get('lname')
      update_item.desc = request.POST.get('description')
      update_item.save()
      messages.info(request,"Item Updated successfully")
    return redirect ("form")