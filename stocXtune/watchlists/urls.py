
from django.urls import path
from django.views.generic import TemplateView

app_name = 'watchlists'

urlpatterns = [
    
    path('', TemplateView.as_view(template_name="watchlist/index.html")),
]