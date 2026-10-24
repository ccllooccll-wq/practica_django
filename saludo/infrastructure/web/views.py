import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from saludo.application.services.saludar_service import SaludarService


@csrf_exempt
def saludar(request):
    if request.method != "POST":
        return JsonResponse({"error": "Usa POST"}, status=405)

    datos = json.loads(request.body)
    mensaje = SaludarService().saludar(datos["nombre"])
    return JsonResponse({"mensaje": mensaje})