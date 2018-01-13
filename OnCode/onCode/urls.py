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
    url(r'^$', views.ProblemsListView.as_view(), name='problem_list_view'),
    url(r'^create-user/$', views.UserCreateView.as_view(), name='user-create-view'),
    url(r'^userprofile/(?P<pk>[0-9]+)/$', views.UserProfileDetailView.as_view(), name='user-profile-view'),
    url(r'^userprofile/(?P<pk>[0-9]+)/edit/$', views.UserUpdateView.as_view(), name='user-edit-profile-view'),
    url(r'^login', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout")

]
