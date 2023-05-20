from django.shortcuts import render


def admin_inf(request):
    return render(request, 'admin.html', context={'customer_id_logged_in': "ASD"})