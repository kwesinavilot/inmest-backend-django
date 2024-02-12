from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.view import View

def json_response(request):
    return JsonResponse({"name": "Kwesi Navilot"})

def greet(request):
    return HttpResponse("<h1>Hello Kwesi Wealth</h1>")

def user_profile(request):
    return JsonResponse({
        "firstName": "Kwesi",
        "lastName": "Wealth",
        "age": 32,
        "gender": 'M',
        "nationality": "Ghanaian",
        "location": "Takoradi/Accra",
        "occupation": "CEO - Naviware",
        "netWorth": "$8.6b",
    })

def filter_queries(request, userID):
    books = [
        {
            "userID": 100,
            "title": "The Journey To Mars",
            "description": "Herein lies the adventures of Kwesi Navilot after he was morooned on Mars.",
            "status": "published",
            "submitted_by": "A.K.A"
        },
        {
            "userID": 101,
            "title": "Building Africa's First 'Centicorn'",
            "description": "This is the memoir of Kwesi Navilot as he built African's first $1tn company.",
            "status": "published",
            "submitted_by": "Olivia Samey"
        },
        {
            "userID": 103,
            "title": "Hitting The Million Mark",
            "description": "This book contains second- and third-party accounts of how Kwesi Navilot led his startup to a million users",
            "status": "published",
            "submitted_by": "Steven De Koffi"
        }
    ]

    for book in books:
        print(book)
        if(userID == book['userID']):
            return JsonResponse(book)
        else:
            return HttpResponse("<h3>Search Response:</h3><p>That which you seek is not found</p>")


# CLASS-BASED VIEWS
class QueryView(View):
    books = [
            {
                "userID": 100,
                "title": "The Journey To Mars",
                "description": "Herein lies the adventures of Kwesi Navilot after he was morooned on Mars.",
                "status": "published",
                "submitted_by": "A.K.A"
            },
            {
                "userID": 101,
                "title": "Building Africa's First 'Centicorn'",
                "description": "This is the memoir of Kwesi Navilot as he built African's first $1tn company.",
                "status": "published",
                "submitted_by": "Olivia Samey"
            },
            {
                "userID": 103,
                "title": "Hitting The Million Mark",
                "description": "This book contains second- and third-party accounts of how Kwesi Navilot led his startup to a million users",
                "status": "published",
                "submitted_by": "Steven De Koffi"
            }
    ]

    def get(self, request):
        return JsonResponse({"response": self.books[0]})
    
    # def post(self, request):