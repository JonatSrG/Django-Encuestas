from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = {"pub_date", "question_text"}
    inlines = [ChoiceInLine]
    list_display = ("question_text", "pub_date", "was_puplished_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

class QuestionInLine(admin.StackedInline):
    model = Choice
    extra = 3

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
