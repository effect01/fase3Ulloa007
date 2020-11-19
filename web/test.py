from django.test import TestCase 
from web.models import Author, Comment, Post
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from web.form import CommentForm

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Author.objects.create(first_name='Isaac', last_name='Asimov2' )
    def test_object_name(self):
        author = Author.objects.get(id=1)
        expected_object = '%s %s' % ( author.first_name , author.last_name )
        self.assertEqual(expected_object, str(author))
    def test_object_firstname_maxlength(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length,65)

class TestUrl(TestCase):
    def test_detail_url(self):
        path = reverse('post-detail' , kwargs={'pk':1})
        self.assertEqual(path, '/library/1/')


class CommentFormTest(TestCase):
    @classmethod
    def test_forms(self):
        form_data = {'comment': 'holap4321' }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid(), True )