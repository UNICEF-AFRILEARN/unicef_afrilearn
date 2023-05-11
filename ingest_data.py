# It loads data from a mongoDB database, cleans it and inserts it into another mongoDB database
from pymongo import MongoClient
import pandas as pd
import string
import random
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
mongo_cluster = config_object["MONGODB"]


# > This class is used to ingest data from a source and store it in a database
class DataIngestion():
    def load_data(self):
        """load data from MongoDB database
        This method loads the relevant data from the mongoDB database.
        """
        cluster = mongo_cluster


        client = MongoClient(cluster)

        self.db=client.afrilearn

        self.classes =  pd.DataFrame(list(self.db.courses.find()))
        self.lessons =  pd.DataFrame(list(self.db.lessons.find()))
        self.mainsubjects = pd.DataFrame(list(self.db.mainsubjects.find()))
        self.subjects  = pd.DataFrame(list(self.db.subjects.find()))
        self.recent_activities = pd.DataFrame(list(self.db.recentactivities.find()))


    def clean_and_merge(self):
        """
        It takes the dataframes from the MongoDB database and merges them into one dataframe.
        :return: A dataframe
        """
        self.lessons['videourl'] = self.lessons.videoUrls.apply(lambda x: list(x)[0]['videoUrl'] 
                                                    if len(list(x))>0 else "")

        df = self.subjects.merge(self.mainsubjects[['_id','name']],left_on=['mainSubjectId']
                            ,right_on=['_id'],how='inner')
        df = df.drop(['_id_y','__v'],axis=1)
        df = df.rename(columns={'_id_x':'subjectId'})
        df = df.merge(self.classes[['_id','name']],left_on=['courseId'],right_on=['_id'],how='inner')
        df = df.drop(['_id'],axis=1)
        df = df.rename(columns={'name_x':'subject_name','name_y':'class_name'})

        df = df.merge(self.lessons[['_id','views','subjectId','courseId','termId','videoUrls','title']]
                    ,left_on=['subjectId','courseId'],right_on=['subjectId','courseId'],how='right')
        df = df.rename(columns={'_id':'lessonId'})
        df = df.merge(self.recent_activities[['lessonId','userId']]
                    ,left_on='lessonId',right_on='lessonId',how='left')


        df['userId'] = df['userId'].apply(lambda x: ''.join(random.choice(string.ascii_lowercase) 
                                                            for i in range(24)) if x!=x else x)
        
        return df
    
    def insert_to_db(self):
        data = self.clean_and_merge(self)
        mycollection = self.db.trainingdata
        mycollection.insert_many(data.to_dict('records'))


if __name__=="__main__":
    data = DataIngestion()
    data.load_data()
    data = data.insert_to_db()
    print("Completed")
