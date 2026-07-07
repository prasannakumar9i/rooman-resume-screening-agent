import logging
from typing import Dict
from src.preprocess import TextPreprocessor
from src.feature_extractor import FeatureExtractor

# Setup modular logger
logger = logging.getLogger(__name__)

class JobDescriptionProcessor:
    """
    Upgraded processor that leverages the structural FeatureExtractor to segment 
    arbitrary Job Descriptions into semantic sections dynamically without domain keywords.
    """
    def __init__(self):
        # Initialize internal processing and extraction sub-modules
        self.preprocessor = TextPreprocessor()
        self.feature_extractor = FeatureExtractor()

    def process(self, raw_jd_text: str) -> Dict[str, str]:
        """
        Cleans and segments incoming job descriptions into structured text sections
        to prepare them for vector embedding comparison loops.
        
        Args:
            raw_jd_text (str): Raw string content of the uploaded Job Description.
            
        Returns:
            Dict[str, str]: Structured sections compatible with SemanticSimilarityEngine.
        """
        # Baseline structural optimization guardrail
        if not raw_jd_text or not raw_jd_text.strip():
            logger.warning("Empty or null Job Description text provided to processor.")
            return {
                "skills": "",
                "experience": "",
                "projects": "",
                "education": "",
                "certifications": ""
            }

        try:
            # 1. Direct preprocessing text normalization
            cleaned_text = self.preprocessor.clean_text(raw_jd_text)

            # 2. Extract structural features dynamically using the upgraded FeatureExtractor
            extracted_sections = self.feature_extractor.extract_features(cleaned_text)
            
            logger.info("Successfully executed semantic partitioning on target Job Description.")
            return extracted_sections

        except Exception as e:
            logger.error(f"Execution failure during Job Description processing phase: {str(e)}")
            # Return clean empty structures to prevent downstream pipeline crashes
            return {
                "summary": "",
                "skills": "",
                "experience": "",
                "projects": "",
                "education": "",
                "certifications": "",
                "other": ""
            }