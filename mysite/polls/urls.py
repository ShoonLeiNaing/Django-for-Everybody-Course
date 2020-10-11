from django.urls import path

from . import views

urlpatterns = [
    path('login',views.ProtectView.as_view(),name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('owner/',views.owner,name='owner'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('guess',views.guessingGame.as_view()),
    path('cookie',views.cookie,name='cookie')
]