from django.conf import settings
from django.db import models
from datetime import datetime
from filer.fields.image import FilerImageField

if 'cms_lab_members' in settings.INSTALLED_APPS:
    from cms.models.fields import PlaceholderField

def tuplify(x): return (x,x)
current_year = datetime.now().year
YEARS_A = map(tuplify, reversed(range(1960, current_year + 1)))
YEARS_B = map(tuplify, reversed(range(1960, current_year + 1)))


class Position(models.Model):

    class Meta:
        ordering = ['title']
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


class ScientistBase(models.Model):

    class Meta:
        abstract = True
        ordering = ['full_name']
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

    email = models.EmailField(u'email address',
        null=True,
        help_text=u'Please enter email address',
    )

    current = models.BooleanField(u'current lab member',
        default=True,
        help_text=u'Please specify whether scientist is a current lab member',
    )

    alumni_redirect_url = models.URLField(u'alumni redirect URL',
        null=True,
        blank=True,
        help_text=u"If former lab member, please enter the scientist's new URL"
    )

    photo = FilerImageField(
        null=True,
        blank=True,
        help_text=u'Please upload an photo of this scientist',
    )

    visible = models.BooleanField('visible',
        default=True,
        help_text='Display this scientist?',
    )

    def __str__(self):
        return self.full_name


class Scientist(ScientistBase):

    if 'cms_lab_members' in settings.INSTALLED_APPS:
        personal_interests = PlaceholderField(u'personal interests',
            related_name='personal_interests',
        )

        research_interests = PlaceholderField(u'research interests',
            related_name='research_interests',
        )

        sidebar = PlaceholderField(u'scientist sidebar',
            related_name='scientist sidebar'
        )

    else:
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


class Institution(models.Model):

    class Meta:
        ordering = ['name']
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
        ordering = ['title']
        verbose_name = "Degree"
        verbose_name_plural = "Degrees"

    title = models.CharField(u'degree title',
        help_text=u'Please enter a degree type',
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return self.title


class Field(models.Model):

    class Meta:
        ordering = ['label']
        verbose_name = "Field"
        verbose_name_plural = "Fields"

    label = models.CharField(u'field of study',
        help_text=u'Please enter a field of study',
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return self.label


class Advisor(models.Model):

    class Meta:
        ordering = ['full_name']
        verbose_name = "Advisor"
        verbose_name_plural = "Advisors"

    full_name = models.CharField(u'advisor name',
        help_text=u"Please enter advisor's name",
        max_length=64,
        unique=True,
    )

    url = models.URLField(u'advisor website',
        null=True,
        blank=True,
        help_text=u"Please enter advisor's website",
    )

    def __str__(self):
        return self.full_name


class Records(models.Model):

    class Meta:
        abstract = True
        ordering = ['-year_start', '-year_end']

    institution = models.ForeignKey('lab_members.Institution',
        help_text=u'Please enter the institution attended',
    )

    field = models.ForeignKey(u'lab_members.Field',
        null=True,
        blank=True,
        help_text=u'Please specify the field studied',
    )

    scientist = models.ForeignKey('lab_members.Scientist')

    advisor = models.ForeignKey('lab_members.Advisor',
        null=True,
        blank=True,
        help_text=u"Please specify advisor's name",
    )


class Education(Records):

    class Meta:
        verbose_name = "Education record"
        verbose_name_plural = "Education records"

    degree = models.ForeignKey(u'lab_members.Degree',
        null=True,
        blank=True,
        help_text=u'Please specify the degree granted',
    )

    year_start = models.IntegerField(u'year started',
        null=True,
        blank=True,
        choices=YEARS_A,
        help_text=u'Please specify the year started',
        max_length=4,
    )

    year_end = models.IntegerField(u'year degree granted (or study ended)',
        null=True,
        blank=True,
        choices=YEARS_B,
        help_text=u'Please specify the year finished',
        max_length=4,
    )

    def __str__(self):
        if self.year_start and self.year_end:
            years = " - ".join([str(self.year_start), str(self.year_end)])
        elif self.year_start:
            years = " - ".join([str(self.year_start), "Present"])
        elif self.year_end:
            years = str(self.year_end)
        else:
            years = "No dates given"

        return years


class Employment(Records):

    class Meta:
        verbose_name = "Employment record"
        verbose_name_plural = "Employment records"

    position = models.ForeignKey('lab_members.Position',
        help_text=u'Please enter a title for this position',
    )

    year_start = models.IntegerField(u'year started',
        null=True,
        choices=YEARS_A,
        help_text=u'Please specify the year started',
        max_length=4,
    )

    year_end = models.IntegerField(u'year ended',
        null=True,
        blank=True,
        choices=YEARS_B,
        help_text=u'Please specify the year finished',
        max_length=4,
    )

    def __str__(self):
        if self.year_start and self.year_end:
            years = " - ".join([str(self.year_start), str(self.year_end)])
        elif self.year_start:
            years = " - ".join([str(self.year_start), "Present"])
        elif self.year_end:
            years = "'Year started' is required"    # This should never happen
        else:
            years = "No dates given"

        return years
