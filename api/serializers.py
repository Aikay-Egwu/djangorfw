from rest_framework import fields, serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tasks
    fields = '__all__'