from django.shortcuts import render


def fifteen(request):
    return render(request, 'fifteen.html', context={'customer_id_logged_in': "ASD"})