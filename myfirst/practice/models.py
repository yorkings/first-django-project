from django.db import models
#from django.utils import timezone
# Create your models here.
class Member(models.Model):
    #class Status(models.TextChoices):
     #   DRAFT = 'DF','Draft'
       # PUBLISHED ="PB","published"
    #title =models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    last =models.CharField(max_length=255)
    email= models.EmailField(max_length=100)
   # slug =models.SlugField(max_length=255)
    #publish =models.DateTimeField(default=timezone.now)
    created =models.DateTimeField(auto_now=True)
    #status= models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    #class Meta:
     #ordering=['-publish']
     #indexes =[ 
     #   models.Index(fields=['publish']),
   #  ]
    def __str__(self) :
        return self.name

