from django.shortcuts import render
from .models import Article

def welcome_home(request):
	articles = Article.objects.all();
	return render(request,'home/welcome_home.html', {'articles' : articles})
