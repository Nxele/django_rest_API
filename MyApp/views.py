# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import requests

@api_view(["POST"])
def get_data(points):
    try:
        sent_points = json.loads(points.body)
        dict_data = {
                "summary": {
                        "status": "Processed",
                        "queryTime": 0,
                        "totalQueries": len(sent_points['payload']),
                        "totalResults": 0
                },
                "results": []
        }
        for count, point in enumerate(sent_points['payload']):
                getReverseGeocode = requests.get("http://134.209.228.30:4000/v1/11111111111111111111111111111111/reverseGeocode/"+point+".json?returnSpeedLimit=true")

                if getReverseGeocode.status_code is 200:
                        get_data = getReverseGeocode.json()
                        dict_data['results'].append({
                                "result": get_data,
                                "query": point
                        })
                        dict_data["summary"]["queryTime"] += get_data["summary"]["queryTime"]
                        dict_data["summary"]["totalResults"] += 1
        return JsonResponse(dict_data,safe=False)

    except ValueError as exc:
            return Response(exc.args[0],status.HTTP_400_BAD_REQUEST)
# Create your views here.
