
from django.conf.urls import url

urlpatterns = [
    url(r'^problem/(?P<pk>[0-9]+)/$',
        views.TaskDetailView.as_view(),
        name='task_detail'),
]
