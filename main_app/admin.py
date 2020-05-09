from django.contrib import admin
from .models import Event, Comment

admin.site.register(Event)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'created_on', 'event', 'author')
    list_filter = ('created_on', 'author')
    search_fields = ('body', 'author')

# Register your models here.
