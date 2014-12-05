# django-copyright

[django-copyright](https://github.com/arteria/django-copyrigh) keeps your site's copyright notice up-to-date. Forever and ever.

## Installation

Install copyright from the PyPI using:

    pip install django-copyright

Add `copyright` to your `INSTALLED_APPS`

    INSTALLED_APPS = (
    
        'copyright',
    )

set a `COPY_START_YEAR` in the django settings (this is an ingeter)

    COPY_START_YEAR = 2009
    
to span a range.


## Usage

Load copyrighttags in the template with `{% load copyrighttags %}`, afterwards place `{% getCopyrightYears %}` in the template, this will render a string like "2009 - 2012" or "2012" in case ``COPY_START_YEAR`` is not definied in your project settings.
