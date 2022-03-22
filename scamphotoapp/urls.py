from django.contrib import admin
from django.urls import path, include
from .views import index, Login, signup, Mypage, DeleteComfirm, Detail, Update, Share, judge, result, Create
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('mypage/', Mypage.as_view(), name='mypage'),
    path('share/', Share.as_view(), name='share'),
    path('judge/', judge, name='judge'), 
    path('result/', result, name='result'),
    path('create/', Create.as_view(), name='create'),
    path('delete/<int:pk>', DeleteComfirm.as_view(), name='delete-confirm'),
    path('share/detail/<int:pk>', Detail.as_view(), name='detail'),
    path('update/<int:pk>', Update.as_view(), name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)