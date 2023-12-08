from django.shortcuts import render
from django.views import View
from .models import Publisher
import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class FirstView(View):

    #create a single publisher
    def post(self, request):
        #get the json body
        json_body= request.body

        #deserialize the json request body into a python dict
        publisher=json.loads(json_body)

        #save the publisher object in the DB 
        Publisher.objects.create(
                name=publisher["name"]
            )

        #return a json response 
        return JsonResponse({'success':'true', 'message':'You have successfully created a publisher '})


    #get all publishers
    def get(self, request):
        #fetch all publishers from DB
        data = Publisher.objects.all().values()

        #serialize to a json response
        json_data = json.dumps(list(data),cls=DjangoJSONEncoder)

        return JsonResponse(json_data, safe=False)


class SecondView(View):
    #get a specific publisher@csrf_exempt
    def get(self,request,id):
        #get the author with the given id from db
        publisher=Publisher.objects.get(pk=id)

        #serialize into json
        json_data=serializers.serialize('json', [ publisher, ])

        struct = json.loads(json_data)
        data = json.dumps(struct[0])

        #return json response
        return JsonResponse(data, safe=False) 
    #todo later delete, update a specific publisher
    pass


