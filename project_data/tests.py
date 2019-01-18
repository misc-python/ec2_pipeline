"""To test django project."""
from django.test import TestCase, RequestFactory
from .models import Kickstarter
# from django.contrib.auth.models import User


class TestKickstarterModel(TestCase):
    """To test book model."""
    def setUp(self):
        """To setup class."""
        # self.user = User.objects.create_user('user_test', 'test@test.com', 'testuser123')
        self.kickstarter = Kickstarter.objects.create(kickstarter_id='0000001', name='test project 1', category='test category')

    def test_kickstarter_names(self):
        """To test titles of kickstarters."""
        one = Kickstarter.objects.get(name='test project 1')
        self.assertEqual(one.name, 'test project 1')

    def test_kickstarter_category(self):
        """To test category of kickstarters."""
        kickstarters = Kickstarter.objects.all()
        self.assertEqual(kickstarters[0].category, 'test category')

    def test_create_new_kickstarter(self):
        """To test creating a new kickstarter."""
        new_kickstarter = Kickstarter.objects.create(kickstarter_id='0000002', name='test project new', category='test category new')
        self.assertEqual(new_kickstarter.name, 'test project new')


class TestProjectDataViews(TestCase):
    """
    """
    def setUp(self):
        """To set up class."""
        self.request = RequestFactory()
        # self.user = User.objects.create_user('user_test', 'test@test.com', 'testuser123')
        self.kickstarter = Kickstarter.objects.create(kickstarter_id='0000001', name='test project 1', category='test category')
        # Kickstarter.objects.create(kickstarter_id='0000002', name='test project 2', category='test category')

    def test_kickstarter_list_view_context(self):
        """To test content of kickstarter_list_view."""
        from .views import kickstarter_list
        request = self.request.get('')
        # request.user = self.user
        response = kickstarter_list(request)
        self.assertIn(b'test project 1', response.content)

    def test_kickstarter_list_view_status(self):
        """To test status code of kickstarter_list_view."""
        from .views import kickstarter_list
        request = self.request.get('')
        # request.user = self.user
        response = kickstarter_list(request)
        self.assertEqual(200, response.status_code)

    def test_kickstarter_list_view_context(self):
        """To test content of kickstarter_list_view."""
        from .views import kickstarter_list
        request = self.request.get('')
        # request.user = self.user
        response = kickstarter_list(request)
        self.assertIn(b'test project 1', response.content)

