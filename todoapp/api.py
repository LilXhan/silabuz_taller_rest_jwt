from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDelAll(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        Todo.objects.all().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def todo_get_all(request):
    
    if request.method == 'GET':
        tasks = Todo.objects.all()

        serializer = TodoSerializer(tasks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def todo_del_all(request):

    if request.method == 'DELETE':

        Todo.objects.all().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class TodoGetAll(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Todo.objects.all()

        serializer = TodoSerializer(tasks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class GetTwoTasks(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Todo.objects.all()[:2]

        serializer = TodoSerializer(tasks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
