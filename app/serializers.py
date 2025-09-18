# from rest_framework import serializers
# from app.models import Student

# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     contact = serializers.CharField(max_length=15)

#     def create(self , validated_data):
#         """
#         Create and return a new `Snippet` instance, give the validated data .
#         """
#         return Student .objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Student` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.age = validated_data.get('age', instance.age)
#         instance.contact = validated_data.get('contact', instance.contact)
#         instance.save()
#         return instance 


from rest_framework import serializers
from app.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'contact']