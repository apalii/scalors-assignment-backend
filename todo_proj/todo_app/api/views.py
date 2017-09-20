from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import viewsets

from todo_app.models import Dashboard, Task
from .serializers import TaskSerializer, DashboardSerializer, TaskEditSerializer, DashboardDetailSerializer


class DashboardListAPIView(ListAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer

    def list(self, request, *args, **kwargs):
        response = super(DashboardListAPIView, self).list(request, *args, **kwargs)
        for entity in response.data:
            entity.update({'total_count': Task.objects.filter(task_dashboard=entity['pk']).count()})
        return response


class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardDetailSerializer

    def list(self, request):
        queryset = Dashboard.objects.all()
        serializer = DashboardSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ActiveTaskListAPIView(ListAPIView):
    queryset = Task.active.all()
    serializer_class = TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer

    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskEditSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)