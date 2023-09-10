from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Zaim Aydin Nazif',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
