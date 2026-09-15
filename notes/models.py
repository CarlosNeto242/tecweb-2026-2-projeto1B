from django.db import models

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=200)
    id = models.BigAutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.id}.{self.title}"

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id}.{self.title}"