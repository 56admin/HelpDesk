from django.contrib import admin

from .models import Start_task


class Start_taskAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_dr', 'created_up', 'end_task')
    list_display_links = ('title',)
    search_fields = ('title', 'content')


admin.site.register(Start_task, Start_taskAdmin)