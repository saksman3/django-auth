# Django Boilerplate
###### - It can be quite frustrating if you want to start building your app and have to start of by doing the setup of your environment, I have built this django boilerplate in order to speed up the process and quickly start off with doing the important parts of development.
###### - This boilerplate is designed to allow the flexibility between working in production and also in development.
### Setup
##### We will need to setup a virtual environment Run
##### Windows 
###### ``` python -m pip install --user virtualenv ```
###### ```.\env\Scripts\activate ```
##### Linux
###### ``` python3 -m venv env```
###### ``` source env/bin/activate ```


###### Run ```pip install -r requirements.txt``` to install required python packages.
###### - Change the environment inside manage.py in the line `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings.dev')` 
###### A command for changing the project name to your preferred name also exists
###### Run ``` python manage.py rename $project_name``` replacing $project_name with your project name
###### Configurations can be done inside the .env file here you can define variables that should be kept secret 
###### - Secret keys, Passwords or DB access details.

