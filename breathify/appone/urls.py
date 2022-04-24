from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), #levels page
    path('home', views.home, name="home"), #levels page
    path('relief', views.relief, name="relief"), #relief home page
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('registration/', views.registration, name="registration"),
    path('levelone/', views.levelone, name="levelone"), #level one - beach
    path('leveltwo/', views.leveltwo, name="leveltwo"), #level two - blue mountains
    path('levelthree/', views.levelthree, name="levelthree"), #level three - mystic river
    path('levelfour/', views.levelfour, name="levelfour"), #level four - Dark Forest
    path('levelfive/', views.levelfive, name="levelfive"), #level five - Night Breeze
    path('levelsix/', views.levelsix, name="levelsix"), #level six - Cosmic rain
    path('levelangry/', views.levelangry, name="levelangry"), #Sudden relief - I'm Angry
    path('leveldepressed/', views.leveldepressed, name="leveldepressed"), #Sudden relief - I'm depressed
    path('levelstressed/', views.levelstressed, name="levelstressed"), #Sudden relief - I'm stressed
    path('profile/', views.profile, name="profile"), #profile
]
