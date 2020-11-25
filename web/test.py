from django.test import TestCase , Client 
from web.models import Author, Comment, Post , GenBook , Author, UserBook
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


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_superuser(
            username='test321',
            password='test321',
        )

        GenBook.objects.create(
            nameGen = 'fantasy'
        )
        Author.objects.create(
            first_name = 'hola1',
            last_name = 'hola2'
        )
        
            # genre= ['fantasy'],
        Post.objects.create(
            title='test321',
            content='test321',
            author_id=1,
            previewContent='hola',
            year='23132',
            publisher='hola',
            image='2313',
            postedBy_id=1,
            base_price=21313,
            data_posted='2002-07-02T00:00:00.000Z')
        

        self.client.force_login(user)
# TEST VIEWS GENERIC
    def test_about_GET(self):
        response = self.client.get(reverse('Booklary-about'))
        self.assertEquals(response.status_code,200)    
        self.assertTemplateUsed(response,'web/views/about.html')
    def test_library_GET(self):
        response = self.client.get(reverse('Booklary-library'))
        self.assertEquals(response.status_code,200)
    def test_library_redirect_login_GET(self):
        c = Client()
        response = c.get(reverse('Booklary-library'))
        self.assertEquals(response.status_code,302 or 301)
    def test_libro_POST(self):
        response = self.client.post('/library/1/',{},  content_type='application/json')
        post = Post.objects.all().filter(title='test321').first()
        userBook = UserBook.objects.all().filter(post=post).first()
        self.assertRedirects(response, '/profile/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        self.assertIsNotNone( userBook  )    

# TEST APIS VIEWS
    def test_API_genBook_GET(self):
        response = self.client.get('/api/gen/')
        self.assertEquals(response.status_code ,200)    
    def test_API_genBook_POST(self):
        response = self.client.post('/api/gen/',{'nameGen':"hola"},  content_type='application/json')
        self.assertEquals(response.status_code ,201)    


class CommentFormTest(TestCase):
    @classmethod
    def test_comment(self):
        form_data = {'comment': 'holap4321' }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid(), True )