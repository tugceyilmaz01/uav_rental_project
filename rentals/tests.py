import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse_lazy

from rentals.models import Brand, Category, UAV, Rental


# Create your tests here.

class BrandViewSetTestCase(TestCase):
    """
        test for listing brands : test_list_brand (GET)
        test for retrieving a brand : test_retrieve_brand (GET)
        test for creating a new brand : test_create_brand (POST)
        test for updating an existing brand : test_update_brand (PATCH)
        test for deleting a brand : test_delete_brand (DELETE)
    """

    def setUp(self) -> None:
        self.brand_1 = Brand.objects.create(name='Test Brand 1')
        self.brand_2 = Brand.objects.create(name='Test Brand 2', is_active=False)

    def _get_count(self):
        return Brand.objects.count()

    def test_list_brand(self):
        url = reverse_lazy('brand-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json.get('count'), self._get_count())

    def test_retrieve_brand(self):
        url = reverse_lazy('brand-detail', [self.brand_2.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json.get('name'), 'Test Brand 2')
        self.assertFalse(response_json.get('is_active'))

    def test_create_brand(self):
        url = reverse_lazy('brand-list')

        post_data = {
            'name': 'Test Brand 3',
            'is_active': True
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self._get_count(), 3)

    def test_update_brand(self):
        url = reverse_lazy('brand-detail', [self.brand_2.id])

        post_data = {
            'is_active': True
        }

        self.assertFalse(self.brand_2.is_active)
        response = self.client.patch(url, post_data,
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.brand_2.refresh_from_db()
        self.assertTrue(self.brand_2.is_active)

    def test_delete_brand(self):
        url = reverse_lazy('brand-detail', [self.brand_2.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(self._get_count(), 1)
        self.assertFalse(Brand.objects.filter(name='Test Brand 2',
                                              is_active=False).exists())


class CategoryViewSetTestCase(TestCase):
    """
        test for listing categories : test_list_category (GET)
        test for retrieving a category : test_retrieve_category (GET)
        test for creating a new category : test_create_category (POST)
        test for updating an existing category : test_update_category (PATCH)
        test for deleting a category : test_delete_category (DELETE)
    """

    def setUp(self) -> None:
        self.category_1 = Category.objects.create(name='Test Category 1')
        self.category_2 = Category.objects.create(name='Test Category 2',
                                                  is_active=False)

    def _get_count(self):
        return Category.objects.count()

    def test_list_category(self):
        url = reverse_lazy('category-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json.get('count'), self._get_count())

    def test_retrieve_category(self):
        url = reverse_lazy('category-detail', [self.category_2.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json.get('name'), 'Test Category 2')
        self.assertFalse(response_json.get('is_active'))

    def test_create_category(self):
        url = reverse_lazy('category-list')

        post_data = {
            'name': 'Test Category 3',
            'is_active': True
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self._get_count(), 3)

    def test_update_category(self):
        url = reverse_lazy('category-detail', [self.category_2.id])

        post_data = {
            'is_active': True
        }

        self.assertFalse(self.category_2.is_active)
        response = self.client.patch(url, post_data,
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.category_2.refresh_from_db()
        self.assertTrue(self.category_2.is_active)

    def test_delete_category(self):
        url = reverse_lazy('category-detail', [self.category_2.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(self._get_count(), 1)
        self.assertFalse(Category.objects.filter(name='Test Category 2',
                                                 is_active=False).exists())


class UAVViewSetTestCase(TestCase):
    """
        test for listing uavs : test_list_uav (GET)
        test for retrieving an uav : test_retrieve_uav (GET)
        test for creating a new uav : test_create_uav (POST)
        test for updating an existing uav : test_update_uav (PATCH)
        test for deleting an uav : test_delete_uav (DELETE)

    """

    def setUp(self) -> None:
        self.brand_1 = Brand.objects.create(name='DJI')

        self.category_1 = Category.objects.create(name='Drone', is_active=False)
        self.category_2 = Category.objects.create(name='Missile')

        self.uav_1 = UAV.objects.create(model='Test UAV 1',
                                        category=self.category_1,
                                        brand=self.brand_1)
        self.uav_2 = UAV.objects.create(model='Test UAV 2',
                                        category=self.category_2,
                                        brand=self.brand_1,
                                        is_active=False)

    def _get_count(self):
        return UAV.objects.count()

    def test_list_uav(self):
        url = reverse_lazy('uav-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json.get('count'), self._get_count())

    def test_retrieve_uav(self):
        url = reverse_lazy('uav-detail', [self.uav_2.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json.get('model'), 'Test UAV 2')
        self.assertFalse(response_json.get('is_active'))

    def test_create_uav(self):
        url = reverse_lazy('uav-list')

        post_data = {
            'model': 'Test UAV 3',
            'is_active': True,
            'brand': self.brand_1.id,
            'category': self.category_2.id
        }
        response = self.client.post(url, post_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self._get_count(), 3)

    def test_update_uav(self):
        url = reverse_lazy('uav-detail', [self.uav_2.id])

        post_data = {
            'is_active': True
        }

        self.assertFalse(self.uav_2.is_active)
        response = self.client.patch(url, post_data,
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.uav_2.refresh_from_db()
        self.assertTrue(self.uav_2.is_active)

    def test_delete_uav(self):
        url = reverse_lazy('uav-detail', [self.uav_2.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(self._get_count(), 1)
        self.assertFalse(Category.objects.filter(name='Test UAV 2',
                                                 is_active=False).exists())


class RentalViewSetTestCase(TestCase):
    """
        test for listing rentals : test_list_rental (GET)
        test for retrieving a rental : test_retrieve_rental (GET)
        test for creating a new rental : test_create_rental (POST)
        test for updating an existing rental : test_update_rental (PATCH)
        test for deleting a rental : test_delete_rental (DELETE)

    """

    def setUp(self) -> None:
        self.brand_1 = Brand.objects.create(name='DJI')

        self.category_1 = Category.objects.create(name='Drone', is_active=False)
        self.category_2 = Category.objects.create(name='Missile')

        self.uav_1 = UAV.objects.create(model='Test UAV 1',
                                        category=self.category_1,
                                        brand=self.brand_1)
        self.uav_2 = UAV.objects.create(model='Test UAV 2',
                                        category=self.category_2,
                                        brand=self.brand_1,
                                        is_active=False)

        self.user_1 = User.objects.create(first_name='Ali', last_name='Yılmaz',
                                          username='ali_yilmaz')
        self.user_2 = User.objects.create(first_name='Veli', last_name='Yılmaz',
                                          username='veli_yilmaz')

        self.rental_1 = Rental.objects.create(uav=self.uav_1, user=self.user_2,
                                              rental_start_date='2024-05-15',
                                              rental_end_date='2024-05-17')
        self.rental_2 = Rental.objects.create(uav=self.uav_2, user=self.user_1,
                                              rental_start_date='2024-05-01',
                                              rental_end_date='2024-05-02')
        self.rental_3 = Rental.objects.create(uav=self.uav_2, user=self.user_2,
                                              rental_start_date='2024-05-10',
                                              rental_end_date='2024-05-12')

    def _get_count(self):
        return Rental.objects.count()

    def test_list_rental(self):
        url = reverse_lazy('rental-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json.get('count'), self._get_count())

    def test_retrieve_rental(self):
        url = reverse_lazy('rental-detail', [self.rental_3.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json.get('uav'), self.uav_2.id)
        self.assertEqual(response_json.get('user'), self.user_2.id)

    def test_create_rental(self):
        url = reverse_lazy('rental-list')

        post_data = {
            'uav': self.uav_1.id,
            'user': self.user_2.id,
            'rental_start_date': '2024-05-10',
            'rental_end_date': '2024-05-12'
        }

        response = self.client.post(url, post_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self._get_count(), 4)

    def test_update_rental(self):
        url = reverse_lazy('rental-detail', [self.rental_1.id])

        post_data = {
            'rental_start_date': '2024-05-20',
            'rental_end_date': '2024-05-28'
        }

        self.assertTrue(self.rental_1.rental_start_date, '2024-05-15')
        self.assertTrue(self.rental_1.rental_end_date, '2024-05-17')
        response = self.client.patch(url, post_data,
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.rental_1.refresh_from_db()
        self.assertTrue(self.rental_1.rental_start_date, '2024-05-20')
        self.assertTrue(self.rental_1.rental_end_date, '2024-05-28')

    def test_delete_rental(self):
        url = reverse_lazy('rental-detail', [self.rental_3.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(self._get_count(), 2)
        self.assertFalse(Rental.objects.filter(uav=self.uav_2, user=self.user_2,
                                               rental_start_date='2024-05-10',
                                               rental_end_date='2024-05-12').exists())
