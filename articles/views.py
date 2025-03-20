from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    # 전체 게시물 읽기
    # 전체 게시물이기 때문에 복수로
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)


def detail(request, id):
    # 하나의 아티클을 찾아야 하기 때문에 단수로
    article = Article.objects.get(id=id)

    context = {
        'article': article
    }

    return render(request, 'detail.html', context)