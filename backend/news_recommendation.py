import pandas as pd
import numpy as np
from collections import defaultdict
from gensim import corpora
from gensim import models
from gensim import similarities
import os

class NewsRecommendation:
    # dataset_file = fakenewsdebunking_scraped_data_EN_FR_v3.xlsx
    def __init__(self, dataset_file):
        self.topics = 4  # k=number of topics, default = 4
        self.data = pd.read_excel(dataset_file)
        self.data = self.data[self.data['Language'] == 'EN']  # Read only English news
        self.dictionary = None
        self.lsi = None
        self.indexFile = None
        self.documents = None
    def pre_process(self):
        print("Running the pre_processing phase...")
        fake_news_debunk = self.data['NewsTitle']
        self.documents = fake_news_debunk.values
        # remove common words and tokenize
        stoplist = set('for a of the and to in'.split())
        texts = [
            [word for word in document.lower().split() if word not in stoplist]
            for document in self.documents
        ]
        # remove words that appear only once
        frequency = defaultdict(int)
        for text in texts:
            for token in text:
                frequency[token] += 1
        texts = [
            [token for token in text if frequency[token] > 1]
            for text in texts
        ]
        self.dictionary = corpora.Dictionary(texts)
        corpus = [self.dictionary.doc2bow(text) for text in texts]
        self.lsi = models.LsiModel(corpus, id2word=self.dictionary, num_topics=self.topics)
        index = similarities.MatrixSimilarity(self.lsi[corpus])  # transform corpus to LSI space and index it
        self.indexFile = os.getcwd() + '/deerwester.index'
        index.save(self.indexFile)
    # doc = query (short plain text fake news)
    def recommend(self, doc):
        vec_bow = self.dictionary.doc2bow(doc.lower().split())
        vec_lsi = self.lsi[vec_bow]  # convert the query to LSI space
        index = similarities.MatrixSimilarity.load(self.indexFile)
        sims = index[vec_lsi]  # perform a similarity query against the corpus
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        newsId = sims[0][0]
        similarity = sims[0][1]
        line = self.data.iloc[newsId,]
        result = {}
        result["title"] = line["NewsTitle"]
        result["explanation"] = line["NewsExplanation"]
        result["url"] = line["NewsURL"]
        result['probability'] = round(float(similarity), 2)
        return result

# filename = "data/fakenewsdebunking_data.xlsx"
# rn = NewsRecommendation(filename)
# rn.pre_process()
# text = "covid is fake"
# result = rn.recommend(text)
# print(result[""])