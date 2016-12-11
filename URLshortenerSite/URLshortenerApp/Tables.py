#tables.py
import django_tables2 as tables
from .models import Usr_Urls

class UsrTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input":{"onclick": "toggle(this)"}})
    #copying = tables.URLColumn(accessor='short_id', attrs = { "td__input":{"onclick": "copying(this)"}})
    #copying = tables.LinkColumn(accessor='short_id', attrs = { "td__input":{"onclick": '<button type="button" id="copying" value="copying" onclick="copying(this)">copy</button>"'}})
    #copying = tables.Column(accessor='short_id', attrs = { "td__input":{"onclick": <button type="button" id="copying" value="copying" onclick="copying(this)"></button>"}},  verbose_name = 'Copy')
    class Meta:
        model = Usr_Urls
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        #empty_text = "There is no Short URLs, Start building alternative routes"
        empty_text = "There is no Short URLs, Start building alternative routes "
        exclude = ['short_id']
        
