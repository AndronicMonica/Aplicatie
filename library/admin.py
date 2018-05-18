from library.models import Book, Imprumuturi
from django.contrib import admin



# Register your models here.


class BookModelAdmin(admin.ModelAdmin):
    list_display = ["titlu", "autor", "editura", "disponibilitate"]
    list_filter = ["autor"]
    search_fields = ["titlu", "autor"]

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('items.read_item'):
            return [f.name for f in self.model._meta.fields]
        return super(BookModelAdmin, self).get_readonly_fields(
            request, obj=obj
        )

class ImprumuturiModelAdmin(admin.ModelAdmin):
    list_display = ['nume_prenume', 'titlul_cartii', 'data_inceput', 'data_sfarsit', 'owner']
    list_filter = ["owner"]
    search_fields = ["owner", "data_inceput", "data_sfarsit", "titlu_carte"]

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('items.read_item'):
            return [f.name for f in self.model._meta.fields]
        return super(ImprumuturiModelAdmin, self).get_readonly_fields(
            request, obj=obj
        )


admin.site.register(Book, BookModelAdmin)
admin.site.register(Imprumuturi, ImprumuturiModelAdmin)