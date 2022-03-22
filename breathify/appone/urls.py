from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), #levels page
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('registration/', views.registration, name="registration"),
    path('levelone/', views.levelone, name="levelone"), #level one - beach
    path('leveltwo/', views.leveltwo, name="leveltwo"), #level two - blue mountains
    path('levelthree/', views.levelthree, name="levelthree"), #level three - blue mountains
    path('levelfour/', views.levelfour, name="levelfour"), #level four - blue mountains


]
