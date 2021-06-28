from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


@login_required()
def home(request):
    users = User.objects.all()
    return render(request, 'core/home.html', {'users': users})