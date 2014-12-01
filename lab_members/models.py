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
        return self.title


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

    personal_interests = models.TextField(u'personal interests',
        blank=True,
        default='',
        help_text=u'Please write a personal interests blurb for this scientist'
    )

    research_interests = models.TextField(u'research interests',
        blank=True,
        default='',
        help_text=u'Please write a research interests blurb for this scientist'
    )

    def __str__(self):
        return self.full_name


class Institution(models.Model):

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"

    name = models.CharField(u'institution name',
        help_text=u'Please enter the institution attended',
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return self.name


class Degree(models.Model):

    class Meta:
        verbose_name = "Degree"
        verbose_name_plural = "Degrees"

    title = models.CharField(u'degree title',
        help_text=u'Please enter a degree type',
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return self.title
