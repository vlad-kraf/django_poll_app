from django.http import HttpResponse


def main_page(request):
    return HttpResponse("This is a main page")
