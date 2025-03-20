from django.urls import path
from . import views
# import한 views는 현재 폴더(같은 위치)에 있기 때문에 . import views

urlpatterns = [
    path('', views.index) # 여기서는 articles/ 를 넣지 않아도 됨, board의 urls로부터 올 것이기 때문에
]