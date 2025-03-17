import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("pokemon.csv")
type1_counts = df['type1'].value_counts()
type2_counts = df['type2'].value_counts()

type_counts = pd.DataFrame({
    'type1': type1_counts,
    'type2': type2_counts
})

type_counts.plot(kind='bar', figsize=(12, 6), color=['blue', 'orange'])
plt.xlabel('Type', fontsize=12)
plt.ylabel('Count', fontsize=12)

plt.show()