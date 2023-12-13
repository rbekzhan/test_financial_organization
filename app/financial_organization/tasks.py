import datetime
import uuid

from celery import shared_task

from financial_organization.models import FinancialOrganizationNews, FinancialOrganization


@shared_task
def update_news_by_organization_id():
    organizations = FinancialOrganization.objects.all()
    for organization in organizations:
        # Пример URL API новостного агрегатора
        # сначала надо создать object NewsAggregator потом вызывать метод get_news и получить данные оттуда и записать
        # данные к postgres



        # Выполнение запроса к API
        # response = requests.get(api_url, params=params)
        status_code = 200
        # Обработка ответа от API
        if status_code == 200:
            # news_data = response.json()
            news_data = {
                'organization_id': str(organization.id),
                'content': 'Here full text content',
                'title': 'here title news',
                'date_published': datetime.datetime.now().isoformat(),
            }
            data = FinancialOrganizationNews(
                organization_id=uuid.UUID(news_data['organization_id']),
                content=news_data['content'],
                title=news_data['title'],
                date_published=datetime.datetime.fromisoformat(news_data['date_published'])
            )
            data.save()
        else:
            # Обработка ошибок, если такие есть
            pass

