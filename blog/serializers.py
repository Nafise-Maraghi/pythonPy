from rest_framework import serializers


class SearchArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    cover = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    content = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    created_at = serializers.DateTimeField()
