from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """ 型增加 __str__() 方法是很重要的，这不仅仅能给你在命令行里使用带来方便，
        Django 自动生成的 admin 里也使用这个方法来表示对象。 """
        return self.question_text
    


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently ?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_choice_vote_not_none(self):
        return self.votes >= 0 


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_info = models.CharField(max_length=500)
    article_content = models.CharField(max_length=5000)
    article_date = models.DateTimeField(max_length=500)
    article_author = models.CharField(max_length=100)
    article = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_title