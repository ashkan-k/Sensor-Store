from rest_framework.viewsets import ModelViewSet
from Setting.api.serializers import SettingSerializer
from Setting.models import Setting

class SettingVS(ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    http_method_names = ['get', 'head']
    search_fields = ['key', 'value']
    lookup_field = 'key'
