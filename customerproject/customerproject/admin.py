from django.contrib import admin
from .models import TextBox

@admin.register(TextBox)
class TextBoxAdmin(admin.ModelAdmin):
    list_display = ['content', 'page_identifier', 'order']
    list_filter = ['page_identifier']
    search_fields = ['content']