from django.db.models import get_model
from django.db.models import Field
import csv

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(unicode_csv_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def run(obj, filename):
    reader = unicode_csv_reader(open(filename))
    i = 0
    f = Field()
    for field in reader:
        size = len(field)-1
        for value in field:
            tipo = obj._meta.fields[i].get_internal_type()
            name = obj._meta.fields[i].name
            if tipo == 'ForeignKey':
                FK = obj._meta.fields[i].rel.to
                obj2 = FK.objects.get(pk=int(value))
                setattr(obj, name, obj2)
            else:
                setattr(obj, name, value)
            i=i+1 if i<size else 0
        obj.save()
    print 'Import successfull :)'
