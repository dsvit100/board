from django.contrib import admin
from .models import Article

# Register your models here.

# 관리자 페이지에서 Article 관리 페이지를 만들기
admin.site.register(Article) # admin 사이트에 Article 추가해줘