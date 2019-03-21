from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import account
from .serializers import UserSerializer

#User
class UserView(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(account.objects.filter(id = request.user.id), many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Please login"})
