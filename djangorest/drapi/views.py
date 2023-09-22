from django.shortcuts import render
from .models import demo
from .serializers import demoSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.

#QuerySet
def demo_info(request):
    #complex data
    complex_data=demo.objects.all()

    #python dict / Native python datatype
    serializer=demoSerializer(complex_data, many=True)

    # render Json / Json data
    json_data = JSONRenderer().render(serializer.data)

    #Json sent to user
    return HttpResponse(json_data, content_type='application/json')


#Model Instance 
def demo_ins(request,pk):
    #complex data
    complex_data=demo.objects.get(id=pk)

    #python dict / Native python datatype
    serializer=demoSerializer(complex_data)

    # render Json / Json data
    json_data = JSONRenderer().render(serializer.data)

    #Json sent to user
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def demo_create(request):
    if request.method == 'POST':
        json_data=request.body
        #Json to stream convert
        stream=io.BytesIO(json_data)
        #stream to python
        python_data=JSONParser().parse(stream)
        #python to complex
        serializer=demoSerializer(data=python_data)
        if serializer.is_valid:
            serializer.save()
            res ={'msg': 'Successfully insert data'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application.json')
        json_data=JSONRenderer().render(serializer.errors)   
        return HttpResponse(json_data,content_type='application.json')
