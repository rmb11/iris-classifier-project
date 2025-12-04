from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ml.predict import predict

# Create your views here.
@csrf_exempt
def predict_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST is allowed."}, status=405)

    # ML prediction to go here later
    return JsonResponse({"message": "Predict API is wired up!"})