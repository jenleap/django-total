from django.contrib import admin
from django import forms
from .models import Food, Measure

# Register your models here.


class MeasureForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = "__all__"

    def clean_custom_unit(self):
        unit = self.cleaned_data.get('unit')
        custom_unit = self.cleaned_data.get('custom_unit')
        if unit != '0' and custom_unit:
            raise forms.ValidationError('Custom unit must be set if unit is "custom".')
        return custom_unit


class MeasureInline(admin.StackedInline):
    model = Measure
    form = MeasureForm
    extra = 1

class FoodAdmin(admin.ModelAdmin):
    inlines = [MeasureInline]

admin.site.register(Food, FoodAdmin)