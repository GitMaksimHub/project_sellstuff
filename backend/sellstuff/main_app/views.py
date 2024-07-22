from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializer import db_api_test_serializer
from rest_framework.response import Response
from .models import db_test, db_api_test
from rest_framework import generics, viewsets


class db_api_view_viewset(viewsets.ModelViewSet):
    queryset = db_api_test.objects.all()
    serializer_class = db_api_test_serializer
class db_api_view_destroy(generics.RetrieveDestroyAPIView):
    queryset = db_api_test.objects.all()
    serializer_class = db_api_test_serializer

# class db_api_view_list(generics.ListCreateAPIView):
#     queryset = db_api_test.objects.all()
#     serializer_class = db_api_test_serializer
#
# class test(generics.RetrieveAPIView):
#     queryset = db_api_test.objects.all()
#     serializer_class = db_api_test_serializer
# class db_api_view_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = db_api_test.objects.all()
#     serializer_class = db_api_test_serializer



def main(request):
    data = {
        "data":db_test.objects.all()
    }
    return render(request, 'main_app/main.html', data)


def test_path(request, slug_id):
    data = get_object_or_404(db_test, slug=slug_id)
    data_put = {
        "data":data
    }
    return render(request, 'main_app/test_path.html', data_put)