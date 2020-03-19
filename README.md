# cz_territory_data_parser
Zpracuje open data z cuzk.cz

https://www.cuzk.cz/Uvod/Produkty-a-sluzby/RUIAN/2-Poskytovani-udaju-RUIAN-ISUI-VDP/Ciselniky-ISUI/Vyssi-uzemni-prvky-a-uzemne-evidencni-jednotky.aspx

Data jsou uložená ve formátu CSV ve složce data_csv.

Pro nahrání dat do DB je potřeba spustit custom command a to v tomhle pořádí.

python manage.py obec_data_collect

python manage.py orp_data_collect

python manage.py pou_data_collect

Applikace obsahuje endpointy, na kterých je možné data zobrazovat.

Pro zobrazení všech dat z DB

/show/obec/

/show/pou/

/show/orp/

Pro zobrazení jednoho objektu.

/show/obec/<obec_pk>/
  
/show/pou/<pou_pk>/
  
/show/orp/<orp_pk>/

Pro filtrování na základě query parametru

/show/obec/?nazev=<foo_bar>

/show/pou/?nazev=<foo_bar>

/show/orp/?nazev=<foo_bar>
