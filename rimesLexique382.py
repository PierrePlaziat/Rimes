"""------------"""
""" find rimes """
"""------------"""  
 
import pandas as pd

search = input()

lex = pd.read_csv('Lexique382.tsv', sep='\t')
lex.head()
searchdetail = lex[lex.ortho==search]
phons = searchdetail.iloc[0,22]
phonList = phons.split("-")[-1]
phon = phonList
rimes = lex.loc[lex.syll.str.endswith(phon)]
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(rimes['ortho'])
