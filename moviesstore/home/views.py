"""
• The Home page will feature a welcoming message.
• The About page will provide details about the Movies Store.
• The Movies page will exhibit information on available movies and include a filter to search movies
by name. Additionally, users can click on a specific movie to view its details and post reviews.
• The Cart page will showcase the movies added to the cart, along with the total price to be paid.
Users can also remove movies from the cart and proceed with purchases.
• The Register page will present a form enabling users to sign up for accounts.
• The Login page will present a form allowing users to log in to the application.
• The Orders page will display the orders placed by the logged-in user.
• The Admin panel will encompass sections to manage the store’s information, including creating,
updating, deleting, and listing information.
"""

from django.shortcuts import render

# Create your views here.
def index(request):
    """ View the Home page """
    template_data = {}
    template_data['title'] = 'Movies Store'

    return render(request, 'home/index.html', {'template_data': template_data})

def about(request):
    """ View the About page """
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {'template_data': template_data})
