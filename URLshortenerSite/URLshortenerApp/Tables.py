#tables.py
import django_tables2 as tables
from .models import Usr_Urls

class UsrTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk')
    class Meta:
        model = Usr_Urls
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        #exclude = ['httpurl']
        
