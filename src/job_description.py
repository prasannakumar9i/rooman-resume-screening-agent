"""
job_description.py

Processes a Job Description and extracts
structured information for comparison.
"""

from src.feature_extractor import FeatureExtractor
from src.preprocess import TextPreprocessor


class JobDescriptionProcessor:

    def __init__(self):

        self.preprocessor = TextPreprocessor()

        self.extractor = FeatureExtractor()

    def process(self, jd_text):

        jd_text = self.preprocessor.clean_text(jd_text)

        features = self.extractor.extract_features(
            jd_text
        )

        return features