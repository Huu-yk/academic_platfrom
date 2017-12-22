from rest_framework import serializers
from spiders.models import ConferenceInfo

class ConferenceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceInfo
        fields = ('name', 'url', 'key_word', 'begin_time', 'end_time', 'host_address', 'description')