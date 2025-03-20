from django.db import models

# Create your models here.
class Article(models.Model):
    # def objects, save, ... 등 models.model을 상속 받아서 씀
    # Django models를 검색해서 사용할 수 있는 클래스 확인
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 날짜, 시간을 사용자에게 입력 받을 때만 옵션값 X
    # DB에만 저장될 것, 보여지는 것은 title과 content
    # auto_now / auto_now_add