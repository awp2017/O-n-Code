from django.conf.urls import url
from onCode.views import (LeaderboardView, UserProfileDetailView, 
                        AddComment, ViewComments, ProblemDetailView)

urlpatterns = [
    url(r'^leaderboard/$', LeaderboardView.as_view(), name='leaderboard_view'),
    url(r'^userprofile/(?P<pk>[0-9]+)/$', UserProfileDetailView.as_view(), name='user-profile-view'),
    url(r'^Problem/(?P<pk>[0-9]+)/$',ProblemDetailView.as_view(),name='problem_detail'),
    url(r'^Problem/(?P<pk>[0-9]+)/ViewComments/$',ViewComments.as_view(),name="view_comment"),
    url(r'^Problem/(?P<pk>[0-9]+)/AddComment/$',AddComment.as_view(),name="add_comment")
]
