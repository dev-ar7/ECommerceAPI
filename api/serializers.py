from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Product, User


class ProductSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, allow_empty_file=False,
                                                     allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'color', 'category', 'price','image')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'password', 'phone',
                  'gender', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.times():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


