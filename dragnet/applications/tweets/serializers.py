from rest_framework import serializers

from .models import TweetModel, BestTweetModel, WorstTweetModel, DayScoreModel, TweetAnalizedModel


class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = TweetModel
        fields = ('__all__')


class BestTweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = BestTweetModel
        fields = ('__all__')


class WorstTweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorstTweetModel
        fields = ('__all__')


class DayScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = DayScoreModel
        fields = ('__all__')


class TweetAnalizedSerializer(serializers.ModelSerializer):

    class Meta:
        model = TweetAnalizedModel
        fields = ('__all__')