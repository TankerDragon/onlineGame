from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from requests import request

#####
from .test import get_num, start_looping, stop_looping


def main(request):
    return render(request, 'index.html')


@api_view(['GET', 'POST'])
def update(request):
    if request.method == 'GET':
        # print(get_num())
        return Response({"num": get_num()})
    elif request.method == 'POST':
        print(request.data)
        if request.data['game'] == 'start':
            start_looping()
            return Response(status=status.HTTP_200_OK)

        elif request.data['game'] == 'stop':
            stop_looping()
            return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
