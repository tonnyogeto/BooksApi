from django.shortcuts import render
import json
from .models import Book
from django.http import JsonResponse,HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here
@csrf_exempt
def create_book(req:HttpRequest):
    #get the json body
    json_body= req.body

    #deserialize the json request body into a dictionary
    book=json.loads(json_body)

    #save the book object in the DB 
    saved_book = Book.objects.create(
            title=book["title"], 
            number_of_pages=book['number_of_pages'], 
            price= book['price'],
            date_of_publication=book['date_of_publication']
        )

    #return a json response 
    return JsonResponse({'success':'true', 'message':'You have successfully created a book'})

@csrf_exempt
def get_books(request):
    #fetched all books from DB
    data = Book.objects.all().values()

    #serialized to a json response
    json_data = json.dumps(list(data),cls=DjangoJSONEncoder)
    
    return JsonResponse(json_data, safe=False)
