from django.urls import path
from . import views
# import한 views는 현재 폴더(같은 위치)에 있기 때문에 . import views


app_name = 'articles'
# 하위 항목에 같은 이름을 가지는 것이 있을 수 있기 때문에
# 설정 하나를 추가로 더 해줌 (articles앱 안의 detail을 가져올게와 같이)

urlpatterns = [
    # 여기서는 articles/ 를 넣지 않아도 됨, board의 urls로부터 올 것이기 때문에
    path('', views.index, name='index'), # 이 path 이정표를 name으로 부를게 - 변수지정
    path('<int:id>/', views.detail, name='detail'),
    # <int:id> 는 id값이 들어오는 공간을 의미. 데이터가 아님
    # -- 여기까지 read 기능

    
    # Create
    # 새글 쓸 빈 종이만 보여주기
    path('new/', views.new, name='new'),
    # 글 쓸 공간 만들기
    path('create/', views.create, name='create'),
]