# -*- coding: utf-8 -*-
import datetime

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def getCopyrightYears():
    """
    Gets the Copyrigth Years. like "2009 - 2012".
    If no COPY_START_YEAR is given in the settings, it returns thisYear.
    else COPY_START_YEAR - thisYear

    Example :

        {{ request|getCopyrightYears }}
    """
    thisYear = datetime.datetime.now().year
    if hasattr(settings, "COPY_START_YEAR"):
        copyYearStart = getattr(settings, "COPY_START_YEAR", )
        if copyYearStart is not None and copyYearStart != thisYear:
            return "%s - %s" % (str(settings.COPY_START_YEAR), str(thisYear))
    return str(thisYear)
