from . import views
from django.urls import path
from django.views.generic.edit import CreateView


app_name = 'firsttune'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post1', views.Post1View.as_view(), name='post1'),
    path('education', views.EducationView.as_view(), name='education'),
    path('information', views.InformationView.as_view(), name='information'),
    path('africa', views.AfricaView.as_view(), name='africa'),
    path('about', views.AboutView.as_view(), name='about'),

    # path('featured/', views.FeaturedView.as_view(), name='featured'),
    # path('team/', views.TeamView.as_view(), name='team'),
    # path('contact/', views.ContactView.as_view(), name='contact'),



    

    
]


