import nltk as n
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re, collections
def sentence_to_wordlist(input_sentence):
    clean_sentence = re.sub("[^a-zA-Z0-9]", " ", input_sentence)
    tokens = n.word_tokenize(clean_sentence)

    return tokens


from nltk.corpus import stopwords


def remove_stop_word(word_list):
    stop_words = set(stopwords.words('english'))

    word_tokens = n.word_tokenize(word_list)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence


def avg_word_len(essay):
    clean_essay = re.sub(r'\W', ' ', essay)
    # print()
    words = n.word_tokenize(clean_essay)

    return sum(len(word) for word in words) / len(words)


def sent_count(essay):
    sentences = n.sent_tokenize(essay)

    return len(sentences)


def word_count(essay):
    clean_essay = re.sub(r'\W', ' ', essay)
    words = n.word_tokenize(clean_essay)

    return len(words)


def tokenize(essay):
    stripped_essay = essay.strip()

    tokenizer = n.data.load('tokenizers/punkt/english.pickle')
    raw_sentences = tokenizer.tokenize(stripped_essay)

    tokenized_sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            tokenized_sentences.append(sentence_to_wordlist(raw_sentence))

    return tokenized_sentences


def count_pos(essay):
    tokenized_sentences = tokenize(essay)

    noun_count = 0
    adj_count = 0
    verb_count = 0
    adv_count = 0

    for sentence in tokenized_sentences:
        tagged_tokens = n.pos_tag(sentence)

        for token_tuple in tagged_tokens:
            pos_tag = token_tuple[1]

            if pos_tag.startswith('N'):
                noun_count += 1
            elif pos_tag.startswith('J'):
                adj_count += 1
            elif pos_tag.startswith('V'):
                verb_count += 1
            elif pos_tag.startswith('R'):
                adv_count += 1

    return noun_count, adj_count, verb_count, adv_count


# checking number of misspelled words

def count_spell_error(essay):
    clean_essay = re.sub(r'\W', ' ', str(essay).lower())
    clean_essay = re.sub(r'[0-9]', '', clean_essay)

    # big.txt: It is a concatenation of public domain book excerpts from Project Gutenberg
    #         and lists of most frequent words from Wiktionary and the British National Corpus.
    #         It contains about a million words.
    data = open('big.txt').read()

    words_ = re.findall('[a-z]+', data.lower())

    word_dict = collections.defaultdict(lambda: 0)

    for word in words_:
        word_dict[word] += 1

    clean_essay = re.sub(r'\W', ' ', str(essay).lower())
    clean_essay = re.sub(r'[0-9]', '', clean_essay)

    mispell_count = 0

    words = clean_essay.split()

    for word in words:
        if not word in word_dict:
            mispell_count += 1
            # print(word)

    return mispell_count


def count_lemmas(essay):
    tokenized_sentences = tokenize(essay)

    lemmas = []
    wordnet_lemmatizer = WordNetLemmatizer()

    for sentence in tokenized_sentences:
        tagged_tokens = n.pos_tag(sentence)

        for token_tuple in tagged_tokens:

            pos_tag = token_tuple[1]

            if pos_tag.startswith('N'):
                pos = wordnet.NOUN
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            elif pos_tag.startswith('J'):
                pos = wordnet.ADJ
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            elif pos_tag.startswith('V'):
                pos = wordnet.VERB
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            elif pos_tag.startswith('R'):
                pos = wordnet.ADV
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            else:
                pos = wordnet.NOUN
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))

    lemma_count = len(set(lemmas))

    return lemma_count


def extract_features(data):
    features = data.copy()

    features['char_count'] = features['essay'].apply(char_count)

    features['word_count'] = features['essay'].apply(word_count)

    features['sent_count'] = features['essay'].apply(sent_count)

    features['avg_word_len'] = features['essay'].apply(avg_word_len)

    features['lemma_count'] = features['essay'].apply(count_lemmas)

    features['spell_err_count'] = features['essay'].apply(count_spell_error)

    features['noun_count'], features['adj_count'], features['verb_count'], features['adv_count'] = zip(
        *features['essay'].map(count_pos))

    return features


def values(eassy):
    features = {}
    # features['char_count'] = char_count(eassy)

    # features['word_count'] = word_count(essay)

    # features['sent_count'] = sent_count(essay)

    features['avg_word_len'] = avg_word_len(eassy)

    features['lemma_count'] = count_lemmas(eassy)

    features['spell_err_count'] = count_spell_error(eassy)
    features['noun_count'], features['adj_count'], features['verb_count'], features['adv_count'] = count_pos(eassy)

    return features


def char_count(essay):
    clean_essay = re.sub(r'\s', '', str(essay).lower())

    return len(clean_essay)


data = pd.read_csv("test_case.csv")
# printing values
# print(data.columns.values)
independent_variables = data.columns
independent_variables = independent_variables.delete(0)
independent_variables = independent_variables.delete(0)
independent_variables = independent_variables.delete(0)
independent_variables = independent_variables.delete(0)
# independent_variables=independent_variables.delete(9)
independent_variables = independent_variables.delete(1)
independent_variables = independent_variables.delete(0)

x = data[independent_variables]
y = data["domain1_score"]
import sklearn.linear_model as lm
lr = lm.LinearRegression()
lr.fit(x, y)
# prediction
y_pre = lr.predict(x)

def fun1(essay):
    r=values(essay)
#print(r)
    for i in independent_variables:
        r_df=pd.DataFrame(data=r,index=[0],columns=x.columns)
#print(r_df)
    y=lr.predict(r_df)
    print(int(y[0]))
    nc,adjc,vc,advc=count_pos(essay)
    s="Grade out of (1-10) : "+str(int(y[0]))+"\n\nNumber of Misspelled words is(are) :"+str(count_spell_error(essay))
    print(s)
    return s





