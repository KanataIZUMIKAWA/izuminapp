from django.core.management.base import BaseCommand
from subekashi.models import Singleton
from datetime import date


class Command(BaseCommand):
    help = "最終更新日のアップデート"

    def handle(self, *args, **options) :
            singletonIns, _ = Singleton.objects.update_or_create(key = "lastModified", defaults = {"key": "lastModified"})
            singletonIns.key = "lastModified"
            v = options['v']
            today = date.today().strftime("%Y-%m-%d")
            value = f"{today} (ver.{v})" if v else today
            singletonIns.value = value
            singletonIns.save()
            self.stdout.write(self.style.SUCCESS(f"version: {value}"))
            
    def add_arguments(self, parser):
        parser.add_argument('--v', required=False, type=str)