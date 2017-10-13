import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def read_tweets(fname, t_type):
    tweets = []
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        tweets.append([line, t_type])
        line = f.readline()
    f.close()
    return tweets


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
    return features


def classify_tweet(tweet):
    return \
        classifier.classify(extract_features(nltk.word_tokenize(tweet)))

def read_datasets_joy():
    data = []
    t_type = 'joy'
    fname = 'NRC-Emotion-Lexicon-v0.92/translate_data/JOY_WORDS.txt'
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        data.append([line, t_type])
        line = f.readline()
    f.close()

    return data

def read_datasets_disgust():
    data = []
    t_type = 'disgust'
    fname = 'NRC-Emotion-Lexicon-v0.92/translate_data/DISGUST_WORDS.txt'
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        data.append([line, t_type])
        line = f.readline()
    f.close()

    return data

def read_datasets_sadness():
    data = []
    t_type = 'sadness'
    fname = 'NRC-Emotion-Lexicon-v0.92/translate_data/SADNESS_WORDS.txt'
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        data.append([line, t_type])
        line = f.readline()
    f.close()

    return data

def read_datasets_anger():
    data = []
    t_type = 'anger'
    fname = 'NRC-Emotion-Lexicon-v0.92/translate_data/ANGER_WORDS.txt'
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        data.append([line, t_type])
        line = f.readline()
    f.close()

    return data

def read_datasets_fear():
    data = []
    t_type = 'fear'
    fname = 'NRC-Emotion-Lexicon-v0.92/translate_data/FEAR_WORDS.txt'
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        data.append([line, t_type])
        line = f.readline()
    f.close()

    return data


# read in postive and negative training tweets
joy_feel = read_tweets('dataset/nrc/asli/sinonim/translate/anger.txt', 'joy')
disgust_feel = read_tweets('dataset/nrc/asli/sinonim/translate/disgust.txt', 'disgust')
sadness_feel = read_tweets('dataset/nrc/asli/sinonim/translate/fear.txt', 'sadness')
anger_feel = read_tweets('dataset/nrc/asli/sinonim/translate/joy.txt', 'anger')
surprise_feel = read_tweets('dataset/nrc/asli/sinonim/translate/sadness.txt', 'surprise')
fear_feel = read_tweets('dataset/nrc/asli/sinonim/translate/surprise.txt', 'fear')


# filter away words that are less than 3 letters to form the training data
tweets = []
for (words, sentiment) in joy_feel + disgust_feel + sadness_feel + anger_feel + surprise_feel + fear_feel:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))


# extract the word features out from the training data
word_features = get_word_features(\
                    get_words_in_tweets(tweets))


# get the training set and train the Naive Bayes Classifier
training_set = nltk.classify.util.apply_features(extract_features, tweets)
classifier = NaiveBayesClassifier.train(training_set)


tweet = 'Ketika saya mendapatkan kabar penculikan balita di Jakarta.'
#print(extract_features(tweet.split()))
sentiment = classifier.classify(extract_features(tweet.split()))
print(sentiment)