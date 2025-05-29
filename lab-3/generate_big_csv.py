import pandas as pd
import numpy as np

n = 100_000

df = pd.DataFrame({
    'площадь': np.random.randint(20, 150, size=n),
    'цена': np.random.randint(1_000_000, 20_000_000, size=n),
    'этаж': np.random.randint(1, 25, size=n),
    'кол-во_комнат': np.random.randint(1, 6, size=n)
})

df.to_csv('big_data.csv', index=False, encoding='utf-8-sig')
print("big_data.csv создан (100 000 строк)")
