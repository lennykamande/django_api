import time
from django import db

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class command(BaseCommand):
    def handle(self):
        self.stdout.write('waiting for db')
        db.conn = None
        while not db.conn:
            try:
                db.conn = connections['default']
            except OperationalError:
                self.stdout.write("Database Unavailable please wait")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Connection Successful'))