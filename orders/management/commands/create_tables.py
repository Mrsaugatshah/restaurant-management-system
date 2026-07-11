from django.core.management.base import BaseCommand
from orders.models import Table


class Command(BaseCommand):
    help = 'helps to populate/seed/config tables for  a resturant'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--n',
            dest='n',
            type=int,
            metavar='N',
            help='No. of tables',
            default=10
        )

    def handle(self, **options):
        no_of_tables = options.get('n')
        for number in range(1, no_of_tables + 1):
            Table.objects.get_or_create(
                name=f"Table{number}",
                defaults={
                    'is_reserved': False
                }
            )

        self.stdout.write(
            self.style.SUCCESS(f'Created {no_of_tables} table(s) successfully!')
        )