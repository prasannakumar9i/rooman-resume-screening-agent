import re
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class ReportGenerator:
    """
    Upgraded report generator that builds highly structured talent telemetry profiles
    using a multi-tier recommendation engine and enriched scoring data points.
    """
    def __init__(self):
        pass

    def _determine_tier(self, score: float) -> str:
        """
        Assigns candidate recommendation categories based on the 2026 screening scale.
        """
        if score >= 90.0:
            return "Highly Recommended"
        elif score >= 80.0:
            return "Recommended"
        elif score >= 70.0:
            return "Good Match"
        elif score >= 60.0:
            return "Average Match"
        else:
            return "Low Match"

    def _extract_skills_tokens(self, text: str) -> List[str]:
        """
        Extract only technical skills from the text.
        """

        if not text:
            return []

        # List of supported technologies
        technical_skills = {
            "python","java","c","c++","c#","javascript","typescript",
            "html","css","react","next.js","node.js","express",
            "flask","fastapi","django","sql","mysql","postgresql",
            "mongodb","oracle","firebase",

            "machine learning","deep learning","artificial intelligence",
            "nlp","computer vision","generative ai","llm",
            "rag","langchain","chromadb","faiss",
            "sentence transformers","huggingface","tensorflow",
            "keras","pytorch","opencv","scikit-learn",
            "pandas","numpy","matplotlib","seaborn",

            "aws","azure","gcp","docker","kubernetes",
            "linux","git","github","streamlit",
            "power bi","tableau","excel"
        }

        text = text.lower()

        found = []

        for skill in technical_skills:
            if skill in text:
                found.append(skill)

        return sorted(set(found))

    def _calculate_completeness(self, resume_sections: Dict[str, str]) -> float:
        """
        Evaluates structural integrity based on populated vs expected profile blocks.
        """
        total_sections = len(resume_sections)
        if total_sections == 0:
            return 0.0
        populated = sum(1 for text in resume_sections.values() if text and text.strip())
        return round((populated / total_sections) * 100, 2)

    def _calculate_confidence(self, scores: Dict[str, float], completeness: float) -> float:
        """
        Derives an operational analytics calculation reflecting parsing alignment factors.
        """
        # Base confidence calculation combining completeness density and target skills scores
        skills_weight = scores.get("skills_score", 0.0) * 0.6
        completeness_weight = completeness * 0.4
        return round(skills_weight + completeness_weight, 2)

    def _generate_insights(self, scores: Dict[str, float], resume_sections: Dict[str, str], jd_sections: Dict[str, str]) -> Dict[str, Any]:
        """
        Performs diagnostic comparison matrices across section values to generate text reviews.
        """
        resume_skills = set(self._extract_skills_tokens(resume_sections.get("skills", "")))
        jd_skills = set(self._extract_skills_tokens(jd_sections.get("skills", "")))
        
        matched_skills = list(resume_skills.intersection(jd_skills)) if jd_skills else ["N/A"]
        missing_skills = list(jd_skills.difference(resume_skills)) if jd_skills else ["None"]
        
        if not matched_skills and jd_skills: matched_skills = ["None"]
        if not missing_skills: missing_skills = ["None"]

        strengths = []
        improvements = []

        if scores.get("skills_score", 0) >= 75:
            strengths.append("Demonstrates solid semantic alignment with target technical skill requirements.")
        else:
            improvements.append("Technical skill context exhibits low correlation with the core job specifications.")

        if scores.get("experience_score", 0) >= 75:
            strengths.append("Professional work history matches background expectations exceptionally well.")
        else:
            improvements.append("Employment chronological narratives could show deeper domain alignment.")

        if scores.get("project_score", scores.get("projects_score", 0.0)) >= 70:
            strengths.append("Project portfolios strongly validate execution capabilities.")
        else:
            improvements.append("Could enrich active project contexts to reflect missing technology stacks.")

        if not strengths: strengths = ["Broad general background matching base criteria."]
        if not improvements: improvements = ["Continue refining background descriptions against target benchmarks."]

        return {
            "matched_skills": matched_skills[:12],
            "missing_skills": missing_skills[:12],
            "strengths": strengths,
            "improvements": improvements
        }

    def generate_report(self, candidate_name: str, scores: Dict[str, float], resume_sections: Dict[str, str], jd_sections: Dict[str, str]) -> Dict[str, Any]:
        """
        Main interface function to construct the dynamic screening reports.
        
        Args:
            candidate_name (str): Identifier string of the candidate.
            scores (Dict[str, float]): Output score matrix from SemanticSimilarityEngine.
            resume_sections (Dict[str, str]): Section contexts from parsed resume.
            jd_sections (Dict[str, str]): Section contexts from job description.
            
        Returns:
            Dict[str, Any]: Consolidated talent analysis telemetry bundle.
        """
        try:
            overall_score = scores.get("overall_score", 0.0)
            recommendation = self._determine_tier(overall_score)
            
            # Map standard analytics data points
            insights = self._generate_insights(scores, resume_sections, jd_sections)
            resume_completeness = self._calculate_completeness(resume_sections)
            confidence_score = self._calculate_confidence(scores, resume_completeness)

            report = {
                "candidate_name": candidate_name,
                "overall_score": overall_score,
                "match_percentage": overall_score,  # Semantic tracking matches overall vector weight
                "skills_score": scores.get("skills_score", 0.0),
                "experience_score": scores.get("experience_score", 0.0),
                "education_score": scores.get("education_score", 0.0),
                "project_score": scores.get("project_score", scores.get("projects_score", 0.0)),
                "certification_score": scores.get("certification_score", scores.get("certifications_score", 0.0)),
                "resume_completeness": resume_completeness,
                "confidence_score": confidence_score,
                "priority_rank": 1,  # Calculated and reassigned dynamically within main/ranker sorting loops
                "matched_skills": ", ".join(insights["matched_skills"]),
                "missing_skills": ", ".join(insights["missing_skills"]),
                "strengths": " ".join(insights["strengths"]),
                "areas_for_improvement": " ".join(insights["improvements"]),
                "recommendation": recommendation
            }
            
            logger.info(f"Successfully generated dynamic report metrics array for {candidate_name}.")
            return report

        except Exception as e:
            logger.error(f"Failed to generate candidate report metrics: {str(e)}")
            return {
                "candidate_name": candidate_name,
                "overall_score": scores.get("overall_score", 0.0),
                "match_percentage": scores.get("overall_score", 0.0),
                "skills_score": scores.get("skills_score", 0.0),
                "experience_score": scores.get("experience_score", 0.0),
                "education_score": scores.get("education_score", 0.0),
                "project_score": scores.get("project_score", 0.0),
                "certification_score": scores.get("certification_score", 0.0),
                "resume_completeness": 0.0,
                "confidence_score": 0.0,
                "priority_rank": 99,
                "matched_skills": "Error loading records",
                "missing_skills": "Error loading records",
                "strengths": "Metrics unavailable.",
                "areas_for_improvement": "Metrics unavailable.",
                "recommendation": "Review Needed"
            }