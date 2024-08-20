from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("book/<int:id>", OtherPage.as_view(), name="other"),
    path('items/', SomeOtherPage.as_view(), name='item-list'),
]