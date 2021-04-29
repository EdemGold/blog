from django.db import models
from django.contrib.auth.models import User
class Entry(models.Model):
    entry_title=models.CharField(max_length=200)
    entry_text=models.TextField()
    entry_date=models.DateTimeField(auto_now=True)
    entry_author=models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="entries"
    def __str__(self):
        return f'{self.entry_title}'

 
