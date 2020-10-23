from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [

    # ex- polls
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view()),
    # ex- polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
