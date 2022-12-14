import base64
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
            # cursor_1.execute("select ID, Name, Description, Time, Place, InstructorName,InstructorPhone,status from workshop where status='Enable'")
            cursor_1.execute(
                "select ID, Name, Description, Time, Place, InstructorName,InstructorPhone,status from workshop")
            row1 = cursor_1.fetchall()
        if row1 == None:
            json_data = {"message": "Wrong"}
            return HttpResponse(json_data, content_type="application/json")
        else:
            result = []
            keys = ('ID', 'Name', 'Description', 'Time', 'Place',
                    'InstructorName', 'InstructorPhone', 'status')
            for row in row1:
                # im = row[3]
                # base64_string = im.decode('utf-8')
                # y = list(row)
                # y[3] = base64_string
                # row = tuple(y)
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            # print(json_data)
            return HttpResponse(json_data, content_type="application/json")

    return HttpResponse("")


@csrf_exempt
def getworkshopListmy(request):
    if request.method == 'POST':
        id = request.POST.get("ID", False)
        type = request.POST.get("type", False)
        if type == "Admin":
            with connection.cursor() as cursor_1:
                # cursor_1.execute("select ID, Name, Description, Time, Place, InstructorName,InstructorPhone,status from workshop where status='Enable'")
                cursor_1.execute(
                    "select ID, Name, Description, Time, Place, InstructorName,InstructorPhone,status from workshop")
                row1 = cursor_1.fetchall()
            result = []
            keys = ('ID', 'Name', 'Description', 'Time', 'Place',
                    'InstructorName', 'InstructorPhone', 'status')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            # print(json_data)
            return HttpResponse(json_data, content_type="application/json")
        if type == "Student":
            with connection.cursor() as cursor_1:
                # cursor_1.execute("select ID, Name, Description, Time, Place, InstructorName,InstructorPhone,status from workshop where status='Enable'")
                cursor_1.execute(
                    "select ID, Name, Description, Time, Place, InstructorName,InstructorPhone from workshop")
                row1 = cursor_1.fetchall()
            with connection.cursor() as cursor_2:
                # cursor_1.execute("select ID, Name, Description, Time, Place, InstructorName,InstructorPhone,status from workshop where status='Enable'")
                cursor_2.execute(
                    "select WorkshopID from applicanttable where StudentID = '"+str(id) + "'")
                row2 = cursor_2.fetchall()
            result = []
            keys = ('ID', 'Name', 'Description', 'Time', 'Place',
                    'InstructorName', 'InstructorPhone', 'AppStatus')
            for r in row1:
                y = list(r)
                for r1 in row2:
                    if r1[0] == r[0]:
                        y.append('Yes')
                    # else:
                    #     y.append('Not')
                r = tuple(y)
                result.append(dict(zip(keys, r)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")
    return HttpResponse("")


@csrf_exempt
def createWorkshop(request):
    if request.method == 'POST':
        WorkshopName = request.POST.get("WorkshopName", False)
        WorkshopDescription = request.POST.get("WorkshopDescription", False)
        WorkshopTime = request.POST.get("WorkshopTime", False)
        WorkshopPlace = request.POST.get("WorkshopPlace", False)
        InstructorName = request.POST.get("InstructorName", False)
        InstructorPhone = request.POST.get("InstructorPhone", False)
        status = "Enable"

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO workshop(Name,Description,Time,Place,InstructorName,InstructorPhone, status) VALUES ('"+str(
                WorkshopName) + "' ,'"+str(WorkshopDescription) + "','"+str(WorkshopTime) + "','"+str(WorkshopPlace) + "','"+str(InstructorName) + "','"+str(InstructorPhone) + "','"+str(status) + "' )")
            connection.commit()
    return HttpResponse("")


@csrf_exempt
def removeWorkshop(request):
    if request.method == 'POST':
        WorkshopID = request.POST.get("WorkshopID", False)

        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "UPDATE workshop SET status='Disable' WHERE ID='"+str(WorkshopID) + "'")
            connection.commit()
    return HttpResponse("")


@csrf_exempt
def updateWorkshop(request):
    if request.method == 'POST':
        WorkshopID = request.POST.get("WorkshopID", False)
        WorkshopName = request.POST.get("WorkshopName", False)
        WorkshopDescription = request.POST.get("WorkshopDescription", False)
        WorkshopTime = request.POST.get("WorkshopTime", False)
        WorkshopPlace = request.POST.get("WorkshopPlace", False)
        InstructorName = request.POST.get("InstructorName", False)
        InstructorPhone = request.POST.get("InstructorPhone", False)
        status = request.POST.get("status", False)

        with connection.cursor() as cursor_1:
            cursor_1.execute("UPDATE workshop SET Name='" + str(WorkshopName) + "', Description='" + str(WorkshopDescription) + "', Time='" + str(WorkshopTime) + "', Place='" +
                             str(WorkshopPlace) + "', InstructorName='" + str(InstructorName) + "', InstructorPhone='" + str(InstructorPhone) + "', status='" + str(status) + "' where ID='" + str(WorkshopID) + "'")
            connection.commit()
    return HttpResponse("")


@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        Name = request.POST.get("Name", False)
        ID = request.POST.get("ID", False)
        Email = request.POST.get("Email", False)
        Phone = request.POST.get("Phone", False)
        Type = request.POST.get("Type", False)
        Password = request.POST.get("Password", False)

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO user(Name,ID,Email,Phone,Type,Password) VALUES ('"+str(
                Name) + "' ,'"+str(ID) + "','"+str(Email) + "','"+str(Phone) + "','"+str(Type) + "','"+str(Password) + "' )")
            connection.commit()

    return HttpResponse("")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        ID = request.POST.get("ID", False)
        password = request.POST.get("password", False)
        userType = request.POST.get("userType", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select ID, Password, Type from user where ID='"+str(ID) + "' and Type='"+str(userType) + "' and Password='"+str(password) + "'")
            row1 = cursor_1.fetchone()
            # print(row1)

        if row1 == None:
            data = {"message": "Wrong"}
        else:
            data = {"message": "Success"}
            # print(data)

        return JsonResponse(data)
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def getProfileInfo(request):
    if request.method == 'POST':
        id = request.POST.get("ID", False)
        type = request.POST.get("type", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select Name, ID, Email, Phone, Type from user where ID='"+str(id) + "'")
            row1 = cursor_1.fetchall()
        result = []
        keys = ('Name', 'ID', 'Email', 'Phone',
                'Type')
        for row in row1:
            result.append(dict(zip(keys, row)))
        json_data = json.dumps(result)
        # print(json_data)
        return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def applyForWorkshop(request):
    if request.method == 'POST':
        Workshop_ID = request.POST.get("Workshop_ID", False)
        Workshop_Name = request.POST.get("Workshop_Name", False)
        Student_ID = request.POST.get("Student_ID", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO applicanttable(WorkshopID,WorkshopName,StudentID) VALUES ('"+str(
                Workshop_ID) + "' ,'"+str(Workshop_Name) + "','"+str(Student_ID) + "')")
            connection.commit()
        return HttpResponse("")
