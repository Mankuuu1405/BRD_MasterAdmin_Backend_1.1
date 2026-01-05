from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group

class RoleListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        roles = Group.objects.all().values("id", "name")
        return Response(roles)
