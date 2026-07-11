from django.core.management.base import BaseCommand
from orders.models import Table, Category, MenuItem
from orders.data.basic_menu_items import RESTAURANT_MENU


class Command(BaseCommand):
    help = "Seed restaurant tables and menu items"

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--n",
            type=int,
            default=10,
            help="Number of tables to create",
        )

    def handle(self, *args, **options):
        no_of_tables = options["n"]

        # -----------------------------
        # Create Tables
        # -----------------------------
        table_count = 0

        for number in range(1, no_of_tables + 1):
            _, created = Table.objects.get_or_create(
                name=f"Table {number}",
                defaults={
                    "is_reserved": False,
                },
            )

            if created:
                table_count += 1

        # -----------------------------
        # Create Categories & Menu Items
        # -----------------------------
        category_count = 0
        item_count = 0

        for category_name, items in RESTAURANT_MENU.items():

            category, created = Category.objects.get_or_create(
                name=category_name
            )

            if created:
                category_count += 1

            for item in items:
                _, created = MenuItem.objects.get_or_create(
                    category=category,
                    name=item["name"],
                    defaults={
                        "price": item["price"],
                        "description": item["description"],
                    },
                )

                if created:
                    item_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"""
=====================================
Restaurant Seed Completed
=====================================
Tables Created     : {table_count}
Categories Created : {category_count}
Menu Items Created : {item_count}
=====================================
"""
            )
        )