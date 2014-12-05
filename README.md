# aR-Copyright #
---


##Setup##

install app using the Shell, type:

    pip install django-copyright

Add `ar_copyright` to your `INSTALLED_APPS`

    INSTALLED_APPS = (
    
        'ar_copyright',
    )

set a `COPY_START_YEAR` in the django settings (this is an ingeter)

    COPY_START_YEAR = 2009


##Usage##

import copyrighttags in the template with `{% load copyrighttags %}`

place `{{ request|getCopyrightYears }}` in the template, this will return something like "2009 - 2012"
