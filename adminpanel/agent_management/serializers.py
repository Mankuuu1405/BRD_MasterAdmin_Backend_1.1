from rest_framework import serializers
from .models import *


class BaseAgentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"


class ChannelPartnerSerializer(BaseAgentSerializer):
    class Meta(BaseAgentSerializer.Meta):
        model = ChannelPartner


class VerificationAgencySerializer(BaseAgentSerializer):
    class Meta(BaseAgentSerializer.Meta):
        model = VerificationAgency


class CollectionAgentSerializer(BaseAgentSerializer):
    class Meta(BaseAgentSerializer.Meta):
        model = CollectionAgent
