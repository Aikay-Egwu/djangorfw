from rest_framework.serializers import Serializer
from api.models import Tasks
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TasksSerializer

from .models import Tasks
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': '/task-list',
    'Detail View': '/task-detail/<str:pk>',
    'Create': '/task-create',
    'Update': '/task-update/<str:pk>',
    'Delete': '/task-delete/<str:pk>',
  }
  return Response(api_urls)

#show all apis
#def apiOverview(request):
#  return JsonResponse("API BASE POINT", safe=False)

@api_view(['GET'])
def taskList(request):
  tasks = Tasks.objects.all()
  #serialize all fields by setting many to True
  serializer = TasksSerializer(tasks, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
  tasks = Tasks.objects.get(id=pk)
  #serialize all fields by setting many to True
  serializer = TasksSerializer(tasks, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
  serializer = TasksSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
  
  return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
  task = Tasks.objects.get(id=pk)
  serializer = TasksSerializer(instance=task, data=request.data)

  if serializer.is_valid():
    serializer.save()
  
  return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
  task = Tasks.objects.get(id=pk)
  task.delete()
  
  return Response("Task Deleted")
