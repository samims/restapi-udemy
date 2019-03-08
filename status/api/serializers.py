from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from accounts.api.serializers import UserPublicSerializer
from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    # user_id = serializers.PrimaryKeyRelatedField(
    #     source='user', read_only=True)
    # user_id = serializers.HyperlinkedRelatedField(
    #     source='user', lookup_field='username', view_name='api-user:detail', read_only=True)

    # user = serializers.SlugRelatedField(read_only=True, slug_field='email'
    # )

    class Meta:
        model = Status
        fields = [
            'uri',
            'user_id',
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ('user',)

    def get_uri(self, obj):
        request = self.context['request']
        return api_reverse('api-status:detail', kwargs={'id': obj.id}, request=request)

    def validate(self, attrs):
        content, image = attrs.get("content"), attrs.get('image')
        if not content and not image:
            raise serializers.ValidationError("Content or image is required")
        return attrs


class StatusInlineUserSerializer(StatusSerializer):
    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'content',
            'image'
        ]
