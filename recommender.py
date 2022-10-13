import pandas as pd
import pickle

df = pickle.load(open("recommendations.pkl", 'rb'))

def recommend(course: str, subject: str, lesson: str,length:int):
    if lesson in df['lesson_id'].unique():
        recommendation = df[(df['school_level']==course)&(df['subject']==subject)&(df['lesson_id']==lesson)]
        recommendation = recommendation.iloc[0:length,:]
    else:
        recommendation = df[(df['school_level']==course)]
        recommendation = recommendation.iloc[0:length,:]
    return recommendation