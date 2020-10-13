from rest_framework import serializers
from main.models import Question, Tag

class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Tag
        fields = ['id','name']

class QuestionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Question
        fields = ['id','text', 'image','tags']
        read_only_fields = ('question',)

    
    #Nested Serializer
    def create(self, validated_data):
        tag_validated_data = validated_data.pop('tags')
        question = Question.objects.create(**validated_data)
        tags_serializer = self.fields['tags']
        for each in tag_validated_data:
            each['question'] = question
        tags = tags_serializer.create(tag_validated_data)
        return question

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        instance.text = validated_data.get("text", instance.text)
        instance.save()
        keep_tags = []
        for tag in tags:
            if "id" in tag.keys():
                if Tag.objects.filter(id=tag["id"]).exists():
                    c = Tag.objects.get(id=tag["id"])
                    c.name = tag.get('name', c.name)
                    c.save()
                    keep_tags.append(c.id)
                else:
                    continue
            else:
                c = Tag.objects.create(**tag, question=instance)
                keep_tags.append(c.id)

        for tag in instance.tags.all():
            if tag.id not in keep_tags:
                tag.delete()

        return instance


