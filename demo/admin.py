from csv import list_dialects
from django.contrib import admin

from demo.models import Book

# Register your models here.
# admin.site.register(Book)
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
  # fields = ["title", "description"]
  list_display = ["title", "description"]
  list_filter = ["published"]
  search_fields = ["title"]