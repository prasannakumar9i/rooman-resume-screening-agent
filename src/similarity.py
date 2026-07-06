"""
similarity.py

Computes semantic similarity between resume
and job description using Sentence Transformers.
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def _score(self, resume_text, jd_text):

        if not resume_text.strip() or not jd_text.strip():
            return 0.0

        emb1 = self.model.encode([resume_text])

        emb2 = self.model.encode([jd_text])

        score = cosine_similarity(
            emb1,
            emb2
        )[0][0]

        return float(round(score * 100, 2))

    def compute_similarity(
        self,
        resume_features,
        jd_features
    ):

        skills_score = self._score(
            " ".join(resume_features["skills"]),
            " ".join(jd_features["skills"])
        )

        education_score = self._score(
            " ".join(resume_features["education"]),
            " ".join(jd_features["education"])
        )

        experience_score = self._score(
            " ".join(resume_features["experience"]),
            " ".join(jd_features["experience"])
        )

        project_score = self._score(
            " ".join(resume_features.get("projects", [])),
            ""
        )

        certification_score = self._score(
            " ".join(resume_features.get("certifications", [])),
            ""
        )

        final_score = (

            skills_score * 0.45 +

            experience_score * 0.25 +

            education_score * 0.15 +

            project_score * 0.10 +

            certification_score * 0.05

        )

        return {

            "skills_score": round(skills_score, 2),

            "education_score": round(
                education_score,
                2
            ),

            "experience_score": round(
                experience_score,
                2
            ),

            "project_score": round(
                project_score,
                2
            ),

            "certification_score": round(
                certification_score,
                2
            ),

            "final_score": round(
                final_score,
                2
            )

        }