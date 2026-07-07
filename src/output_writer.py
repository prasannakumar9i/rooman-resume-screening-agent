import os
import json
import csv
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional

# Configure modular logging telemetry
logger = logging.getLogger(__name__)

class OutputWriter:
    """
    Upgraded output writer component responsible for persisting candidate evaluation
    telemetry matrix payloads into structured CSV and JSON formats. Generates dual
    production files (static for frontend alignment and timestamped for historical archiving).
    """
    def __init__(self):
        # Default target paths ensuring seamless backward compatibility with V1 scripts
        self.default_csv_path = "output/ranked_candidates.csv"
        self.default_json_path = "output/ranked_candidates.json"

    def _ensure_directory(self, path: str) -> None:
        """
        Validates target directories exist on the filesystem layer, spawning them if missing.
        """
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            logger.info(f"Automatically spawned missing output repository structural node: {directory}")

    def _generate_timestamped_path(self, base_path: str) -> str:
        """
        Injects standard normalized chronological tracking stamps into active write names.
        """
        directory, filename = os.path.split(base_path)
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(directory, f"{name}_{timestamp}{ext}")

    def save_json(self, data: Any, base_path: Optional[str] = None) -> str:
        """
        Saves nested structured report models as standard json nodes. Writes both a fixed-name 
        file for live application binding and a timestamped clone for system logs.
        """
        primary_path = base_path if base_path else self.default_json_path
        
        
        try:
            # Commit primary fallback configuration file node
            self._ensure_directory(primary_path)
            with open(primary_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            logger.info(f"Committed primary static JSON schema node for frontend access: {primary_path}")

            
            return primary_path
        except Exception as e:
            logger.error(f"Write execution barrier encountered serialization JSON block to {primary_path}: {str(e)}")
            return ""

    def save_csv(self, data: Any, base_path: Optional[str] = None) -> str:
        """
        Flattens dynamic screening data arrays into tabular formats, supporting dual mapping 
        for 'candidate' and 'candidate_name' properties across version scopes.
        """
        primary_path = base_path if base_path else self.default_csv_path
    
        # Re-map single dictionary elements safely into iterative arrays
        reports: List[Dict[str, Any]] = []
        if isinstance(data, dict):
            reports = [data]
        elif isinstance(data, list):
            reports = data
        else:
            logger.warning("Unrecognized raw data input routed to CSV serialization node. Skipping execution.")
            return ""

        if not reports:
            logger.warning("Empty candidate array parameter routed to CSV serialization node. Skipping execution.")
            return ""

        # Comprehensive header field mapping rules aligning both system versions seamlessly
        headers = [
            "candidate",
            "candidate_name",
            "overall_score",
            "match_percentage",
            "skills_score",
            "experience_score",
            "education_score",
            "project_score",
            "certification_score",
            "resume_completeness",
            "confidence_score",
            "matched_skills",
            "missing_skills",
            "strengths",
            "areas_for_improvement",
            "recommendation"
        ]

        try:
            self._ensure_directory(primary_path)
            
            # Sub-routine executing standard row normalization structures across data layers
            normalized_reports = []
            for report in reports:
                # Capture polymorphic user properties to defend downstream layout reads
                c_val = report.get("candidate", report.get("candidate_name", "Unknown Candidate"))
                cn_val = report.get("candidate_name", report.get("candidate", "Unknown Candidate"))
                
                norm_row = {k: report.get(k, "") for k in headers}
                norm_row["candidate"] = c_val
                norm_row["candidate_name"] = cn_val
                
                # Cross-map properties to cover project vs project tracking fields
                if "project_score" not in norm_row or norm_row["project_score"] == "":
                    norm_row["project_score"] = report.get("project_score", report.get("projects_score", 0.0))
                if "certification_score" not in norm_row or norm_row["certification_score"] == "":
                    norm_row["certification_score"] = report.get("certification_score", report.get("certifications_score", 0.0))
                    
                normalized_reports.append(norm_row)

            # Write primary clean configuration file system link
            with open(primary_path, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(normalized_reports)
            logger.info(f"Committed primary flat-file CSV table layer: {primary_path}")


            return primary_path
        except Exception as e:
            logger.error(f"Write execution barrier encountered serialization CSV data arrays to {primary_path}: {str(e)}")
            return ""