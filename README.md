djangoTango
===========

You can use this section for a quick reference if you need to remind yourself about particular actions.

**********************************************Chapter 3***********************************************************


1) Creating a new Django Project

To create the project run, django-admin.py startproject <name>, where <name> is the name of the project you wish to create.

2) Creating a new Django application

To create a new application run, $ python manage.py startapp <appname>, where <appname> is the name of the application you wish to create.
Tell your Django project about the new application by adding it to the INSTALLED_APPS tuple in your project’s settings.py file.
In your project urls.py file, add a mapping to the application.
In your application’s directory, create a urls.py file to direct incoming URL strings to views.
In your application’s view.py, create the required views ensuring that they return a HttpResponse object.


**********************************************Chapter 4***********************************************************

With the chapter complete, you should now know how to setup and create templates, use templates within your views,
setup and use Django to send static media files, include images within your templates and setup Django’s static
media server to allow for file uploads. We’ve actually covered quite a lot!

Creating a template and integrating it within a Django view is a key concept for you to understand.
It takes several steps, but becomes second nature to you after a few attempts.

1)    First, create the template you wish to use and save it within the templates directory you specified in your
      project’s settings.py file. You may wish to use Django template variables (e.g. {{ variable_name }}) within your template.
      You’ll be able to replace these with whatever you like within the corresponding view.
2)    Find or create a new view within an application’s views.py file.
3)    Add your view-specific logic (if you have any) to the view. For example, this may involve extracting data 
      from a database.
4)    Within the view, construct a dictionary object which you can pass to the template engine as part of the template’s context.
5)    Make use of the RequestContext() class and render_to_response() helper function to generate the rendered response.
      Ensure you reference the correct template file for the first render_to_response() parameter!
6)    If you haven’t already done so, map the view to a URL by modifying your project’s urls.py file - and the
      application-specific urls.py file if you have one.

The steps involved for getting a static media file onto one of your pages is another important process you should be familiar with.
Check out the steps below on how to do this.

1)    Take the static media file you wish to use and place it within your project’s static directory. This is
      the directory you specify in your project’s STATICFILES_DIRS tuple within settings.py.
2)    Add a reference to the static media file to a template. For example, an image would be inserted into
      an HTML page through the use of the <img /> tag. Remember to use the {% load static %} and {% static "filename" %} commands
      within the template to make your life easier!
3)    Load the view that utilises the template you modified in your browser. Your static media should appear.


**********************************************Chapter 5 Models and Databases***********************************************************


1) Setting up your Database

With a new Django project, you should first tell Django about the database you intend to use (i.e. configure DATABASES in settings.py). 

Without doing so, Django won’t have anywhere to store your data. You can also enable the admin interface to make your life a little bit easier - and remember, you can always disable it later if you want to.

2) Adding a Model

The workflow for adding models can be broken down into five steps.

    a) First, create your new model(s) in your Django application’s models.py file.
    b) With the model created, reconfigure the admin interface to include your new model(s), if you are using it.
    c) You should then synchronise or resynchronise your database with the $ python manage.py syncdb command.
       This will create the necessary infrastructure within the database for your new model(s).
    d) Create/Edit and then run your population script for your new model(s).

You should also remember about the nuances of the syncdb command (Use SOUTH).
Note that the command can be used only for adding new models to your database - if you 
wish to amend an existing model, you must recreate the database.

5.10.1. Hints

If you require some help or inspiration to get these exercises done, these hints will hopefully help you out.

    To customise the admin interface, you will need to edit rango/admin.py and create a PageAdmin class that inherits from admin.ModelAdmin.
    Within your new PageAdmin class, add list_display = ('title', 'category', 'url').
    Finally, register the PageAdmin class with Django’s admin interface. You should modify the line admin.site.register(Page). Change it to admin.site.register(Page, PageAdmin) in Rango’s admin.py file.