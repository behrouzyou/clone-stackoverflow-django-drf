from rest_framework import serializers


class QuestionTitleViewCountField(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.title} - {value.views_count}"
