"""
main.py

Resume Screening and Ranking System
"""

import os

from src.parser import ResumeParser
from src.preprocess import TextPreprocessor
from src.feature_extractor import FeatureExtractor
from src.job_description import JobDescriptionProcessor
from src.similarity import SimilarityEngine
from src.ranker import CandidateRanker
from src.output_writer import OutputWriter
from src.report_generator import ReportGenerator

def main():

    print("=" * 60)
    print(" AI Resume Screening & Ranking System ")
    print("=" * 75)

    parser = ResumeParser()
    preprocessor = TextPreprocessor()
    extractor = FeatureExtractor()
    jd_processor = JobDescriptionProcessor()
    similarity_engine = SimilarityEngine()
    ranker = CandidateRanker()
    writer = OutputWriter()
    report_generator = ReportGenerator()

    resume_folder = "data/resumes"
    jd_file = "data/job_description/jd.txt"

    if not os.path.exists(jd_file):
        print("Job Description not found.")
        return

    with open(jd_file, "r", encoding="utf-8") as file:
        jd_text = file.read()

    jd_text = preprocessor.clean_text(jd_text)

    jd_features = jd_processor.process(jd_text)

    print("✅ Job Description Loaded Successfully.\n")

    candidates = []

    files = [
        file for file in os.listdir(resume_folder)
        if file.endswith((".pdf", ".docx", ".txt"))
    ]

    print(f"Found {len(files)} resumes.\n")

    for file in files:

        print("=" * 50)
        print(f"Processing : {file}")

        file_path = os.path.join(resume_folder, file)

        try:

            resume_text = parser.extract_text(file_path)

            resume_text = preprocessor.clean_text(resume_text)

            resume_features = extractor.extract_features(resume_text)

            similarity = similarity_engine.compute_similarity(
                resume_features,
                jd_features
            )

            candidate = {
                "candidate": file,
                "skills_score": similarity["skills_score"],
                "education_score": similarity["education_score"],
                "experience_score": similarity["experience_score"],
                "project_score": similarity["project_score"],
                "certification_score": similarity["certification_score"],
                "score": similarity["final_score"]
            }

            candidates.append(candidate)

            print("✓ Resume Processed Successfully")

        except Exception as e:

            print(f"Error : {e}")

    ranked = ranker.rank_candidates(candidates)

    final_candidates = []

    for candidate in ranked:
        final_candidates.append(
            report_generator.generate_report(candidate)
        )

    ranked = final_candidates

    print("\n")
    print("=" * 60)
    print("FINAL RANKING")
    print("=" * 60)

    for i, candidate in enumerate(ranked, start=1):

        
            print(f"{i}. {candidate['candidate']}")
            print(f"   Overall Score      : {candidate['overall_score']:.2f}%")
            print(f"   Skills Score       : {candidate['skills_score']:.2f}%")
            print(f"   Education Score    : {candidate['education_score']:.2f}%")
            print(f"   Experience Score   : {candidate['experience_score']:.2f}%")
            print(f"   Project Score      : {candidate['project_score']:.2f}%")
            print(f"   Certification Score: {candidate['certification_score']:.2f}%")
            print(f"   Recommendation     : {candidate['recommendation']}")
            print("-" * 60)
                    

    writer.save_csv(ranked)

    writer.save_json(ranked)

    print("\nResults saved successfully.")


if __name__ == "__main__":
    main()