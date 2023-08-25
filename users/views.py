from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Rediriger vers la page de connexion
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Rediriger vers la page du tableau de bord
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# users/views.py
from django.shortcuts import render
@login_required
def dashboard(request):
    # Logique de la vue dashboard
    return render(request, 'dashboard.html')

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import ProjectAssignment

def download_submitted_project(request, assignment_id):
    assignment = get_object_or_404(ProjectAssignment, id=assignment_id)
    if assignment.submitted:
        file_path = assignment.uploaded_file.path
        with open(file_path, 'rb') as project_file:
            response = HttpResponse(project_file.read())
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = f'attachment; filename="{assignment.uploaded_file.name}"'
            return response
    else:
        return HttpResponse("Le projet n'a pas encore été soumis.")

from django.shortcuts import render

def upload_project(request):
    # Logique pour le chargement du projet par l'enseignant
    return render(request, 'upload_project.html')

from django.shortcuts import render

def upload_processed_project(request):
    # Logique pour le chargement du projet traité
    return render(request, 'users/upload_processed_project.html')


