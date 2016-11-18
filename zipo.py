import pandas as pd 


year = input("year?  ")
gitter = str("https://github.com/calvincouch/calvincouch.github.io/blob/master/datc/DAT_ASCII_USDJPY_M1_",input(year),".csv")

df = pd.read_csv(gitter)

df
