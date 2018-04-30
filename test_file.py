from helper_function import *
from create_vocab import *

eng_data,bangla_data = load_file_rmv_punct()

eng_vocab = make_vocab(eng_data)

print(eng_vocab)