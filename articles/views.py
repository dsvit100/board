from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    # 전체 게시물 읽기
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)