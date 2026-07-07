import os
import time
import logging
from typing import List, Dict, Any

# Ensure backward compatible imports match the exact file architecture definitions
from src.parser import ResumeParser
from src.preprocess import TextPreprocessor
from src.feature_extractor import FeatureExtractor
from src.job_description import JobDescriptionProcessor
from src.similarity import SimilarityEngine
from src.ranker import CandidateRanker
from src.report_generator import ReportGenerator
from src.output_writer import OutputWriter

# Configure clean production logging telemetry layout
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("output/ats_pipeline.log", mode='a', encoding='utf-8')
    ]
)
logger = logging.getLogger("ATS_Main_Execution")

def main():
    """
    Main pipeline entrypoint running structured document ingestion, cleaning, section 
    segmentation, semantic vector comparison, and telemetry layout writes.
    """
    start_pipeline_time = time.time()
    logger.info("Initializing system processing arrays.")

    # Target static data path nodes matching project constraints
    resumes_dir = "data/resumes/"
    jd_path = "data/job_description/jd.txt"
    
    # Instantiate exact predefined class components
    parser = ResumeParser()
    preprocessor = TextPreprocessor()
    feature_extractor = FeatureExtractor()
    jd_processor = JobDescriptionProcessor()
    similarity_engine = SimilarityEngine()
    ranker = CandidateRanker()
    report_generator = ReportGenerator()
    output_writer = OutputWriter()

    # Create missing sub-directories safely
    os.makedirs("output", exist_ok=True)
    os.makedirs(resumes_dir, exist_ok=True)
    os.makedirs(os.path.dirname(jd_path), exist_ok=True)

    if not os.path.exists(jd_path):
        logger.error(f"Execution halted: Target Job Specification not found at {jd_path}")
        return

    # Ingest and segment target Job Description reference vectors
    try:
        raw_jd_text = parser.extract_text(jd_path)
        jd_sections = jd_processor.process(raw_jd_text)
        print("\n========== JD SECTIONS ==========")
        for key, value in jd_sections.items():
            print(f"\n{key.upper()}:")
            print(value[:300] if value else "EMPTY")
    except Exception as jd_err:
        logger.critical(f"Fatal disruption processing Job Description parameters: {str(jd_err)}")
        return

    unfiltered_reports: List[Dict[str, Any]] = []

    # Filter targets inside tracking directory node
    try:
        resume_files = [f for f in os.listdir(resumes_dir) if os.path.splitext(f)[1].lower() in ['.pdf', '.docx', '.txt']]
    except Exception as dir_err:
        logger.error(f"Directory mapping access barrier on tracking directory: {str(dir_err)}")
        return

    # Process individual candidate repositories systematically
    for filename in resume_files:
        file_path = os.path.join(resumes_dir, filename)
        candidate_name = os.path.splitext(filename)[0]

        print("==================================================")
        print(f"Processing : {filename}")
        print("==================================================")

        try:
            # 1. Parse Layer
            raw_resume_text = parser.extract_text(file_path)
            print("Resume parsed successfully")

            # 2. Preprocess Layer
            cleaned_resume_text = preprocessor.clean_text(raw_resume_text)

            # 3. Segment Layer
            resume_sections = feature_extractor.extract_features(cleaned_resume_text)
            print("\n========== RESUME SECTIONS ==========")
            for key, value in resume_sections.items():
                print(f"\n{key.upper()}:")
                print(value[:300] if value else "EMPTY")
            print("Feature extraction completed")

            # 4. Semantic Engine Layer
            scores = similarity_engine.compute_scores(resume_sections, jd_sections)
            print("Similarity computed")

            # 5. Telemetry Generation Layer
            # Gracefully maps single Candidate or separated components ensuring backward compatibility
            report = report_generator.generate_report(candidate_name, scores, resume_sections, jd_sections)
            
            # Maintain backward compatibility fields fallback rules across components
            report["candidate"] = candidate_name
            report["candidate_name"] = candidate_name
            
            unfiltered_reports.append(report)
            print("Report generated")

        except Exception as candidate_err:
            logger.error(f"Aborted profile pipeline block for candidate file '{filename}': {str(candidate_err)}")
            continue

    if not unfiltered_reports:
        logger.warning("Zero candidate vectors processed. Halting score ranking sequence matrices.")
        return

    # 6. Ranker Layer
    try:
        for report in unfiltered_reports:
            report["score"] = report.get("overall_score", 0.0)
        # Pass list configuration arrays directly matching expected CandidateRanker interfaces
        ranked_reports = ranker.rank_candidates(unfiltered_reports)
    except Exception as rank_err:
        logger.error(f"CandidateRanker signature variation or execution crash. Falling back to internal sorting: {str(rank_err)}")
        ranked_reports = sorted(unfiltered_reports, key=lambda x: x.get("overall_score", 0.0), reverse=True)

    # Output Structured Tabular Telemetry Performance Evaluation Matrix
    print("\n" + "-"*120)
    print(f"{'Rank':<5} | {'Candidate':<15} | {'Overall':<7} | {'Skills':<6} | {'Exp':<6} | {'Edu':<6} | {'Proj':<6} | {'Cert':<6} | {'Conf':<6} | {'Comp':<6} | {'Recommendation':<15}")
    print("-"*120)
    for idx, rep in enumerate(ranked_reports):
        print(
            f"{idx+1:02d}    | "
            f"{rep.get('candidate_name', rep.get('candidate', 'Unknown'))[:15]:<15} | "
            f"{rep.get('overall_score', 0.0):>5.1f}% | "
            f"{rep.get('skills_score', 0.0):>5.1f}% | "
            f"{rep.get('experience_score', 0.0):>5.1f}% | "
            f"{rep.get('education_score', 0.0):>5.1f}% | "
            f"{rep.get('project_score', rep.get('projects_score', 0.0)):>5.1f}% | "
            f"{rep.get('certification_score', rep.get('certifications_score', 0.0)):>5.1f}% | "
            f"{rep.get('confidence_score', 0.0):>5.1f}% | "
            f"{rep.get('resume_completeness', 0.0):>5.1f}% | "
            f"{rep.get('recommendation', 'Review Needed'):<15}"
        )
    print("-"*120 + "\n")

    # 7. Output Writer Layer
    try:
        output_writer.save_json(ranked_reports)
        output_writer.save_csv(ranked_reports)
    except Exception as write_err:
        logger.critical(f"Serialization failed on filesystem write layers: {str(write_err)}")

    # 8. Render ATS Global System Performance Summary Telemetry
    total_time = round(time.time() - start_pipeline_time, 2)
    total_candidates = len(ranked_reports)
    all_scores = [r.get("overall_score", 0.0) for r in ranked_reports]
    
    highest_score = max(all_scores) if all_scores else 0.0
    lowest_score = min(all_scores) if all_scores else 0.0
    avg_score = sum(all_scores) / total_candidates if total_candidates > 0 else 0.0
    
    top_cand_node = ranked_reports[0] if ranked_reports else {}
    top_candidate = top_cand_node.get("candidate_name", top_cand_node.get("candidate", "N/A"))

    print("====================================")
    print("ATS SUMMARY")
    print("====================================")
    print(f"Total Candidates : {total_candidates}")
    print(f"Highest Score    : {highest_score:.1f}%")
    print(f"Lowest Score     : {lowest_score:.1f}%")
    print(f"Average Score    : {avg_score:.1f}%")
    print(f"Top Candidate    : {top_candidate}")
    print(f"Processing Time  : {total_time}s")
    print("====================================\n")

if __name__ == "__main__":
    main()