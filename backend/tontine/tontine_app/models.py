import uuid
from django.db import models


class Versement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    description = models.TextField()
    montant = models.DecimalField(max_digits=10, decimal_places=2,)
    date_versement = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_versement']

    def __str__(self):
        return str(self.id)