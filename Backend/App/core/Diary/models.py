from django.db import models
from django.utils import timezone
# Create your models here.


class DiaryEntry(models.Model):
    """
        Diary Entry (Entrada de Diario)
        
        Clase que representara el modelo de la entrada de datos
        al diario, cada Entrada de diario contendrá
    """

    title = models.CharField(max_length=50)
    feel = models.CharField(max_length=20)    
    description = models.TextField()
    image = models.ImageField(upload_to='core/Diary/static/Diary/img',null=True,blank=True)
    creation_date = models.DateField(default=timezone.now)
    last_edited = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['creation_date']

    def save(self,*args, **kwargs):
        self.last_edited = timezone.now()
        return super().save(*args, **kwargs)