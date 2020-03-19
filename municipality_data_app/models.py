from django.db import models
from django.utils.translation import gettext_lazy as _

from django.utils import timezone

class ObecQuerySet(models.QuerySet):

    def today(self):
        return self.filter(plati_od=timezone.now())


class Obec(models.Model):
    """
    Obce
    """
    kod = models.CharField(max_length=10, primary_key=True)
    nazev = models.CharField(max_length=255)
    status_kod = models.CharField(max_length=5)
    pou_kod = models.CharField(max_length=10)
    okres_kod = models.CharField(max_length=10)
    cleneni_sm_rozsah_kod = models.CharField(max_length=30, null=True, blank=True, verbose_name=_("david"))
    cleneni_sm_typ_kod = models.CharField(max_length=30, null=True, blank=True)
    plati_od = models.DateTimeField()
    plati_do = models.DateTimeField(null=True, blank=True)
    datum_vzniku = models.DateTimeField(null=True, blank=True)

    objects = ObecQuerySet.as_manager()

class Orp(models.Model):
    """
    Správní obvody obcí s rozšířenou působností
    """
    kod = models.CharField(max_length=4, primary_key=True)
    nazev = models.CharField(max_length=255)
    spravni_obec_kod = models.ForeignKey(Obec, on_delete=models.DO_NOTHING)
    vusc_kod = models.CharField(max_length=10)
    plati_od = models.DateTimeField()
    plati_do = models.DateTimeField(null=True, blank=True)
    datum_vzniku = models.DateTimeField()

class Pou(models.Model):
    """
    Model reprezentující Správní obvody obcí s pověřeným obecním úřadem
    https://www.cuzk.cz/Uvod/Produkty-a-sluzby/RUIAN/2-Poskytovani-udaju-RUIAN-ISUI-VDP/Ciselniky-ISUI/Vyssi-uzemni-prvky-a-uzemne-evidencni-jednotky.aspx
    """
    kod = models.CharField(max_length=4, primary_key=True)
    nazev = models.CharField(max_length=255)
    orp_kod = models.ForeignKey(Orp, on_delete=models.DO_NOTHING)
    spravni_obec_kod = models.ForeignKey(Obec, on_delete=models.DO_NOTHING)
    plati_od = models.DateTimeField()
    plati_do = models.DateTimeField(null=True, blank=True)
    datum_vzniku = models.DateTimeField()

