from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Article

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text']
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date',]  # 增加过滤选项
    search_fields = ['question_text'] # 增加搜索选项



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Article)