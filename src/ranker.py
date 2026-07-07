"""
ranker.py

Ranks candidates based on overall score.
"""


class CandidateRanker:

    def rank_candidates(self, candidates):

        ranked = sorted(
            candidates,
            key=lambda x: x.get("overall_score", 0),
            reverse=True
        )

        return ranked