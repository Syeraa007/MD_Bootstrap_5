from django.shortcuts import render

# Create your views here.
def mdb5(request):
    return render(request,'mdb5.html')

def parent(request):
    return render(request,'parent.html')

def child(request):
    return render(request,'child.html')