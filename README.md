# django-copyright

## Installation

Install copyright from the PyPI using:

    pip install django-copyright

Add `django-copyright` to your `INSTALLED_APPS`

    INSTALLED_APPS = (
    
        'django-copyright',
    )

set a `COPY_START_YEAR` in the django settings (this is an ingeter)

    COPY_START_YEAR = 2009


## Usage

Load copyrighttags in the template with `{% load copyrighttags %}`, afterwards place `{% getCopyrightYears %}` in the template, this will render a string like "2009 - 2012" or "2012" in case ``COPY_START_YEAR`` is not definied in your project settings.
