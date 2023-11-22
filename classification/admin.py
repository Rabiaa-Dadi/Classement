from django.contrib import admin
from . models import *
# Register your models here.
class CompteAdmin(admin.ModelAdmin):
    list_display = ["user","roles"]
    class Meta:
        model = Compte
admin.site.register(Compte,CompteAdmin)
admin.site.register(Medecin)
admin.site.register(Patient)
admin.site.register(Spécialité)
admin.site.register(Ville)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["Name","email","message"]
    class Meta:
        model = Contact
admin.site.register(Contact,ContactAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["patient","medecin","body","rate"]
    class Meta:
        model = Commentaire
admin.site.register(Commentaire,CommentAdmin)