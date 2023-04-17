from django.contrib import admin
from webapp.models.todos import ToDo


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'deadline', 'status', 'project', 'type', 'created_at')
    list_filter = ('id', 'title', 'deadline', 'status', 'project', 'type', 'created_at')
    search_fields = ('title', 'deadline', 'text')
    fields = ('text', 'title', 'deadline', 'status', 'project', 'type', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at', 'created_at')

admin.site.register(ToDo, ToDoAdmin)
