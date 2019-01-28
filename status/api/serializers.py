from rest_framework import serializers

from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    # field level validation
    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way to long")
    #     return value

    # whole serializer validation
    def validate(self, attrs):
        print(attrs)
        content, image = attrs.get("content"), attrs.get('image')
        if not content and not image:
            raise serializers.ValidationError("Content or image is required")
        return attrs


'''
class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()

'''
