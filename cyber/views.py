from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import joblib
from .models import CyberLog
from .forms import CyberLogForm

model = joblib.load("cyber_model.pkl")

def cyber_form_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated

    if request.method == 'POST':
        form = CyberLogForm(request.POST)
        if form.is_valid():
            cyber_entry = form.save(commit=False)
            input_text = cyber_entry.log
            predicted_label = model.predict([input_text])[0]
            cyber_entry.predicted_label = predicted_label
            cyber_entry.save()
            return redirect('cyber_result', log_id=cyber_entry.id)
    else:
        form = CyberLogForm()
    
    return render(request, 'cyber/cyber_form.html', {'form': form})

def cyber_result_view(request, log_id):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated

    cyber_entry = get_object_or_404(CyberLog, id=log_id)
    return render(request, 'cyber/result.html', {'prediction': cyber_entry.predicted_label, 'log': cyber_entry.log})

def user_signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")
    
    return render(request, "cyber/signup.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("cyber_form")
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "cyber/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")
