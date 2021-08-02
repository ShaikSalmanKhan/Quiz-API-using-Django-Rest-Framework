from App.models     import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    option_one = serializers.CharField(default=True,read_only=True)
    option_two = serializers.CharField(default=False,read_only=True)
    class Meta:
        model        =  Question
        fields       =  ('question','correct_answer','option_one','option_two','active',)  
        

    