from django.db import models

class TextBox(models.Model):
    content = models.TextField()
    page_identifier = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id', 'page_identifier']