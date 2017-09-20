from datetime import datetime, timedelta
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import viewsets

from todo_app.models import Dashboard, Task, Reminder
from .serializers import (
    TaskSerializer,
    DashboardSerializer,
    TaskEditSerializer,
    DashboardDetailSerializer,
    ReminderSerializer
)

from todo_app.tasks import send_reminder


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


class RemindersListCreateAPIView(ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def post(self, request, *args, **kwargs):
        print request.data['remind_about'], request.data['delay']
        execute_at = datetime.utcnow() + timedelta(seconds=int(request.data['delay']))
        send_reminder.apply_async((request.data['remind_about'],), eta=execute_at)
        return self.create(request, *args, **kwargs)


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


