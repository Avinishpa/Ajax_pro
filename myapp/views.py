from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def add_row(request):
    User.objects.create(
        f_name = request.POST['first_name'],
        l_name = request.POST['last_name'],
        mobile = request.POST['mobile']
    )
    return JsonResponse({'msg':'success'})