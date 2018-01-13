from django.conf.urls import url
from onCode.views import LeaderboardView, UserProfileDetailView

urlpatterns = [
    #url(r'^problem/(?P<pk>[0-9]+)/$',views.TaskDetailView.as_view(),name='task_detail'),
    url(r'^leaderboard/$', LeaderboardView.as_view(), name='leaderboard_view'),
    url(r'^userprofile/(?P<pk>[0-9]+)/$', UserProfileDetailView.as_view(), name='user-profile-view'),
]
