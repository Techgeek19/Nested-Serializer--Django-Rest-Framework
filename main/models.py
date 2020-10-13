from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.TextField(null=False, blank=False) 
    image = models.ImageField(blank=False, null=False)
    # tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.text

class Tag(models.Model):
    question = models.ForeignKey(Question, related_name='tags', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


