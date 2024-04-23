from xml.dom import ValidationErr 
from rest_framework import serializers

from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from modules.models import Asset, Transaction, User
from modules.utils import Util

from rest_framework.permissions import BasePermission
from . import views


class UserRegistrationSerializer(serializers.ModelSerializer):
    '''writing this because we need to confirm password from registration 
       and also to hide the password while writing
    '''
    Re_type_Your_password=serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['Email', 'First_Name', 'Last_Name', 'password', 'Re_type_Your_password', 'Terms_Privacy_Policy']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        Re_type_Your_password = attrs.get('Re_type_Your_password')
        if password != Re_type_Your_password:
            raise serializers.ValidationError("password and Re type Your password does not match")
        return attrs
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    Email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['Email', 'password'] 

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Email', 'First_Name', 'Last_Name']

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    Re_type_Your_password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)

    class Meta:
        fields = ['password', 'Re_type_Your_password']

    def validate(self, attrs):
        password = attrs.get('password')
        Re_type_Your_password = attrs.get('Re_type_Your_password')
        user = self.context.get('user')
        if password != Re_type_Your_password:
            raise serializers.ValidationError("password and Re type Your password does not match")
        user.set_password(password)
        user.save()
        return attrs
    
class SendPasswordResetEmailSerializer(serializers.Serializer):
    Email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['Email']

    def validate(self, attrs):
        Email = attrs.get('Email')
        if User.objects.filter(Email=Email).exists():
            user = User.objects.get(Email = Email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
            print('Password Reset Link', link)
            #send Email
            body = 'Click Following Link to Reset Your Password'+link
            data = {
                'subject':'Reset Your Password',
                'body':body,
                'to_email':user.Email       
            }
            Util.send_email(data)
            return attrs
        else:
            raise ValidationErr('You are not a Registered User')    

class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    Re_type_Your_password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)

    class Meta:
        fields = ['password', 'Re_type_Your_password']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            Re_type_Your_password = attrs.get('Re_type_Your_password')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != Re_type_Your_password:
                raise serializers.ValidationError("password and Re type Your password does not match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError('Token is Not Valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('Token is Not Valid or Expired')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Email', 'First_Name', 'Last_Name', 'Terms_Privacy_Policy']
        

#Add Asset
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        