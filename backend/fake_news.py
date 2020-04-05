import pandas
import re
import numpy as np

from stop_words import get_stop_words
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import cross_val_score, KFold
import sys
from nltk.tokenize import word_tokenize
import string

from sklearn.preprocessing import normalize
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn import preprocessing


class FakeNewsDetection:

    def __init__(self, dataset_file, algorithm="nne"):
        self.algorithm = algorithm
        self.data = pandas.read_csv(dataset_file, usecols=['Origin', 'Statement', 'Label'], encoding= 'unicode_escape', engine='python', index_col=None)

        print(self.data.shape)
        self.swe = get_stop_words('english')
        self.model = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.vectorizer = None
        self.count_vect = None
        self.scaler = MaxAbsScaler()

    def clean(self, txt):
        tokens = word_tokenize(txt)
        # convert to lower case
        tokens = [w.lower() for w in tokens]
        # remove punctuation from each word
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]
        # filter out stop words
        words = [w for w in words if not w in self.swe]
        return " ".join(words)

    def clean_str(self, s):
        if not s or s == "":
            return None
        s = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", s)
        s = re.sub(r"\'ve", " \'ve", s)
        # s = re.sub(r"n\'t", " n\'t", s)
        s = re.sub(r"haven\'t", "have not", s)
        s = re.sub(r"hasn\'t", "has not", s)
        s = re.sub(r"hadn\'t", "had not", s)
        s = re.sub(r"isn\'t", "is not", s)
        s = re.sub(r"aren\'t", "are not", s)
        s = re.sub(r"wasn\'t", "was not", s)
        s = re.sub(r"weren\'t", "were not", s)
        s = re.sub(r"don\'t", "do not", s)
        s = re.sub(r"doesn\'t", "does not", s)
        # s = re.sub(r"\'re", " \'re", s)
        s = re.sub(r"\'re", " are", s)
        s = re.sub(r" he\'s", " he is", s)
        s = re.sub(r" she\'s", " she is", s)
        s = re.sub(r" it\'s", " it is", s)
        # s = re.sub(r"\'d", " \'d", s)
        s = re.sub(r"\'d", " would", s)
        # s = re.sub(r"\'ll", " \'ll", s)
        s = re.sub(r"\'ll", " will", s)
        s = re.sub(r",", " , ", s)
        s = re.sub(r"!", " ! ", s)
        s = re.sub(r"\(", " ( ", s)
        s = re.sub(r"\)", " ) ", s)
        s = re.sub(r"\?", " ? ", s)
        s = re.sub(r"\s{2,}", " ", s)
        # s = re.sub(r"\'s", " \'s", s)
        s = re.sub(r"\'", "`", s)
        s = re.sub(r"\n", " ", s)
        return s.strip().lower() if s.strip().lower() else " "

    def norm(self, values, method="l2", phase="train"):
        if method == "l2":
            return normalize(values, axis=1, norm='l2')
        elif method == "l1":
            return normalize(values, axis=1, norm='l1')
        elif method == "mm":
            if phase == "train":
                self.scaler.fit(values)
            return self.scaler.transform(values)
        else:
            return values

    def pre_process(self):
        print("Running the pre_processing phase...")

        self.data["all_features"] = self.data["Origin"].fillna(' ') + " " + self.data["Statement"].fillna(' ')
        self.data["all_features"] = self.data["all_features"].apply(self.clean)
        self.data["all_features"] = self.data["all_features"].apply(self.clean_str)
        self.data.dropna(subset=['all_features'], inplace=True)
        self.data.dropna(how='all', inplace=True)
        print(self.data.shape, file=sys.stderr)
        self.data["class"] = self.data["Label"].map({"Real": 0, "Fake": 1})
        print(self.data.shape, file=sys.stderr)

        self.X_train = self.data["all_features"]
        self.y_train = list(self.data["class"].values)
        print(self.y_train, file=sys.stderr)
    def vectorize_train(self):
        print("Text transformation (vectorizer) of train data for model : {}".format(self.algorithm))

        self.vectorizer = TfidfVectorizer(min_df=2, max_features=2000, strip_accents='unicode',
                                           tokenizer=word_tokenize, stop_words=self.swe,
                                           analyzer='word', ngram_range=(1, 4),
                                           use_idf=1, smooth_idf=1, sublinear_tf=1
                                           ).fit(self.X_train)
        tf_idf_data = self.vectorizer.fit_transform(self.X_train)
        print(tf_idf_data.shape, file=sys.stderr)
        return self.norm(tf_idf_data, "mm")

    def vectorize_test(self):
        #print("Text transformation (vectorizer) of test data")
        return self.norm(self.vectorizer.transform(self.X_test), "mm", "test")

    def train_model(self, x):
        print("Running the training phase..")
        if self.algorithm == "logistic":
            self.model = LogisticRegression()
        elif self.algorithm == "svm":
            self.model = svm.SVC(kernel="linear", probability=True)
        elif self.algorithm == "multiNB":
            self.model = MultinomialNB()
        elif self.algorithm == "linear":
            mod = linear_model.SGDClassifier(loss='hinge')
            self.model = CalibratedClassifierCV(mod, cv=5, method='sigmoid')
        elif self.algorithm == "forest":
            self.model = RandomForestClassifier(n_estimators=100)
        elif self.algorithm == "nne":
            self.model = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(30, 30, 30), random_state=7)
        else:
            self.model = LogisticRegression()
        print('teststastas', file=sys.stderr)
        print(x.shape, file=sys.stderr)
        #x.to_csv("test1.csv", sep="|", index=False)
        scores = cross_val_score(self.model, x, self.y_train, cv=10)
        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean() * 100.0, scores.std() * 2), file=sys.stderr)
        self.model.fit(x, self.y_train)

    def get_probability(self, prob1, prob2):
        return prob1 if prob1 > prob2 else prob2

    def predict(self, x_input):
        #print("Trying to predict a class..")
        self.X_test = x_input
        X_test_tfidf = self.vectorize_test()

        prediction_rbf = self.model.predict(X_test_tfidf)
        print(prediction_rbf, file=sys.stderr)
        prediction = "False" if prediction_rbf[0] == 1 else "Real"
        model_classes = list(self.model.classes_)
        prob = list(self.model.predict_proba(X_test_tfidf)[0])
        out = {"prediction": prediction,
               "class": int(list(prediction_rbf)[0]),
               "classes": [int(model_classes[0]), int(model_classes[1])],
               "prob": [float(prob[0]), float(prob[1])],
               "probability": self.get_probability(prob[0], prob[1])
               }

        return out

    def initialize(self):
        self.pre_process()
        x_transformed = self.vectorize_train()
        print('training', file=sys.stderr)
        print(x_transformed.shape, file=sys.stderr)
        #np.where(x_transformed.values >= np.finfo(np.float64).max)
        #np.savetxt("test.csv", x_transformed, delimiter="|")
        print(type(x_transformed), file=sys.stderr)
        print(x_transformed.shape, file=sys.stderr)
        self.train_model(x_transformed)



