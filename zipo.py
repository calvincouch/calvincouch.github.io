import pandas as pd 
import httplib2

data = httplib2.Http("https://github.com/calvincouch/calvincouch.github.io/blob/master/datc/DAT_ASCII_USDJPY_M1_2000.csv")

df = pd.read_csv("https://github.com/calvincouch/calvincouch.github.io/blob/master/datc/DAT_ASCII_USDJPY_M1_2000.csv")

print df