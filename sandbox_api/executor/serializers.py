from rest_framework import serializers

class CodeExecutionSerializer(serializers.Serializer):
    language = serializers.ChoiceField(choices=['python'])
    code = serializers.CharField()
    input = serializers.CharField(required=False, allow_blank=True)


