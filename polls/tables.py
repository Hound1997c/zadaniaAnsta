import django_tables2 as tables
from .models import Osoba

class PersonTable(tables.Table):
    class Meta:
        model = Osoba
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )