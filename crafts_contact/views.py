from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact


class Contact(APIView):
    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        subject = request.data.get("subject")
        message = request.data.get("message")

        if not name or not email or not subject or not message:
            return Response( status=status.HTTP_400_BAD_REQUEST)
        
        Contact.objects.create(
            name=name, email=email, subject=subject, message=message
        )

        return Response(status=status.HTTP_201_CREATED)
    
