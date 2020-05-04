import panads as pd
import numpy as np 

df=pd.read_csv("input/foreign_sample.csv")
df['score'] = pd.Series( 0 , index = df.index)

def levenshtein_score(string1, string2):
    score = 0
    i=0
    matching = 0
    # set score maximum the length of the longer string
    if string1 == NaN:
        string1 = ''
    if stirng2 == NaN:
        string2 = ''
        
    if len(string1)>len(string2):
        score = len(string1)
        #make the strings equally long
        string2 = string2 + ((len(string1)-len(string2))*' ')
            
    else:
        score = len(string2)
        string1 = string1 + ((len(string2)-len(string1))*' ')
        
    #count matching characters
    while i < score:
        if string1[i] == string2[i]:
            matching = matching + 1    
        i = i + 1

    score = 1-(score - matching)/len(string1)
    return score

    i = 0
    #loop to create levenshtein score row-wise, not working properly yet
    #missing observations are an issue yet
	while i < len(df):
    df.at[i, 'score'] = levenshtein_score(df.Partner[i], df.Name[i])
    i = i+1