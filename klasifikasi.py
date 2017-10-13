import nltk
import sqlite3
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


def read_tweets(t_type):
    tweets = []

    conn = sqlite3.connect('dataset/nrc/asli/sinonim/translate/'+ t_type + '.db')
    c = conn.cursor()
    for row in c.execute('SELECT data_komen FROM dataku'):
        tweets.append([row[0], t_type])
    conn.close()

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


# read in postive and negative training tweets
joy_feel = read_tweets('joy')
disgust_feel = read_tweets('disgust')
sadness_feel = read_tweets('sadness')
anger_feel = read_tweets('anger')
surprise_feel = read_tweets('surprise')
fear_feel = read_tweets('fear')


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