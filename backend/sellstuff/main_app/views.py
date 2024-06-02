from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializer import db_api_test_serializer
from rest_framework.response import Response
from .models import db_test, db_api_test






class db_api_view(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "description":output.description
            } for output in db_api_test.objects.all()
        ]
        return Response(output)
    def post(self, request):
        serializer = db_api_test_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



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