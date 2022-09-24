import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.http import FileResponse, HttpResponse, JsonResponse

# Create your views here.


@csrf_exempt
def getworkshopList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select name,address,phone,profilePic from homeowner")
            row1 = cursor_1.fetchall()
        if row1 == None:
            json_data = {"message": "Wrong"}
            return HttpResponse(json_data, content_type="application/json")
        else:
            result = []
            keys = ('name', 'address', 'phone', 'profilePic')
            for row in row1:
                im = row[3]
                base64_string = im.decode('utf-8')
                y = list(row)
                y[3] = base64_string
                row = tuple(y)
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            # print(json_data)
            return HttpResponse(json_data, content_type="application/json")

    return HttpResponse("hello")


@csrf_exempt
def createWorkshop(request):
    if request.method == 'POST':
        WorkshopName = request.POST.get("WorkshopName", False)
        WorkshopDescription = request.POST.get("WorkshopDescription", False)
        WorkshopTime = request.POST.get("WorkshopTime", False)
        WorkshopPlace = request.POST.get("WorkshopPlace", False)
        InstructorName = request.POST.get("InstructorName", False)
        InstructorPhone = request.POST.get("InstructorPhone", False)
        Active_NotActive = "Active"

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO workshop(Name,Description,Time,Place,InstructorName,InstructorPhone, Active_NotActive) VALUES ('"+str(
                WorkshopName) + "' ,'"+str(WorkshopDescription) + "','"+str(WorkshopTime) + "','"+str(WorkshopPlace) + "','"+str(InstructorName) + "','"+str(InstructorPhone) + "','"+str(Active_NotActive) + "' )")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def removeWorkshop(request):
    return HttpResponse("hello")


@csrf_exempt
def editWorkshop(request):
    return HttpResponse("hello")
