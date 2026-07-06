"""
ranker.py

Ranks candidates based on overall score.
"""


class CandidateRanker:

    def rank_candidates(self, candidates):

        ranked = sorted(
            candidates,
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked