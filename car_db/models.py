from django.db import models
from django.utils import timezone

from colorful.fields import RGBColorField
from django.utils.html import format_html


class Car(models.Model):
    brand = models.CharField(max_length=50)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.brand


class Note(models.Model):
    car = models.ForeignKey(Car)
    sensor = models.CharField(max_length=50)
    pin = models.IntegerField()
    wire_color = models.CharField(max_length=100)
    create_date = models.DateTimeField(editable=False)
    update_date = models.DateTimeField()
    note = models.TextField(null=True, blank=True)
    color = RGBColorField()

    def display_color(self):
        return format_html(
            '<span style="width:5px;height:5px;color:{}">color</span>'.format(self.color)
        )
    display_color.short_description = 'Color'
    display_color.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.update_date = timezone.now()
        return super(Note, self).save(*args, **kwargs)
