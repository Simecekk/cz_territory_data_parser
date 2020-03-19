from rest_framework.response import Response
from rest_framework import mixins, viewsets

from .models import Obec, Orp, Pou
from .serializers import ObecSerializer, OrpSerializer, PouSerializer

class ObecAPIView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    Slouží pro zobrazování Obcí

    url: /show/obec/?nazev=Hronov (volitelný parametr nazev, podle kterého lze filtrovat)
    """
    queryset = Obec.objects.all()
    serializer_class = ObecSerializer

    def list(self, request, *args, **kwargs):
        if 'nazev' in request.query_params:
            queryset = Obec.objects.filter(nazev__icontains=request.query_params['nazev'])
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class PouAPIView(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """
    Slouží pro zobrazování Správní obvody obcí s pověřeným obecním úřadem

    url: /show/pou/?nazev=Hronov (volitelný parametr nazev, podle kterého lze filtrovat)
    """
    queryset = Pou.objects.all()
    serializer_class = PouSerializer

    def list(self, request, *args, **kwargs):
        if 'nazev' in request.query_params:
            queryset = Pou.objects.filter(nazev__icontains=request.query_params['nazev'])
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OrpAPIView(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """
    Slouží pro zobrazování Správní obvody obcí s rozšířenou působností

    url: /show/orp/?nazev=Hronov (volitelný parametr nazev, podle kterého lze filtrovat)
    """
    queryset = Orp.objects.all()
    serializer_class = OrpSerializer

    def list(self, request, *args, **kwargs):
        if 'nazev' in request.query_params:
            queryset = Orp.objects.filter(nazev__icontains=request.query_params['nazev'])
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)