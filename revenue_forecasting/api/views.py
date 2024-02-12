from django.http import JsonResponse
from rest_framework.views import APIView
import pickle
import numpy as np

class PrediccionRevenueView(APIView):
    def get(self, request, *args, **kwargs):
        # Cargar el modelo
        with open('../revenue_apple_model.pickle', 'rb') as archivo:
            modelo = pickle.load(archivo)

        # Obtener los datos de la solicitud
        datos = request.data
        # Aquí deberías validar y transformar los datos según sea necesario
        predictores = np.array([datos['open'], datos['high'], datos['low'], datos['close']]) 

        # Hacer la predicción
        prediccion = modelo.predict([predictores])

        # Devolver la respuesta
        return JsonResponse({'prediccion': prediccion.tolist()})
