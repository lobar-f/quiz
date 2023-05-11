from django.contrib import admin
from .models import Category, Tag, Quiz, Feedback, Question, MultipleChoiceOption, Answer

class MultipleChoiceOptionInline(admin.TabularInline):
    model = MultipleChoiceOption
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [MultipleChoiceOptionInline]
    list_display = ('text', 'quiz', 'display_options')

    def display_options(self, obj):
        options = obj.multiplechoiceoption_set.all()
        return ', '.join([f"{option.text} ({'Correct' if option.is_correct else 'Incorrect'})" for option in options])
    display_options.short_description = 'Options'

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Quiz)
admin.site.register(Feedback)
admin.site.register(Question, QuestionAdmin)
admin.site.register(MultipleChoiceOption)
admin.site.register(Answer)
