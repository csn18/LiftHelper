from django.shortcuts import render


def main(request):
    return render(request, 'Main/main-page.html')
