import numpy as np
from typing import Dict
from sentence_transformers import SentenceTransformer

class SimilarityEngine:
    """
    Upgraded similarity engine that utilizes all-MiniLM-L6-v2 transformers to compute 
    independent cosine similarity matching arrays across structural context blocks.
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        # Initialize the Sentence Transformer model once on initialization
        self.model = SentenceTransformer(model_name)
        
        # Exact requested modular score weights ensuring clean mathematical scaling
        self.weights = {
            "skills": 0.45,
            "experience": 0.25,
            "education": 0.15,
            "projects": 0.10,
            "certifications": 0.05
        }

    def _cosine_similarity(self, vec_a: np.ndarray, vec_b: np.ndarray) -> float:
        """
        Computes the standard cosine similarity angle between two vector distributions.
        """
        norm_a = np.linalg.norm(vec_a)
        norm_b = np.linalg.norm(vec_b)
        
        if norm_a == 0 or norm_b == 0:
            return 0.0
            
        return float(np.dot(vec_a, vec_b) / (norm_a * norm_b))

    def compute_scores(self, resume_sections: Dict[str, str], jd_sections: Dict[str, str]) -> Dict[str, float]:
        """
        Calculates distinct embeddings and cross-similarity sub-scores for each matching profile section,
        scaling them into a weighted overall score matrix.
        
        Args:
            resume_sections (Dict[str, str]): Mapped structural blocks from the candidate resume.
            jd_sections (Dict[str, str]): Mapped structural blocks from the target Job Description.
            
        Returns:
            Dict[str, float]: Calculated sub-scores and overall similarity summary.
        """
        scores = {}
        overall_score = 0.0

        for section, weight in self.weights.items():
            res_text = resume_sections.get(section, "").strip()
            jd_text = jd_sections.get(section, "").strip()

            if len(res_text) < 15 or len(jd_text) < 15:
                score = 0.0
                scores[f"{section}_score"] = 0.0
                continue

            # If both components are empty, assign a balanced neutral zero score
            if not res_text and not jd_text:
                score = 0.0
            # If the job description requires a section but the candidate misses it completely
            elif jd_text and not res_text:
                score = 0.0
            # If the candidate has background documentation but the JD doesn't mandate it explicitly
            elif res_text and not jd_text:
                score = 0.0 # Award partial credit for bonus domain qualifications
            else:
                # Generate localized sentence transformer vector configurations
                embeddings = self.model.encode(
                    [res_text, jd_text],
                    convert_to_numpy=True,
                    normalize_embeddings=True
                )
                score = self._cosine_similarity(embeddings[0], embeddings[1])
                
                # Smooth edge values bounded inside normal percentage matrices
                score = max(0.0, min(1.0, score))

            # Store matching individual percentage metrics (0 - 100)
            scores[f"{section}_score"] = round(score * 100, 2)
            
            # Apply linear scalar matrix translation weights
            overall_score += score * weight

        # Inject final master metrics into response payload register
        scores["overall_score"] = round(overall_score * 100, 2)
        
        return scores