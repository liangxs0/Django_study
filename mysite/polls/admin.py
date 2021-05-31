from django.contrib import admin
from .models import Question,Choice

# Register your models here.
# admin.site.register(Question)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QusstionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields':['pud_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pud_date' )




admin.site.register(Question, QusstionAdmin)
# admin.site.register(Choice, ChoiceInline)