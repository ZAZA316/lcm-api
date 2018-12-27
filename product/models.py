from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _


# # class User(AbstractUser):
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     sex = models.CharField(verbose_name=_('Sex'), max_length=1, null=True, blank=True)
#     birthday = models.DateField(verbose_name=_('Birthday'), null=True, blank=True)
#     income = models.IntegerField(verbose_name=_('Income'), null=True, blank=True)
#     work_place = models.CharField(verbose_name=_('Work Place'), max_length=255, null=True, blank=True)
#     education = models.CharField(verbose_name=_('Education'), max_length=255, null=True, blank=True)
#     marriage = models.CharField(verbose_name=_('Marriage'), max_length=1, null=True, blank=True)
#     children = models.CharField(verbose_name=_('Children'), max_length=1, null=True, blank=True)
#     want_child = models.CharField(verbose_name=_('Want Child'), max_length=1, null=True, blank=True)
#     job = models.CharField(verbose_name=_('Job'), max_length=255, null=True, blank=True)
#     house = models.CharField(verbose_name=_('House'), max_length=1, null=True, blank=True)
#     vehicle = models.CharField(verbose_name=_('Vehicle'), max_length=1, null=True, blank=True)
#     height = models.IntegerField(verbose_name=_('Height'), null=True, blank=True)
#     weight = models.FloatField(verbose_name=_('Weight'), null=True, blank=True)
#     body_type = models.CharField(verbose_name=_('Body Type'), max_length=50, null=True, blank=True)
#     smoking = models.CharField(verbose_name=_('Smoking'), max_length=1, null=True, blank=True)
#     drinking = models.CharField(verbose_name=_('Drinking'), max_length=1, null=True, blank=True)
#     constellation = models.IntegerField(verbose_name=_('Constellation'), null=True, blank=True)
#     nation = models.IntegerField(verbose_name=_('Nation'), null=True, blank=True)
#     period_marriage = models.IntegerField(verbose_name=_('Period Marriage'), null=True, blank=True)
#
#     class Meta:
#         verbose_name = _('Profile')
#         verbose_name_plural = _('Profiles')
#
#
# class News(models.Model):
#     title = models.CharField(verbose_name=_('Title'), max_length=100)
#     content = models.TextField(verbose_name=_('Content'))
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = _('News')
#         verbose_name_plural = _('News')


class SeaCruiseGroup(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    text = models.TextField()
    sort = models.IntegerField()

    class Meta:
        verbose_name = _('SeaCruiseGroup')
        verbose_name_plural = _('SeaCruiseGroup')
        ordering = ['sort']
