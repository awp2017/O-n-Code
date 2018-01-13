from django.conf.urls import url
from onCode.views import LeaderboardView

urlpatterns = [
    #url(r'^problem/(?P<pk>[0-9]+)/$',views.TaskDetailView.as_view(),name='task_detail'),
    url(r'^leaderboard/$', LeaderboardView.as_view(), name='leaderboard_view'),
]
