from django.contrib import admin
from .models import Food, Profile


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'food_name',
        'status',
        'quantity',
        'address',
        'notes',
        'created_at',
    )
    list_filter = ('status',)
    search_fields = ('food_name', 'address', 'notes')


admin.site.register(Profile)
