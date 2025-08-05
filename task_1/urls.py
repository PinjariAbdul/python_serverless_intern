from django.urls import path
from .views import signup_view, login_view, doctor_dashboard, patient_dashboard, CustomLogoutView
from django.shortcuts import redirect

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('', lambda request: redirect('signup/')),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Works with GET
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
]
