from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from firstapp.models import Employee

# Create your views here.
def employeeView(request):
  data = Employee.objects.all()
  response = {'employees': list(data.values('name', 'sal'))}

  return JsonResponse(response)