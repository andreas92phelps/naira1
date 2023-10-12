from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password, check_password


    # def validate

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
       #fields = "__all__"
        fields = ["first_name","last_name","phone" ,"email", 'password', 'username']# this code states that only these specific fields are required
#       fields = "__all__" #if this code is written, "all" fields will be required to be field on sign up

    def validate(self,data):

        if data['first_name'] == 'hick':
            raise ValueError('error')
        
        else:
            return data
        
    
    def create(self,data):
        pwd = data['password']

        encrypted_pwd = make_password(pwd, "ifh8032hIYFY9gg3gh23ifjJUBJ0hb2f8f308hjienwi9u3DYO023")

        user = User.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            # photo = data['photo'],
            phone =  data['phone'],
            username = data['username'],
            # age = data['age'],
            # salary = data['salary'],
            password = encrypted_pwd
        )
        user.password = encrypted_pwd

        print(user)

        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def loginuser(self,data):
        
        user = User.objects.filter(email = data['email']).first()#'.first()' is there to make sure that only the first reult from the filter is given

        if user is not None:
            original_pwd = data['password']
            encrypted_pwd = getattr(user, 'password')

            check = check_password(original_pwd, encrypted_pwd)
        
        # pwd = getattr(user, 'password')

            if check == True:
                user = {
                    "first_name": getattr(user, "first_name"),
                    "last_name": getattr(user, "last_name"),
                    "email": getattr(user, "email"),
                    "id": getattr(user, "id")
                }

                return user
            else:
                raise ValueError("invalid login details")
        
        else:
            raise ValueError("invalid login details")

        
    