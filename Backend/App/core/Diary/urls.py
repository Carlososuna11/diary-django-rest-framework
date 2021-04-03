from django.urls import path
from core.Diary.views import *

urlpatterns = [
    path('diary-entries/',DiaryEntryListAPIView.as_view(),name='entries'),
    path('create/',DiaryEntryCreateAPIView.as_view(),name='create'),
    path('entry/<int:pk>/',DiaryEntryRetrieveDestroyAPIView.as_view(),name='retrieve'),
    path('update/<int:pk>/',DiaryEntryRetrieveUpdateAPIView.as_view(),name='update'),
]
