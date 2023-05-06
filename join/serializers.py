from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from board.models import Task

class TaskSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['created_at','title', 'description','user',]#'category','priority','subtasks']
        
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializers
    permission_classes = [] #permission.IsAuthenticated