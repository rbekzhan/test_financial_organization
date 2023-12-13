from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page
from .models import FinancialOrganizationNews, FinancialOrganization


@cache_page(60*10)
def news(request):
    organization = FinancialOrganization.objects.first()
    news_list = FinancialOrganizationNews.objects.filter(organization=organization).all()
    template = loader.get_template('index.html')
    context = {
        'organization': organization,
        'news_list': news_list
    }
    return HttpResponse(template.render(context, request))
