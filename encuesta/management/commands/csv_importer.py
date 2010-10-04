from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_model
from csv_utf8 import *
import os

class Command(BaseCommand):

    help = "Whatever you want to print here"

    def handle(self, model_name, filename, **options):
        app, model = model_name.split('.')

        #validando si existe el fichero
        if not os.path.exists(filename):
            raise CommandError('No such file :P')
        Modelo = get_model(app, model)
        obj = Modelo()
        run(obj, filename)
        #try:
            #validando si existe la app
            
        #except:
            #raise CommandError('The app or model doesn\'t exist :(')
