import os
from zipfile import ZipFile
import string

punct = string.punctuation

file_dir = ''
file_name = 'test.txt'
data_from_file = []
output_after_punct = []
eng_data = []
bangla_data = []
split_data_first_phase = []
eng_data_after_lowercase = []
bangla_data_after_lowercase = []



#load the file, then remove punctuation

def lower_case(file):
    data_after_lowercase = []

    for x in file:
        data_after_lowercase.append(x.lower().split())
    return data_after_lowercase

def load_file_rmv_punct():

    #load file
    with open(os.path.join(file_dir,file_name),'r',encoding='utf-8')as f:
        for row in f:
            data_from_file.append(row[:-1])


   #remove punctuation

    for sent in data_from_file:
        out_str = ''
        for char in sent:
            if char not in punct:
                out_str = out_str+char
        output_after_punct.append(out_str)


    #split the dataset into two list for two language

    for x in output_after_punct:
        if len(x)>=1:
            split_data_first_phase.append(x.split('\t'))

    [eng_data,bangla_data] = [list(x) for x in zip(*split_data_first_phase)]

    eng_data_after_lowercase = lower_case(eng_data)
    bangla_data_after_lowercase = lower_case(bangla_data)

    return eng_data_after_lowercase,bangla_data_after_lowercase