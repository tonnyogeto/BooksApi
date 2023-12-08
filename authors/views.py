from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Author
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

@csrf_exempt
def author_view(request):

    verb =request.method

    if verb=='POST':
        #get the json body
        json_body= request.body

        #deserialize the json request body into a python dict
        author=json.loads(json_body)

        #save the book object in the DB 
        saved_author =Author.objects.create(
                first_name=author["x"],
                second_name=author["y"]
            )

        #return a json response 
        return JsonResponse({'success':'true', 'message':'You have successfully created an author'})
    
    elif verb=='GET':
        #fetched all books from DB
        data = Author.objects.all().values()

        #serialize to a json response
        json_data = json.dumps(list(data),cls=DjangoJSONEncoder)

        return JsonResponse(json_data, safe=False)

    else:
        return JsonResponse({'message':f'HTTP verb {verb} is not supported'})
    
@csrf_exempt
def author_view_with_id(request,id):
    verb =request.method
    if verb == 'GET':
        #get the author with the given id from db
        author=Author.objects.get(pk=id)

        #serialize into json
        json_data=serializers.serialize('json', [ author, ])

        struct = json.loads(json_data)
        data = json.dumps(struct[0])

        #return json response
        return JsonResponse(data, safe=False)
    
    else:
        return JsonResponse({'message':f'HTTP verb {verb} is not supported'})


