from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help="Renames a Django project"
    def add_arguments(self, parser):
        parser.add_argument('project_name',type=str, help='new project name')

    def handle(self, *args,**kwargs):
        project_name = kwargs['project_name']

        files_to_rename = ['demo.settings.base.py','demo.wsgi.py', 'manage.py']
        folders_to_rename = 'demo'
        for f in files_to_rename:
            with open(f,'r') as file:
                filedata = file.read()
            filedata.replace('demo',project_name)
            with open(f,'w') as file:
                file.write(filedata)
        os.rename(folders_to_rename,project_name)
        self.stdout.write(self.style.SUCCESS("Project renamed to %s" %project_name))