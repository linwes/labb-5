import numpy as np
from numpy import percentile
import pandas as pd
import csv, sys
import matplotlib.pyplot as plt
import seaborn as sns

df_csv = pd.read_csv('santVäder.csv', sep=';', names=['år' , 'tempÅr', 'avvikelse år', 'tempVår', 'avvikelse vår', 'tempSommar', 'avvikelse sommar', 'tempHöst', 'avvikelse höst', 'tempVinter', 'avvikelse vinter']) 
df_csv.set_index('år')

år = df_csv[['tempÅr', 'avvikelse år']]

år.plot(title='År', kind='line')
plt.ylabel('tempratur')
plt.xlim(left=1860)
plt.xlim(right=2016)
plt.show()

medianÅr = df_csv['tempÅr']
procentÅr = percentile(medianÅr, [25, 50, 75])
print(f"medianen för åren är : ",(procentÅr))
kallasteÅret = percentile(medianÅr, [1])
varmasteÅret = percentile(medianÅr, [100])
print(f"kallaste medel tempraturen under åren var", kallasteÅret, "grader")
print(f"Varmaste medel tempraturen under åtren var", varmasteÅret, "grader")

# num_bins = 180
# n, bins, patches = plt.hist(medianÅr, num_bins, facecolor='blue', alpha=0.5)
# plt.show()

allt = df_csv[['tempÅr', 'tempVår', 'tempSommar', 'tempHöst', 'tempVinter']]

# ax = sns.heatmap(df_csv)

vår = df_csv[['tempVår', 'avvikelse vår']]

vår.plot(title='Vår', kind='line')
plt.ylabel('tempratur')
plt.show()

medianVår = df_csv['tempVår']
procentVår = percentile(medianVår, [25, 50, 75])
print(f"medianen för våren är : ",(procentVår))
kallasteVåren = percentile(medianVår, [1])
varmasteVåren = percentile(medianVår, [100])
print(f"kallaste medel tempraturen under våren var", kallasteVåren, "grader")
print(f"Varmaste medel tempraturen under våren var", varmasteVåren, "grader")

sommar = df_csv[['tempSommar', 'avvikelse sommar']]

sommar.plot(title='sommar', kind='line')
plt.ylabel('tempratur')
plt.show()

medianSommar = df_csv['tempSommar']
procentSommar = percentile(medianSommar, [25, 50, 75])
print(f"medianen för sommaren är : ",(procentSommar))
kallasteSommaren = percentile(medianSommar, [1])
varmasteSommaren = percentile(medianSommar, [100])
print(f"kallaste medel tempraturen under Sommaren var", kallasteSommaren, "grader")
print(f"Varmaste medel tempraturen under Sommaren var", varmasteSommaren, "grader")

höst = df_csv[['tempHöst', 'avvikelse höst']]

höst.plot(title='Höst', kind='line')
plt.ylabel('tempratur')
plt.show()

medianHöst = df_csv['tempHöst']
procentHöst = percentile(medianHöst, [25, 50, 75])
print(f"medianen för hösten är : ",(procentHöst))
kallasteHösten = percentile(medianHöst, [1])
varmasteHösten = percentile(medianHöst, [100])
print(f"kallaste medel tempraturen under hösten var", kallasteHösten, "grader")
print(f"Varmaste medel tempraturen under hösten var", varmasteHösten, "grader")

vinter = df_csv[['tempVinter', 'avvikelse vinter']]

vinter.plot(title='Vinter', kind='line')
plt.ylabel('tempratur')
plt.show()

medianVinter = df_csv['tempVinter']
procentVinter = percentile(medianVinter, [25, 50, 75])
print(f"medianen för vintern är : ",(procentVinter))
kallasteVintern = percentile(medianVinter, [1])
varmasteVintern = percentile(medianVinter, [100])
print(f"kallaste medel tempraturen under vintern var", kallasteVintern, "grader")
print(f"Varmaste medel tempraturen under vintern var", varmasteVintern, "grader")

allSkillnad = df_csv[['avvikelse vår', 'avvikelse sommar', 'avvikelse höst', 'avvikelse vinter']]
allSkillnad.plot(title='skillnad i tempratur', kind='line')
plt.ylabel('tempratur')
plt.show()


# hehej=(kallasteVintern, kallasteHösten, kallasteSommaren, kallasteVåren, kallasteÅret)
# hehej.plot(title='skillnad i tempratur', kind='line')
# plt.ylabel('tempratur')
# plt.show()


plt.scatter(medianSommar, medianVår, medianHöst, medianVinter)
plt.ylabel('tempratur')
plt.colorbar()
plt.show()

allt.plot(title='skillnad i tempratur', kind='line')
plt.ylabel('tempratur')
plt.show()

# plt.hist2d(medianSommar, medianHöst, medianVinter, medianVår)
# plt.show()

# df_web = pd.DataFrame(df_csv)

# print(f'df_web:\n{df_web}')

# df_csv.plot(title='tempÅR', kind='line')
# plt.ylabel('år')
# plt.show()