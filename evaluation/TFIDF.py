# TFIDF class extends Evaluator class to evaluate accuracy of Term Frequency, Inverse Document Frequency with cosine similarity

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Import local libraries
import sys
sys.path.append('../src')

import processing
from Evaluator import Evaluator

class TFIDF(Evaluator):
    bow_transformer = ''
    tfidf_transformer = ''
    
    def vectorize(self):
        """Returns vectors of transformed corpus, using Bag of Words and Term Frequency/Inverse Document Frequency."""
        # Create BOW tranformer based on faq.question + faq.answer
        self.bow_transformer = CountVectorizer(analyzer=processing.text_process).fit(self.corpus)
        # Tranform faq.question itself into BOW
        corpus_bow = self.bow_transformer.transform(self.corpus)

        # Create TFIDF transformer based on faq.question's BOW
        self.tfidf_transformer = TfidfTransformer().fit(corpus_bow)
        # Transform faq.question's BOW into TFIDF and return    
        return self.tfidf_transformer.transform(corpus_bow)

    def max_similarity(self, query):
        """Returns (index, similarity value) of string argument q's most similar match in FAQ, determined by cosine similarity."""
        # Transform test question into BOW using BOW transformer (based on faq.question) 
        query_bow = self.bow_transformer.transform([query])
        # Transform test question's BOW into TFIDF
        query_tfidf = self.tfidf_transformer.transform(query_bow)

        sims = np.transpose(cosine_similarity(query_tfidf, self.vectors))

        max_similarity = sims.max()
        max_index = np.argmax(sims)

        return max_index, max_similarity

  

    