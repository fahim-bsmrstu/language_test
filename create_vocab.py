from collections import Counter

def make_vocab(file):
    all_word = []
    word_keys = []
    lang_processed =[]

    vocab_size = 1000


    #seperate every word
    for sent in file:
        for word in sent:
            all_word.append(word)

    all_word_count = Counter(all_word) #make a dictionary with the frequency of each word as their key

    for x in all_word_count.most_common(vocab_size-1):
        word_keys.append(x[0])

    vocab2ix = dict(zip(word_keys,range(1,vocab_size)))

    ix2vocab = {val: key for key, val in vocab2ix.items()}

    for sent in file:
        temp_sent = []
        for word in sent:
            try:
                temp_sent.append(vocab2ix[word])
            except:
                temp_sent.append(0)
        lang_processed.append(temp_sent)

