from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime

from .models import Question

def create_question(question_text, days):
    """ 通过传入的question_text, days 创建新的question,days 为负值是过去时间，正值为将来时间 """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """ 对于未来发布的问题， was_published_recently() 应该返回 False """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)   



class QuestionIndexViewTests(TestCase):
    def test_no_quesiton(self):
        """ 如果没有question存在，则返回一个提示信息 """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No blogs are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_future_question(self):
        """ 验证在打开详情页的时候，如果pub_date为未来时间，返回404 """
        # pub_date = timezone.now() + datetime.timedelta(days=5)
        # future_question = Question(question_text='Future question.', pub_date=pub_date)
        # future_question.save()
        create_question(question_text='Future question.',days=5)
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_past_question(self):
        """ 如果问题的发布时间为过去的，打开详情页能够看到问题内容 """
        create_question(question_text='Past question.',days=-5)
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>'])


    def test_future_question_and_past_question(self):
        """ 当过时的问题和未来的问题同时存在的情况下，也只有past question 显示 """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_question(self):
        """ quesrion index 页面可以展示多个questions """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-6)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>','<Question: Past question 1.>']
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """ 如果question 的pub_date 在今天之后，返回 404 not found """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('blog:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """ 已发布的question，返回question_text """
        past_question = create_question(question_text='Past question.', days = -5)
        url = reverse('blog:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
