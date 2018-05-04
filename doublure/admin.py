from django.contrib import admin
from .models import Doublure, ResponseDoublure, ObjectifDoublure, SousTheme, ThemeDoublure, AnswerIntegerDoublure,\
    AnswerSelectMultipleDoublure, AnswerSelectDoublure, AnswerRadioDoublure, AnswerTextDoublure, AnswerBaseDoublure, \
    DescriptionDoublure


# Register your models here.

class ObjectifInline(admin.TabularInline):

    model = ObjectifDoublure
    ordering = ('soustheme',)
    extra = 0


class ThemeDoublureInline(admin.TabularInline):
    model = ThemeDoublure
    extra = 0



class SousThemeInline(admin.TabularInline):
    model = SousTheme
    ordering =  ('theme',)
    extra = 0




class AnswerBaseInline(admin.StackedInline):

    fields = ('objectif', 'body')
    readonly_fields = ('objectif',)
    extra = 0


class AnswerTextInline(AnswerBaseInline):
    model = AnswerTextDoublure



class AnswerRadioInline(AnswerBaseInline):
    model = AnswerRadioDoublure
    fields = ('objectif', 'body', 'comments')



class AnswerSelectInline(AnswerBaseInline):
    model = AnswerSelectDoublure


class AnswerSelectMultipleInline(AnswerBaseInline):
    model = AnswerSelectMultipleDoublure


class AnswerIntegerInline(AnswerBaseInline):
    model = AnswerIntegerDoublure

class DoublureAdmin(admin.ModelAdmin):


    inlines = [ThemeDoublureInline, SousThemeInline, ObjectifInline]

class ResponseDoublureAdmin(admin.ModelAdmin):
    list_display = ('doublure_uuid', 'stagiaire','numero_doublure', 'created','id')
    inlines = [AnswerTextInline, AnswerRadioInline, AnswerSelectInline, AnswerSelectMultipleInline, AnswerIntegerInline]
  # specifies the order as well as which fields to act on

    readonly_fields = ('doublure', 'created', 'updated', 'doublure_uuid')


admin.site.register(Doublure, DoublureAdmin)
admin.site.register(DescriptionDoublure)

admin.site.register(ResponseDoublure, ResponseDoublureAdmin)