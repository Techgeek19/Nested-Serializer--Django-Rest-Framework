from django.shortcuts import render

#Generic 
from rest_framework import generics, mixins
from rest_framework.decorators import action

#Models
from main.models import *

#Serializers
from main.serializers import QuestionSerializer

#Django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters

#Upload
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser

# class QuestionFilter(FilterSet):
#     tags = filters.CharFilter(method="filter_by_tags")

#     class Meta:
#         model = Question
#         fields =["tags"]

#     def filter_by_tags(self, queryset, name, value):
#         tag_names = value.strip().split(",")
#         tags = Tag.objects.filter(name__in=tag_names)
#         return queryset.filter(tags__in=tags).distinct()

class QuestionListView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin ):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    parser_class = (FileUploadParser,FormParser, JSONParser, MultiPartParser)
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = QuestionFilter

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id) 

    # @action(detail=True, methods=["GET"])
    # def tags(self, request, id):
    #     question = self.get_object()
    #     tags = Tag.objects.filter(question=question)
    #     serializer = TagSerializer(tags, many=True)
    #     return Response(serializer.data, status=200)  

    # @action(detail=True, methods=["POST"])
    # def tag(self, request, id=None):
    #     question = self.get_object()
    #     data = request.data
    #     data["question"] = question.id
    #     serializer = TagSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.erros, status=400)

    # @action(detail=True, methods=["PUT"])
    # def image(self, request, id=None):
    #     question = self.get_object()
    #     image= question.image
    #     serializer = QuestionSerializer(image, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.erros, status=400)
    



