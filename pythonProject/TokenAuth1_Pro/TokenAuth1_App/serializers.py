from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =['id','username','email','password','gender','age']

    # convert user password into hashmap or encrypted format.
    def create(self, validated_data):
        password = validated_data.pop('password')

        user = CustomUser1.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    # this code is not work, it is work only for put method
    '''def change_password(self, instance, validated_data):
        password = validated_data.get('password')
        instance.set_password(password)
        instance.save()
        return instance
'''