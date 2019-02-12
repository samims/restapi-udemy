from rest_framework import serializers

from accounts.api.serializers import UserPublicSerializer
from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ('user',)

    def get_uri(self, obj):
        return "/api/status/{}".format(obj.id)

    # field level validation
    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way to long")
    #     return value

    # whole serializer validation
    def validate(self, attrs):
        content, image = attrs.get("content"), attrs.get('image')
        if not content and not image:
            raise serializers.ValidationError("Content or image is required")
        return attrs


'''
class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()

'''
