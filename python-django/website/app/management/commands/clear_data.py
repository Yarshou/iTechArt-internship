from django.core.management.base import BaseCommand
from app.models import Shop


class Command(BaseCommand):

    def handle(self, *args, **options):
        Shop.objects.all().delete()
        print('Deleted successfully')
