from django.contrib import admin
from django.utils.html import format_html
from car_db.models import Car, Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('car', 'sensor', 'pin', 'wire_color', 'display_color')


admin.site.register(Car)
admin.site.register(Note, NoteAdmin)
