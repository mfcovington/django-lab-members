from django.db import models

class Position(models.Model):

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    title = models.CharField(u'title',
        blank=False,
        default='',
        help_text=u'Please enter a title for this position',
        max_length=64,
        unique=True,
    )

    def __str__(self):
        pass


class Scientist(models.Model):

    class Meta:
        verbose_name = "Scientist"
        verbose_name_plural = "Scientists"

    full_name = models.CharField(u'full name',
        blank=False,
        default='',
        help_text=u'Please enter a full name for this scientist',
        max_length=64,
        unique=True,
    )

    slug = models.SlugField(u'slug',
        blank=False,
        default='',
        help_text=u'Please enter a unique slug for this scientist',
        max_length=64,
    )

    title = models.ForeignKey('lab_members.Position',
        blank=True,
        default=None,
        help_text=u'Please specify a title for this scientist',
        null=True,
    )

    def __str__(self):
        pass
