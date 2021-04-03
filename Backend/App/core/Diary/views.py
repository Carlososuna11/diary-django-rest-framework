from django.db.models.expressions import Value
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from core.Diary.models import DiaryEntry
from core.Diary.serializers import *
import datetime
import locale

class DiaryEntryListAPIView(generics.ListAPIView):
    """Listar"""
    serializer_class = DiaryEntrySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        for instance in res.data:
            instance['image'] = None if instance['image'] is None else instance['image'].replace('/core/Diary','')
            descripcion = instance['description']
            if len(descripcion)>200:
                instance['description'] = descripcion[:200] + "..."
            instance['creation_date']=datetime.datetime.strptime(instance['creation_date'],'%Y-%m-%d').strftime("%d, %B %Y")
            instance['last_edited'] = datetime.datetime.fromisoformat(instance['last_edited']).strftime("%d/%m/%Y, %H:%M:%S")
        return res 

class DiaryEntryCreateAPIView(generics.CreateAPIView):
    serializer_class = DiaryEntryCreateUpdateSerializer


class DiaryEntryRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = DiaryEntrySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def get(self, request, *args, **kwargs):
        res = super().get(request, *args, **kwargs)
        res.data['last_edited'] = datetime.datetime.fromisoformat(res.data['last_edited']).strftime("%d/%m/%Y, %H:%M:%S")
        res.data['image'] = None if res.data['image'] is None else res.data['image'].replace('/core/Diary','')
        res.data['creation_date']=datetime.datetime.strptime(res.data['creation_date'],'%Y-%m-%d').strftime("%d, %B %Y")
        return res

class DiaryEntryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class =  DiaryEntryCreateUpdateSerializer

    def get(self, request, *args, **kwargs):
        res = super().get(request, *args, **kwargs)
        res.data['image'] = None if res.data['image'] is None else res.data['image'].replace('/core/Diary','')
        return res


    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()