from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from municipality_data_app.models import Pou, Orp, Obec

import os
import csv
from datetime import datetime

class Command(BaseCommand):
    """
    Vezme soubor data_csv/UI_OBEC.csv a udělá z něj Obec object
    """
    help = 'Create Obec object base on csv in data_csv'

    def handle(self, *args, **options):

        # Otebře CSV soubor
        with open(settings.BASE_DIR + "\\data_csv\\" + 'UI_OBEC.csv', encoding="1250") as csv_file:
            # Přečtení csv dat
            csv_reader = csv.reader(csv_file, delimiter=';')

            # Počítadlo řádku, pro určení prvního řádku.
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                   kod = row[0]
                   nazev = row[1]
                   status_kod = row[2]
                   pou_kod = row[3]
                   okres_kod = row[4]
                   cleneni_sm_rozsah_kod = [5]
                   cleneni_sm_typ_kod = [6]
                   
                   plati_od = datetime.strptime(row[7].replace('.', '/'), '%d/%m/%Y %H:%M:%S')

                   # Oběření jestli je datum uvedený, Pokud není vrátí None
                   if row[8] != "":
                       plati_do = datetime.strptime(row[8].replace('.', '/'), '%d/%m/%Y %H:%M:%S')
                   else:
                       plati_do = None
                   
                   if row[9] != "":
                       datum_vzniku = datetime.strptime(row[9].replace('.', '/'), '%d/%m/%Y %H:%M:%S')
                   else:
                       datum_vzniku = None

                   Obec.objects.create(kod=kod,
                                       nazev=nazev,
                                       status_kod=status_kod,
                                       pou_kod=pou_kod,
                                       okres_kod=okres_kod,
                                       cleneni_sm_rozsah_kod=cleneni_sm_rozsah_kod,
                                       cleneni_sm_typ_kod=cleneni_sm_typ_kod,
                                       plati_od=plati_od,
                                       plati_do=plati_do,
                                       datum_vzniku=datum_vzniku)

            print('DATA COLLECTED')

