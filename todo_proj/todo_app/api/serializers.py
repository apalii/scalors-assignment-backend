from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from todo_app.models import Dashboard, Task, Reminder


class DashboardSerializer(ModelSerializer):
    class Meta:
        model = Dashboard
        fields = [
            'name',
            'pk'
        ]


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'task',
            'created',
            'updated',
            'task_dashboard',
        ]


class DashboardDetailSerializer(ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Dashboard
        fields = [
            'name',
            'tasks',
        ]


class TaskEditSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'task',
            'is_done',
        ]


class ReminderSerializer(ModelSerializer):
    class Meta:
        model = Reminder
        fields = [
            'remind_about',
            'delay',
        ]
