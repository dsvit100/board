from django.shortcuts import render, redirect
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


# Create

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', id=article.id)


# Delete
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')


def edit(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article,
    }
    return render(request, 'edit.html', context)


def update(request, id):
    # 기존정보
    article = Article.objects.get(id=id)
    # 새로운 정보
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', id=article.id)