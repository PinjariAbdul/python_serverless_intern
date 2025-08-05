from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from .models import Doctor, Patient

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Redirect based on user type after signup
            if user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on user type
                if hasattr(user, 'doctor') or user.user_type == 'doctor':
                    return redirect('doctor_dashboard')
                elif hasattr(user, 'patient') or user.user_type == 'patient':
                    return redirect('patient_dashboard')
                else:
                    return redirect('home')  # fallback
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})


@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

