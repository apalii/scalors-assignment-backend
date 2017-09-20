from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    DashboardListAPIView,
    DashboardViewSet,
    TaskListAPIView,
    ActiveTaskListAPIView,
    TaskViewSet,
)


urlpatterns = [
    url(r'^dashboards/$', DashboardListAPIView.as_view(), name='task-list'),

    url(r'^dashboards/(?P<pk>\d+)/$', DashboardViewSet.as_view({'get': 'retrieve',
                                                                'put': 'update',
                                                                'delete': 'destroy'}), name='dashboard-detail'),
    url(r'^tasks/$', TaskListAPIView.as_view(), name='task-list'),
    url(r'^tasks/active/$', ActiveTaskListAPIView.as_view(), name='taskactive-list'),
    url(r'^tasks/(?P<pk>\d+)/$', TaskViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='task-detail'),

]
