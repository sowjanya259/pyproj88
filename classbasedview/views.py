
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render


class GETInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class POSTInput(View):
    def post(self,request):
        return render(request,'postinput.html')
class Add(View):
    def get(self,request):
        try:
            a=request.GET['t1']
            x=int(a)
            b=request.GET['t2']
            y=int(b)
            z=x+y
            return HttpResponse("<html><body bgcolor=cyan><h1><sum is:" + str(z) + "</h1></body></html")
        except(ValueError):
            return HttpResponse("invalid input")
    def post(self,request):
        try:
            a = request.POST['t1']
            x = int(a)
            b = request.POST['t2']
            y = int(b)
            z = x + y
            return HttpResponse("<html><body bgcolor=cyan><h1><sum is:" + str(z) + "</h1></body></html")
        except(ValueError):
            return HttpResponse("invalid input")