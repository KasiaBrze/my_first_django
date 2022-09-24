"""my_first_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django_application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('hello/', views.hello),
    path('sum/', views.add),
    path('brothers/', views.brothers),
    path('fibonnaci/', views.fibonnaci),
    path('multiply/', views.multiply),
    path('game/', views.game),
    path('article/<int:id>/', views.article),
    path('greetings/<str:name>/<int:repeat>', views.greetings),
    path('calc/<int:number_a>/<str:operation>/<int:number_b>', views.calc),
    path('random/<int:min>/<int:max>/<int:throw>', views.random_generator),
    path('template/', views.show_template),
    path('form/', views.show_form),
    path('class/', views.FormView.as_view()), #klasa zawsze uruchamia .as_view
    path('metody/', views.metody),
    path('test/', views.TestView.as_view()),
    path('test/show', views.ShowTestView.as_view()),
    path('pizza/', views.PizzaView.as_view()),

]
