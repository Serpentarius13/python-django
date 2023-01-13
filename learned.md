# Overall python


## Code

### f"{a}" *Template literals in Python*
### if __name__ == _main__: main()  *Running code as a script and not as module*


## Commands

### python -m pip install PACKAGE_NAME *Installs package*
### python -m venv ENV_NAME   *Virtual Environment for packages*  **To get into the env** ENV_NAME\Scripts\activate.bat **To get out** deactivate
#### *Conda venv* conda create ENV_NAME (or in UI) **-->** conda activate ENV_NAME **||** conda list / conda deactivate etc




# Django

## Urls:

### "<int:query>" *Take up only an integer in param query. Otherwise not found*
### include("apppath.urls") *Include app's router in global app urls*
### name="urlname" reverse("urlname", args=[]) *Retrieve exact baseURL path by pathname*


## Templates:

### from django.template.loader render_to_string('template.html') *Create html template string from a template file* 
#### appfolder/templates/appfolder(any name) *Path for folders*  **settings.py in mainfolder with Templates, BaseDIR or Connected apps via "appname" for it to work properly!**
#### from django.shortcuts // return render(request, "template.html")




## Commands:

### django-admin startserver APP_NAME *Starts project in django*
### python manage.py runserver *Runs server*
### python manage.py startapp APP_NAME *Creates subapp in django project foler*

