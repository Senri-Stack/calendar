from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.MyCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MyCalendar.as_view(), name='month'),
]