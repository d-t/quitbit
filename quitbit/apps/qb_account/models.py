from django.db import models
from django.db.models.signals import post_save
from django.core import validators
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# from emailconfirmation.models import EmailAddress
from apps.qb_main.utils import now
from apps.qb_main.models import Cigarette
from signals import password_changed

import re

user = settings.AUTH_USER_MODEL

SEX_CHOICES = (
    ('M', _('male')),
    ('F', _('female'))
)


# Entity User
class QuitBitUser(AbstractUser):
    """
    Auth User Model
    Contains personal info of a user
    """

    # Personal fields
    about = models.TextField(_('about me'), blank=True)
    gender = models.CharField(_('gender'), max_length=1, choices=SEX_CHOICES, blank=True)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)

    # Address Info
    address = models.CharField(_('address'), max_length=150, blank=True)
    city = models.CharField(_('city'), max_length=30, blank=True)
    country = models.CharField(_('country'), max_length=30, blank=True)

    # Smoking Habits
    years_smoked = models.IntegerField(null=True, blank=True) # I'd create a method for this
    cigarettes_per_day = models.IntegerField(null=True, blank=True)
    packet_cost = models.FloatField(null=True, blank=True)
    cigarette_brand = models.CharField(null=True, blank=True, max_length=50)
    cigarette_type = models.CharField(null=True, blank=True, max_length=50)
    money_saved = models.FloatField(null=True, blank=True)   # maybe it's better to put this in a method
    last_cigarette = models.ForeignKey(Cigarette, blank=True, null=True) # Automatically Updated using signals

    # Manager
    objects = UserManager()

    # REQUIRED_FIELDS = settings.USER_REQUIRED_FIELDS

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        # app_label = 'users'

    def __unicode__(self):
        return self.username

    def save(self, *args, **kwargs):
        """ ensure instance has usable password when created """
        if not self.pk and self.has_usable_password() is False:
            self.set_password(self.password)

        super(QuitBitUser, self).save(*args, **kwargs)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])



# Change this if you change REQUIRED_FIELDS
#
# def create_superuser(self, email, date_of_birth, password):
# u = self.create_user(email, date_of_birth, password)
# u.superuser = True
# u.save()
# return u

# Entity Smoking_habit


# Update the SmokingHabit.last_cigarette whenever a new Cigarette is created
#  use django.db.models.get_model if I put this code in signals.py and import it here in models
def update_last_cigarette(sender, instance, created, **kwargs):
    if created:
        # instance = kwargs.get('instance')
        user = instance.user
        user.last_cigarette = instance
        user.save()

post_save.connect(update_last_cigarette, sender=Cigarette)