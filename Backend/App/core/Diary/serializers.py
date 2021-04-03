from django.db.models import fields
from rest_framework import serializers
from core.Diary.models import DiaryEntry


class DiaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields='__all__'

class DiaryEntryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        exclude = ['last_edited',]