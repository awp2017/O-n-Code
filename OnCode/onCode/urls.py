from django.conf.urls import url
from onCode import views

urlpatterns = [
    url(r'^leaderboard/$', views.LeaderboardView.as_view(), name='leaderboard_view'),
    url(r'^Problem/(?P<pk>[0-9]+)/$',
        views.ProblemDetailView.as_view(),
        name='problem_detail'),
    url(r'^Problem/(?P<pk>[0-9]+)/ViewComments/$',
        views.ViewComments.as_view(),
        name="view_comment"),
    url(r'^Problem/(?P<pk>[0-9]+)/AddComment/$',
        views.AddComment.as_view(),
        name="add_comment"
        ),
    url(r'^problems/$', views.ProblemsListView.as_view(), name='problem_list_view'),  
    url(r'^userprofile/(?P<pk>[0-9]+)/$', views.UserProfileDetailView.as_view(), name='user-profile-view'),
    url(r'^create-user/$', views.UserCreateView.as_view(), name='user-create-view'),

]
