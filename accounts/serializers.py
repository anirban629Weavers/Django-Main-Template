from rest_framework import serializers
from core.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        pop_dict = [
            'password',
            'id',
            'last_login',
            'is_admin',
            'is_active',
            'is_superuser',
            'is_staff',
            'user_permissions',
            'groups',
        ]

        for values in pop_dict:
            representation.pop(values, None)

        return representation


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = "__all__"
        exclude = (
            "groups",
            "user_permissions",
            "is_admin",
            "is_active",
            "is_staff",
            "last_login",
            "is_superuser"
            )

    def save(self):
        user = User(
            email=self.validated_data["email"],
            name=self.validated_data['name'],
            phone=self.validated_data['phone'],
            address=self.validated_data['address'],
            image=self.validated_data['image'],
        )
        password = self.validated_data["password"]

        user.set_password(password)
        user.save()

        print(user.image)

        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return user, tokens

    def to_representation(self, instance):
        # Exclude the password field from the serialized representation
        representation = super().to_representation(instance)
        representation.pop('password', None)
        return representation


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = get_user_model().objects.filter(email=email).first()

            if user and user.check_password(password):
                return user

            raise serializers.ValidationError(
                "Invalid email or password. Please try again."
                )

        raise serializers.ValidationError(
            "Email and password are required fields."
            )
