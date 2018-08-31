from django.db import models

CHAR_FIELD_LEN = 50

class Lease(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_LEN)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.name

class Charge(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    name = models.CharField(max_length=CHAR_FIELD_LEN)

    def __str__(self):
        return "Charges for %s" % self.name

class ChargeDetail(models.Model):
    charge = models.ForeignKey(Charge, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    start_date = models.DateField()
    end_date = models.DateField()
