import csv
import pandas as pd
from django.core.management.base import BaseCommand
from models.models import NetflixRevenue
from datetime import datetime
import os

class Command(BaseCommand):
    help = 'Importa los ingresos de Netflix desde un archivo CSV'

    def handle(self, *args, **kwargs):
        dir_ = os.getcwd()
        data_netflix = pd.read_csv(os.path.join(dir_, 'netflix_revenue_updated.csv'))
        for index, row in data_netflix.iterrows():
            NetflixRevenue.objects.create(
                date=datetime.strptime(row['Date'], '%d-%m-%Y'),
                global_revenue=int(row['Global Revenue']),
                ucan_streaming_revenue=int(row['UCAN Streaming Revenue']),
                emea_streaming_revenue=int(row['EMEA Streaming Revenue']),
                latm_streaming_revenue=int(row['LATM Streaming Revenue']),
                apac_streaming_revenue=int(row['APAC Streaming Revenue']),
                ucan_members=int(row['UCAN Members']),
                emea_members=int(row['EMEA  Members']),
                latm_members=int(row['LATM Members']),
                apac_members=int(row['APAC Members']),
                ucan_arpu=float(row['UCAN ARPU']),
                emea_arpu=float(row['EMEA ARPU']),
                latm_arpu=float(row['LATM  ARPU']),
                apac_arpu=float(row['APAC  ARPU']),
                netflix_streaming_memberships=int(row['Netflix Streaming Memberships ']),
            )
        self.stdout.write(self.style.SUCCESS('Datos importados con éxito'))
