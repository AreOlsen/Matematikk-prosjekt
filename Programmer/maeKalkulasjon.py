import pandas as pd
import math

# Last inn data
fil = "torsk.csv"
datafil = pd.read_csv(fil, sep=",", comment="#", decimal=".")
codDataSet = datafil["TORSK"].tolist()

#T(t) = 526052 + 190105 × sin(0.7295t + 1.96), årstall etter 1987.
def regresjonsModel(årstall):
    return 526052+190105*math.sin(0.7295*årstall+1.96)

#Kalkuler MAE, MAE = 1/n × Sum i=0 => n (|y_i − y_iˆ |).
def kalkulerMAE():
    midlertidigVerdi = 0
    for i in range(len(codDataSet)):
        regresjonsVerdi = regresjonsModel(i)
        ekteVerdi = float(codDataSet[i])*1000 #Over frå '000 tonn til tonn.
        midlertidigVerdi+=abs(ekteVerdi-regresjonsVerdi)
    return midlertidigVerdi/len(codDataSet)

MAE = kalkulerMAE()
print(f'MAE er {MAE} i verdi.')