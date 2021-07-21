from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'notes/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of notes',
        },
        {
            'Endpoint': 'notes/id/',
            'method': 'GET',
            'body': None,
            'description': 'returns a single note object',
        }, {
            'Endpoint': 'notes/create/',
            'method': 'POST',
            'body': {'title': "", 'description': ""},
            'description': 'creates a new note',
        }, {
            'Endpoint': 'notes/id/update/',
            'method': 'PUT',
            'body': {'title': "", 'description': ""},
            'description': 'update an  existing note',
        }, {
            'Endpoint': 'notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'deletes an existing note',
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        title=data['title'],
        description=data['description'],
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    updated_data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=updated_data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted")
