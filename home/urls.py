from django.urls import path
from . import views
from todolist.views import CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('',views.index, name = 'index'),
    path('bmi/wellbeing/',views.wellbeing, name = 'bmi_wellbeing'),
    path('mental/',views.mental, name = 'mental'),
    path('wellbeing/',views.wellbeing, name = 'wellbeing'),
    path('bmi/',views.bmi, name = 'bmi'),
    path('bmi/underweight/', views.underWeight, name = 'underweight'),
    path('bmi/normal/',views.normal, name = "normal"),
    path('bmi/overweight/',views.overweight, name = "overweight"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

]