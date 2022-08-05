from . import views
from django.urls import path
from django.views.generic.edit import CreateView


app_name = 'firsttune'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('/post1', views.Post1View.as_view(), name='post1'),

    # path('featured/', views.FeaturedView.as_view(), name='featured'),
    # path('team/', views.TeamView.as_view(), name='team'),
    # path('contact/', views.ContactView.as_view(), name='contact'),



    

    
]


