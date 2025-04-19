from django.http import JsonResponse
from datetime import datetime
import platform

def index(request):
    if platform.system() == "Windows":
        # Use Windows-compatible format
        current_time = datetime.now().strftime("%I:%S %p")
        current_date = datetime.now().strftime("%A %m %Y")
    else:
        # Use Unix-compatible format
        current_time = datetime.now().strftime("%-I:%S %p")
        current_date = datetime.now().strftime("%A %m %-Y")

    data = {
        'time': current_time,
        'date': current_date,
    }

    return JsonResponse(data)
