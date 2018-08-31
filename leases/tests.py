import datetime

from django.db.models import Max
from django.test import Client, TestCase

from .models import Lease, Charge, ChargeDetail

# Create your tests here.
class LeasesTestCase(TestCase):

    def setUp(self):

        # Create leases
        todays_date = datetime.datetime.now()
        future_date = todays_date + datetime.timedelta(days=800)

        #lease with end date
        a1 = Lease.objects.create(name="test1", start_date=todays_date, end_date=future_date)

        #lease without end date
        a2 = Lease.objects.create(name="test2", start_date=future_date)

        # Create charges.
        #Charge.objects.create(name="base rent")
        #Charge.objects.create(name="cam")

    def test_index(self):
        c = Client()
        response = c.get("/leases/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["leases"].count(), 2)

    def test_valid_lease_page(self):
        a1 = Lease.objects.get(name="test1")

        c = Client()
        response = c.get(f"/leases/{a1.id}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_lease_page(self):
        max_id = Lease.objects.all().aggregate(Max("id"))["id__max"]

        c = Client()
        response = c.get(f"/leases/{max_id + 1}")
        self.assertEqual(response.status_code, 404)
