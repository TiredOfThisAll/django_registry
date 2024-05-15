from django.template import loader
from django.http import HttpResponse, JsonResponse
from .utils import split_phone_number
from .models import Registry


def main_page(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request))


def get_phone_number_info(request):
    phone_number = request.POST["phone_number"]
    phone_number = split_phone_number(phone_number)
    info = Registry.objects.filter(
        abc=phone_number["operator_code"],
        end__gte=phone_number["rest_numbers"],
        start__lte=phone_number["rest_numbers"]
    ).first()
    if not info:
        return JsonResponse({"error": "Incorrect phone number"})
    phone_number_info = {
        "abc": info.abc,
        "start": info.start,
        "end": info.end,
        "capacity": info.capacity,
        "operator": info.operator,
        "region": info.region,
        "gar_territory": info.GAR_territory,
        "tin": info.TIN
        }
    return JsonResponse(phone_number_info)
