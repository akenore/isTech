from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(_('Full Name'), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=254)
    phone = PhoneNumberField(_("Phone Number"))
    subject = models.CharField(_("Subject"), max_length=250)
    message = models.TextField(_("Enter Message"))

    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

