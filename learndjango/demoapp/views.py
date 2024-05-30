from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.

def home(request):
    return HttpResponse("<h1>This is first View</h1>")


def index(request):
    return HttpResponse("<h1>Home page</h1>")

def comment(request):
    return render(request,"comment.html",{"name":"Muneeb","age":21})

def subject(request):
    subjects=["maths","Science","History","Geography","Marathi"]
    return render(request,"subject.html",{"subjects":subjects})

def inputData(request):
    if request.method=="GET":
        # username=request.GET.get("username","")
        # return render(request,"input.html",{"username":username})
        return render(request,"input.html")
    
    elif request.method=="POST":
        username=request.POST.get("username")
        return render(request,"input.html",{"username":username})


# Class based View

class Book(View):
    def get(self,request):
        return render(request,"book.html")
    def post(self,request):
        bookname=request.POST.get("bookname")
        bookprice=request.POST.get("bookprice")
        return render(request,"book.html",{"bookname":bookname,"bookprice":bookprice})







