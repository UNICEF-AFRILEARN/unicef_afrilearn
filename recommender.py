import pandas as pd
import pickle


def recommend(course: str, subject: str, lesson: str):
    try:
        school_dict = pickle.load(open("dictionary/school_level_dict.pkl", 'rb'))
        lesson_dict = pickle.load(open("dictionary/lesson_dict.pkl", 'rb'))
        top10_dict = pickle.load(open("dictionary/top10_dict.pkl", 'rb'))
        if course in ['SSS One', 'SSS Two', 'SSS Three']:
            science_subjects = pickle.load(open('subject_names/science_subjects.pkl', 'rb'))
            if subject in science_subjects:
                course_rec_rules = pickle.load(open(str('subjects/') + school_dict[str(course) + ' science'], 'rb'))
            else:
                course_rec_rules = pickle.load(
                    open(str('subjects/') + school_dict[str(course) + ' socialscience'], 'rb'))
        else:
            course_rec_rules = pickle.load(open(str('subjects/') + school_dict[course], 'rb'))
        recommendation_list = []
        for i, courses in enumerate(course_rec_rules["antecedents"]):
            for j in list(courses):
                if j == subject:
                    recommendation_list.append(list(course_rec_rules.iloc[i]["consequents"])[0])
        recommendation_list = pd.DataFrame(recommendation_list).drop_duplicates()
        recommended_subject = list(recommendation_list[0])
        other_subjects_to_watch = pickle.load(open(str('top10/')+top10_dict[str(recommended_subject[0]) + '_' + str(course)], 'rb'))

        lesson_rec_rules = pickle.load(open(str('lessons/') + lesson_dict[subject + '_' + course], 'rb'))
        recommendation_list = []
        if lesson:
            for i, lessons in enumerate(lesson_rec_rules["antecedents"]):
                for j in list(lessons):
                    if j == lesson:
                        recommendation_list.append(list(lesson_rec_rules.iloc[i]["consequents"])[0])
            recommendation_list = pd.DataFrame(recommendation_list).drop_duplicates()
            recommendation_list = list(recommendation_list[0])
            recommendation = recommendation_list[0:5]
            df = pd.DataFrame(other_subjects_to_watch[0:5], columns=[subject])
            df[recommended_subject[0]] = recommendation[0:5]
            return df
    except Exception as e:
        print(e)
        print('Welcome to Afrilearn!')
