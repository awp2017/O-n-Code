from django.conf.urls import url
import views

urlpatterns = [
    url(r'^leaderboard/$', views.LeaderboardView.as_view(), name='leaderboard_view'),
    url(r'^Problem/(?P<pk>[0-9]+)/$',
        views.ProblemDetailView.as_view(),
        name='problem_detail'),

]
