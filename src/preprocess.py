"""
preprocess.py

This module cleans and preprocesses resume text before
feature extraction and similarity scoring.
"""

import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


class TextPreprocessor:

    def clean_text(self, text):
        """
        Basic text cleaning.
        """

        # Lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r"http\S+|www\S+", "", text)

        # Remove email addresses
        text = re.sub(r"\S+@\S+", "", text)

        # Remove phone numbers
        text = re.sub(r"\+?\d[\d\s\-\(\)]{8,}\d", "", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def tokenize(self, text):
        """
        Tokenize using spaCy.
        """

        doc = nlp(text)

        tokens = [
            token.lemma_
            for token in doc
            if not token.is_stop
            and not token.is_punct
            and not token.is_space
        ]

        return tokens