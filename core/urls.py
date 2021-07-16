from django.urls import path
from rooms import views as room_views

app_name = "core"
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
# HomeView는 클래스기 때문에 함수가 필요
