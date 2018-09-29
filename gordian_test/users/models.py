from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, null=True, max_length=255)
    session = CharField(_("Session ID"), blank=True, null=True, max_length=100)
    basket = TextField(_("Basket"), blank=True, null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
