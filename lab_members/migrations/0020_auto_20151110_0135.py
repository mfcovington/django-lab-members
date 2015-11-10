# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0019_auto_20150522_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='advisor',
        ),
        migrations.RemoveField(
            model_name='employment',
            name='advisor',
        ),
        migrations.AddField(
            model_name='education',
            name='advisors',
            field=models.ManyToManyField(blank=True, help_text="Please select advisor's name (or multiple co-advisors).<br>", to='lab_members.Advisor', related_name='lab_members_education_records'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employment',
            name='advisors',
            field=models.ManyToManyField(blank=True, help_text="Please select advisor's name (or multiple co-advisors).<br>", to='lab_members.Advisor', related_name='lab_members_employment_records'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scientist',
            name='alumni_current_institution',
            field=models.ForeignKey(blank=True, help_text="If former lab member, please enter the scientist's new institution", on_delete=django.db.models.deletion.PROTECT, null=True, to='lab_members.Institution', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scientist',
            name='alumni_current_title',
            field=models.ForeignKey(blank=True, help_text="If former lab member, please enter the scientist's new title", related_name='alumni_scientist_set', null=True, to='lab_members.Position', on_delete=django.db.models.deletion.PROTECT, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.ForeignKey(blank=True, help_text='Please specify the degree granted', on_delete=django.db.models.deletion.PROTECT, null=True, to='lab_members.Degree'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='education',
            name='field',
            field=models.ForeignKey(blank=True, help_text='Please specify the field studied', on_delete=django.db.models.deletion.PROTECT, null=True, to='lab_members.Field'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='education',
            name='institution',
            field=models.ForeignKey(help_text='Please enter the institution attended', on_delete=django.db.models.deletion.PROTECT, to='lab_members.Institution'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='education',
            name='year_end',
            field=models.IntegerField(blank=True, choices=[(2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960)], help_text='Please specify the year finished', verbose_name='year degree granted (or study ended)', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='education',
            name='year_start',
            field=models.IntegerField(blank=True, choices=[(2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960)], help_text='Please specify the year started', verbose_name='year started', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employment',
            name='field',
            field=models.ForeignKey(blank=True, help_text='Please specify the field studied', on_delete=django.db.models.deletion.PROTECT, null=True, to='lab_members.Field'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employment',
            name='institution',
            field=models.ForeignKey(help_text='Please enter the institution attended', on_delete=django.db.models.deletion.PROTECT, to='lab_members.Institution'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employment',
            name='position',
            field=models.ForeignKey(help_text='Please enter a title for this position', on_delete=django.db.models.deletion.PROTECT, to='lab_members.Position'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employment',
            name='year_end',
            field=models.IntegerField(blank=True, choices=[(2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960)], help_text='Please specify the year finished', verbose_name='year ended', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employment',
            name='year_start',
            field=models.IntegerField(null=True, choices=[(2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960)], help_text='Please specify the year started', verbose_name='year started'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scientist',
            name='photo',
            field=filer.fields.image.FilerImageField(blank=True, help_text='Please upload an photo of this scientist', on_delete=django.db.models.deletion.PROTECT, null=True, to='filer.Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scientist',
            name='title',
            field=models.ForeignKey(blank=True, help_text='Please specify a title for this scientist', related_name='current_scientist_set', null=True, to='lab_members.Position', on_delete=django.db.models.deletion.PROTECT, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scientist',
            name='website_name',
            field=models.CharField(blank=True, max_length=64, help_text='Enter a name to display for the website. Default is the URL of the site.', verbose_name='website name'),
            preserve_default=True,
        ),
    ]
