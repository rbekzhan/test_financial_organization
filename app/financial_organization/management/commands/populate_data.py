from django.core.management.base import BaseCommand
from financial_organization.models import FinancialOrganization  # Import your model(s)


class Command(BaseCommand):
    help = 'Populate initial data'

    def handle(self, *args, **kwargs):
        FinancialOrganization.objects.create(name='АО "Отбасы банк"',
                                             first_leader='value2',
                                             board_of_directors='value3',
                                             chairman='value4',
                                             board_members='value5',
                                             director='value6',
                                             chief_accountant='value7',
                                             BIN='990805301225',
                                             address='value9',
                                             phone='77472095672',
                                             email='rakhmetzhan.bekzhan@gmail.com',
                                             website='value10.kz',
                                             license='0'
                                             )
        self.stdout.write(self.style.SUCCESS('Successfully populated initial data'))
