from django.test import TestCase, Client
from .models import Article
from django.urls import reverse


class ArticleTestCase(TestCase):

    def setUp(self):
        Article.objects.create(
            title = 'Some title',
            description = 'Some Description',
            author = 'Albert'
        )

    def test_article_exist(self):
        """Created article exists in the database """
        article = Article.objects.get(title='Some title')
        self.assertEqual(article.author, 'Albert')


class ArticleCreateViewTest(TestCase):

    def setUp(self):
        client = Client()


    def test_article_created(self):
        """Created article saved in the database  """
        response = self.client.post(
            reverse('add_article'),
            {'title': 'Test title', 'description': 'Test description', 'author': 'Test author'}
        )
        self.assertEqual(response.status_code, 302)