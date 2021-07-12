from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import HistorySerializer
from ..models import History


@api_view(['GET'])
def history_list(request, section):
    """
    Get the past scores for a section
    """
    try:
        history = History.objects.filter(section=section)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def best_score_by_section(request, section):
    """
    Get the best score for the past scores for a section
    """
    try:
        best_history = History.objects.filter(section=section).order_by('score').first()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HistorySerializer(best_history)
        return Response(serializer.data)


@api_view(['POST'])
def history_post(request):

    if request.method == "POST":
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def history_details(request, pk):
    try:
        history = History.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HistorySerializer(history)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = HistorySerializer(history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)