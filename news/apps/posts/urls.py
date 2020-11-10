from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('/start_search/', views.start_search, name = 'start_search'),
	]
