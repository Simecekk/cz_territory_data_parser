from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from municipality_data_app.models import Orp, Obec

import os
import csv
from datetime import datetime

class Command(BaseCommand):
    """
    Vezme soubor data_csv/UI_ORP.csv a udělá z něj Orp object
    """
    help = 'Create Orp object base on csv in data_csv'

    def handle(self, *args, **options):

        # Otebře CSV soubor
        with open(settings.BASE_DIR + "\\data_csv\\" + 'UI_ORP.csv', encoding="1250") as csv_file:
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
                   spravni_obec_kod = Obec.objects.get(kod=row[2])
                   vusc_kod = row[3]
                   plati_od = datetime.strptime(row[4].replace('.', '/'), '%d/%m/%Y %H:%M:%S')

                   if row[5] != "":
                       plati_do = datetime.strptime(row[4].replace('.', '/'), '%d/%m/%Y %H:%M:%S')
                   else:
                       plati_do = None

                   datum_vzniku = datetime.strptime(row[6].replace('.', '/'), '%d/%m/%Y %H:%M:%S')

                   Orp.objects.create(kod=kod,
                                       nazev=nazev,
                                       spravni_obec_kod=spravni_obec_kod,
                                       vusc_kod=vusc_kod,
                                       plati_od=plati_od,
                                       plati_do=plati_do,
                                       datum_vzniku=datum_vzniku)

            print('DATA COLLECTED')

