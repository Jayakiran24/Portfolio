from django.urls import path
from app import views
urlpatterns = [
    path("",views.home,name='home'),
    path("about/",views.about,name="about"),
    path("project/",views.project,name='project'),
    path("certificates/",views.certificates,name='certificates'),
    path("contact/",views.contact,name='contact'),
    path('resume/',views.resume,name='resume')
]