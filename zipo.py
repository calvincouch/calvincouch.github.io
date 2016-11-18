import pandas as pd 


a = input("year?  ")
gitter = str("https://github.com/calvincouch/calvincouch.github.io/blob/master/datc/DAT_ASCII_USDJPY_M1_",a,".csv")

df = pd.read_csv(gitter)

print df
