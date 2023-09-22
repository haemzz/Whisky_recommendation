import pandas as pd
from fuzzywuzzy import fuzz

class WhiskeyFindProcessor:
    def __init__(self, csv_file_path, sim_length=7, threshold_similarity=60):
        self.df = pd.read_csv(csv_file_path, encoding='utf-8')
        self.sim_length = sim_length
        self.threshold_similarity = threshold_similarity

    def find_similar_names(self, name):
        temp_Sr = self.df['nameEng'].apply(str.lower)
        similar_names = self.df[self.df['nameEng'].apply(lambda x: fuzz.partial_ratio(x, name) >= self.threshold_similarity)]
        similar_names = similar_names.reset_index(drop=True)
        return similar_names

    def result_list(self, input_whiskey):
        target_name = input_whiskey.lower()
        similar_names = self.find_similar_names(target_name)
        result = similar_names.loc[:self.sim_length, 'nameEng'].to_list()
        return result