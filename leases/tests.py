from django.db.models import Max
from django.test import Client, TestCase

from .models import Lease, Charge, ChargeDetail

# Create your tests here.
class LeasesTestCase(TestCase):

    def setUp(self):

        # Create leases.
        a1 = Lease.objects.create(name="test1")
        a2 = Lease.objects.create(name="test2")

        # Create charges.
        Charge.objects.create(name="base rent")
        Charge.objects.create(name="cam")

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["leases"].count(), 2)

    def test_valid_lease_page(self):
        a1 = Lease.objects.get(name="test1")

        c = Client()
        response = c.get(f"/{f.id}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_lease_page(self):
        max_id = Lease.objects.all().aggregate(Max("id"))["id__max"]

        c = Client()
        response = c.get(f"/{max_id + 1}")
        self.assertEqual(response.status_code, 404)
