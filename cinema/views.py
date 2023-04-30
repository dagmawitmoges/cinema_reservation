from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')
def movie_description(request):
    return render(request, 'm-description.html')
def about_us(request):
    return render(request, 'about.html' )
def seat_page(request):
    return render(request, 'seat.html' )
def ticket_page(request):
    return render(request, 'ticket.html' )