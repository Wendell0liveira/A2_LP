from django.core.management.base import BaseCommand, CommandError
from corrida.models import Race
import pandas as pd
class Command(BaseCommand):
    help = 'Atualiza as corridas'

    def handle(self, *args, **options):
        Corridas = pd.read_csv("corridas.csv")
        print("kkkkkkkkkkkkkkkkkk")
        print(Race.objects.all())
        #print(Corridas)
        for index, row in Corridas.iterrows():
            print(row['begin'])
            Race.objects.create(begin=row['begin'],end = row['end'],rating = row['rating'])
        print(Race.objects.all())
        

    