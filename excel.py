import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta

class Excel():
    def __init__(self, d_inicio: date, d_fin: date):
        self.df = pd.read_excel('datos.xlsx')
        self.personas = []
        self.df_personas = None

        self.d_inicio = d_inicio.replace(year=1)
        self.d_fin = d_fin.replace(year=1)
        
    def get_names(self, imprimir = False):
        for i in range(len(self.df)):
            date_str = self.df.iloc[i]['Fecha de nacimiento']
            try:
                d_date = datetime.strptime(date_str,"%Y-%m-%d").date()
                d_date = d_date.replace(year=1)
            except:
                if date_str == '0000-00-00' and imprimir:
                    print(str(i + 2) + ': No fecha')
                continue

            if self.d_inicio <= d_date <= self.d_fin:
                cel = self.df.iloc[i]['Celular']
                self.personas.append({
                    'numero': i,
                    'nombre': self.df.iloc[i]['nombre'],
                    'fecha': d_date,
                    'cel': cel,
                    'link': ('https://wa.me/52' + str(cel)) if cel is not np.nan else 'No cel'
                })

        self.df_personas = pd.DataFrame(self.personas)
        return self.personas

    def crear_csv(self):
        d_actual = self.d_inicio
        delta = timedelta(days=1)
        while d_actual <= self.d_fin:
            path = 'results/' + d_actual.strftime("%B") + '/' + str(d_actual.day) + '/' + 'enlaces.csv'
            df_actual = self.df_personas[self.df_personas['fecha'] == d_actual]
            df_actual.to_csv(path)
            d_actual += delta
