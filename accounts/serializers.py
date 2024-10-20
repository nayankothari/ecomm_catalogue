from rest_framework import serializers
from .models import CustomUser


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff',
                  'is_superuser', 'app_user_type', "phone_number"]
        read_only_fields = ['id', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            app_user_type=validated_data["app_user_type"],
            phone_number=validated_data["phone_number"],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
