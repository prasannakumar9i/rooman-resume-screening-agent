"""
report_generator.py

Generates candidate reports.
"""


class ReportGenerator:

    def generate_report(self, candidate):

        score = candidate["score"]

        if score >= 90:
            recommendation = "Highly Recommended"

        elif score >= 75:
            recommendation = "Recommended"

        elif score >= 60:
            recommendation = "Consider"

        else:
            recommendation = "Not Recommended"

        report = {

            "candidate": candidate["candidate"],

            "overall_score": round(candidate["score"], 2),

            "skills_score": round(
                candidate["skills_score"],
                2
            ),

            "education_score": round(
                candidate["education_score"],
                2
            ),

            "experience_score": round(
                candidate["experience_score"],
                2
            ),

            "project_score": round(
                candidate.get(
                    "project_score",
                    0
                ),
                2
            ),

            "certification_score": round(
                candidate.get(
                    "certification_score",
                    0
                ),
                2
            ),

            "recommendation": recommendation

        }

        return report