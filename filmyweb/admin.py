from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Aktor

# Register your models here.
#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ["opis"]
    list_display = ["tytul", "imdb_rating", "rok"]
    list_filter = ("rok",)
    search_fields = ("tytul",)

admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)