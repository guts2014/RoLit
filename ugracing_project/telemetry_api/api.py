__author__ = 'Vlad Iulian Schnakovszki'
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Telemetry
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from exceptions import MyException

@csrf_exempt # Prevents Cross Site Request Forgery errors.
def getLatestValues(request):
    try:
        # Get the latest telemetry values.
        telemetryValues = Telemetry.objects.latest('id')

        # Build the response.
        response = dict(
            id = telemetryValues.id,
            report_datetime = telemetryValues.report_datetime,
			battery = telemetryValues.battery,
			brake = telemetryValues.brake,
			coolant_t = telemetryValues.coolant_t,
			fuel = telemetryValues.fuel,
			gear = telemetryValues.gear,
			map = telemetryValues.map,
			mat = telemetryValues.mat,
			o2 = telemetryValues.o2,
			rpm = telemetryValues.rpm,
			speed = telemetryValues.speed,
			throttle = telemetryValues.throttle,
			wheel_t_1 = telemetryValues.wheel_t_1,
			wheel_t_2 = telemetryValues.wheel_t_2,
			wheel_t_3 = telemetryValues.wheel_t_3,
			wheel_t_4 = telemetryValues.wheel_t_4,
			wheel_v_1 = telemetryValues.wheel_v_1,
			wheel_v_2 = telemetryValues.wheel_v_2,
			wheel_v_3 = telemetryValues.wheel_v_3,
			wheel_v_4 = telemetryValues.wheel_v_4,
            )

        # Return the response in a json format, with a HTTP status code of 200.
        Http_Response = HttpResponse(json.dumps(response, indent=4, cls=DjangoJSONEncoder), status=200, content_type= "application/json")
        Http_Response["Access-Control-Allow-Origin"] = "*"
        Http_Response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        Http_Response["Access-Control-Max-Age"] = "1000"
        Http_Response["Access-Control-Allow-Headers"] = "*"
        return Http_Response
    except MyException as ex:
        # Return the error message, along with a HTTP status of 500.
        return HttpResponse(ex.message, status=500)

@csrf_exempt # Prevents Cross Site Request Forgery errors.
def getValuesById(request):
    # Return a 400 Bad Request if id is not specified.
    if request.POST.get('ID') is None:
        return HttpResponse("You need to specify the id as a parameter named ID!", status=400)

    # Return a 404 Not Found if no object with the specified id exists.
    telemetryValues = Telemetry.objects.get(id=request.POST.get('ID'))
    if telemetryValues is None:
        return HttpResponse("Telemetry with id " + request.POST.get('ID') + " not found!", status=404)

    try:
        # Build the response.
        response = dict(
            id = telemetryValues.id,
            report_datetime = telemetryValues.report_datetime,
			battery = telemetryValues.battery,
			brake = telemetryValues.brake,
			coolant_t = telemetryValues.coolant_t,
			fuel = telemetryValues.fuel,
			gear = telemetryValues.gear,
			map = telemetryValues.map,
			mat = telemetryValues.mat,
			o2 = telemetryValues.o2,
			rpm = telemetryValues.rpm,
			speed = telemetryValues.speed,
			throttle = telemetryValues.throttle,
			wheel_t_1 = telemetryValues.wheel_t_1,
			wheel_t_2 = telemetryValues.wheel_t_2,
			wheel_t_3 = telemetryValues.wheel_t_3,
			wheel_t_4 = telemetryValues.wheel_t_4,
			wheel_v_1 = telemetryValues.wheel_v_1,
			wheel_v_2 = telemetryValues.wheel_v_2,
			wheel_v_3 = telemetryValues.wheel_v_3,
			wheel_v_4 = telemetryValues.wheel_v_4,
            )

        # Return the response in a json format, with a HTTP status code of 200.
        Http_Response = HttpResponse(json.dumps(response, indent=4, cls=DjangoJSONEncoder), status=200, content_type= "application/json")
        Http_Response["Access-Control-Allow-Origin"] = "*"
        Http_Response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        Http_Response["Access-Control-Max-Age"] = "1000"
        Http_Response["Access-Control-Allow-Headers"] = "*"
        return Http_Response
    except MyException as ex:
        # Return the error message, along with a HTTP status of 500.
        return HttpResponse(ex.message, status=500)

@csrf_exempt # Prevents Cross Site Request Forgery errors.
def addValues(request):
    try:
        s = Telemetry.objects.create(
            report_datetime = datetime.now(),
			battery = request.POST.get('BATTERY'),
			brake = request.POST.get('BRAKE'),
			coolant_t = request.POST.get('COOLANT_T'),
			fuel = request.POST.get('FUEL'),
			gear = request.POST.get('GEAR'),
			map = request.POST.get('MAP'),
			mat = request.POST.get('MAT'),
			o2 = request.POST.get('O2'),
			rpm = request.POST.get('RPM'),
			speed = request.POST.get('SPEED'),
			throttle = request.POST.get('THROTTLE'),
			wheel_t_1 = request.POST.get('WHEEL_T_1'),
			wheel_t_2 = request.POST.get('WHEEL_T_2'),
			wheel_t_3 = request.POST.get('WHEEL_T_3'),
			wheel_t_4 = request.POST.get('WHEEL_T_4'),
			wheel_v_1 = request.POST.get('WHEEL_V_1'),
			wheel_v_2 = request.POST.get('WHEEL_V_2'),
			wheel_v_3 = request.POST.get('WHEEL_V_3'),
			wheel_v_4 = request.POST.get('WHEEL_V_4'),
	    )
        s.save()

        return HttpResponse('Created OK', status=200)
    except MyException as ex:
        print "ERROR: " + ex.message
        return HttpResponse('Create failed. Error: ' + ex.message, status=500)
