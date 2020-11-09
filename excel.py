import pandas as pd
from datetime import datetime

class Excel():
    def __init__(self):
        self.df = pd.read_excel('datos.xlsx')
        
    def get_names(self, d_inicio: (), d_fin: (), imprimir = False):
        nombres = []
        for i in range(len(self.df)):
            date_str = self.df.iloc[i]['Fecha de nacimiento']
            try:
                date = datetime.strptime(date_str,"%Y-%m-%d")
            except:
                if date_str == '0000-00-00' and imprimir:
                    print(str(i + 2) + ': No fecha')
                continue

            d_date = (date.month, date.day)

            if d_inicio <= d_date <= d_fin:
                nombres.append({
                    'numero': i,
                    'nombre': self.df.iloc[i]['nombre'],
                    'fecha': d_date
                })

        return nombres