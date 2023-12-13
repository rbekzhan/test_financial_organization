import uuid

from django.db import models


class FinancialOrganization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    first_leader = models.CharField(max_length=100)
    board_of_directors = models.CharField(max_length=100)
    chairman = models.CharField(max_length=100)
    board_members = models.CharField(max_length=255)
    director = models.CharField(max_length=100)
    chief_accountant = models.CharField(max_length=100)
    BIN = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    license = models.CharField(max_length=100)


class FinancialOrganizationNews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(FinancialOrganization, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateField()