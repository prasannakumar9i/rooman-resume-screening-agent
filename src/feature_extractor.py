import re
from typing import Dict, List

class FeatureExtractor:
    """
    Upgraded semantic feature extractor that segments profiles using expanded structural header matching,
    heuristic context inference fallbacks for unmapped files, and integrated section text normalization.
    """
    def __init__(self):
        # Problem 1: Vastly expanded section patterns to adapt seamlessly across multiple template styles
        self.section_patterns = {
            "skills": re.compile(
                r"(technical\s+skills|skills|required\s+skills|preferred\s+skills|"
                r"technical\s+competencies|core\s+skills|tech\s+stack|technology\s+stack|"
                r"tools\s*&\s*technologies|programming\s+languages)",
                re.IGNORECASE
            ),
            "experience": re.compile(
                r"(experience|work\s+experience|professional\s+experience|employment|"
                r"employment\s+history|internship|internships|career\s+history|"
                r"professional\s+background|responsibilities|job\s+responsibilities|"
                r"key\s+responsibilities|what\s+you'?ll\s+do|role|roles|duties)",
                re.IGNORECASE
            ),
            "projects": re.compile(
                r"(projects|project\s+experience|portfolio|research|"
                r"case\s+studies|implementations|applications|products)",
                re.IGNORECASE
            ),
            "education": re.compile(
                r"(education|qualification|qualifications|eligibility|"
                r"academic\s+background|degree|minimum\s+qualification)",
                re.IGNORECASE
            ),
            "certifications": re.compile(
                r'^\s*(certifications|certificates|training|achievements|awards|licenses|'
                r'certifications\s+&\s+training|awards\s+&\s+achievements|honors)\s*$', 
                re.IGNORECASE | re.MULTILINE
            )
        }
        
        # Problem 2: Heuristic keyword weight mapping for context fallback inference
        self.fallback_weights = {
            "skills": ["python", "java", "javascript", "c++", "sql", "react", "aws", "docker", "kubernetes", "git", "expert", "proficient", "frameworks", "libraries"],
            "experience": ["managed", "led", "developed", "worked", "responsibility", "company", "team", "inc.", "pvt.", "ltd.", "years", "months", "present", "20"],
            "projects": ["implemented", "built", "designed", "github", "source", "system", "application", "dataset", "accuracy", "model", "engine"],
            "education": ["university", "college", "degree", "bachelor", "master", "b.s.", "m.s.", "b.tech", "m.tech", "ph.d", "gpa", "major", "school"],
            "certifications": ["certified", "certification", "credential", "license", "cleared", "awarded", "prize", "rank", "coursera", "udemy", "hackathon"]
        }

    def extract_features(self, text: str) -> Dict[str, str]:
        """
        Parses text into dynamic structural sections using structural markers,
        falling back to keyword-heuristics if sections remain unpopulated.
        """
        extracted_sections = {k: "" for k in self.section_patterns.keys()}
        
        if not text or not text.strip():
            return extracted_sections

        lines = text.split('\n')
        current_section = None
        section_buffers = {k: [] for k in self.section_patterns.keys()}
        unmapped_lines = []

        # Parse step 1: Process text line-by-line via structural boundary regex matching
        for line in lines:
            cleaned_line = line.strip()

            if not cleaned_line:
                continue

            matched_section = None

            for section_name, pattern in self.section_patterns.items():
                if pattern.search(cleaned_line):
                    print(f"[HEADER FOUND] {section_name} --> {cleaned_line}")
                    matched_section = section_name
                    break

            if matched_section:
                current_section = matched_section
            else:
                if current_section:
                    section_buffers[current_section].append(line)
                else:
                    unmapped_lines.append(line)

        # Assign initial parsed strings
        for section, buffer in section_buffers.items():
            if buffer:
                extracted_sections[section] = "\n".join(buffer)

        # Problem 2 Fallback: Process orphan text regions if sections are structurally missing
        missing_sections = [k for k, v in extracted_sections.items() if not v.strip()]
        if missing_sections and unmapped_lines:
            extracted_sections = self._apply_fallback_inference(unmapped_lines, extracted_sections, missing_sections)

        # Problem 3: Standardize text across all output fields
        for section in extracted_sections.keys():
            extracted_sections[section] = self._normalize_text(extracted_sections[section])

        return extracted_sections

    def _apply_fallback_inference(self, unmapped_lines: List[str], current_sections: Dict[str, str], missing_sections: List[str]) -> Dict[str, str]:
        """
        Infers orphan content classification vectors based on text heuristic token concentrations.
        """
        inference_buffers = {k: [] for k in missing_sections}

        for line in unmapped_lines:
            tokens = re.findall(r'\w+', line.lower())
            if not tokens:
                continue

            # Tabulate score counts for each missing classification structure
            scores = {k: 0 for k in missing_sections}
            for section in missing_sections:
                for token in tokens:
                    if token in self.fallback_weights[section]:
                        scores[section] += 1

            # Append to the highest matching scoring criteria if baseline indicator hits
            best_match = max(scores, key=scores.get)
            if scores[best_match] > 0:
                inference_buffers[best_match].append(line)

        # Merge inferred structures safely back into main dictionary registers
        for section, buffer in inference_buffers.items():
            if buffer:
                current_sections[section] = "\n".join(buffer)

        return current_sections

    def _normalize_text(self, text: str) -> str:
        """
        Problem 3: Standardizes token spacing layout parameters while removing bullet noises.
        """
        if not text:
            return ""

        # Strip standard structural list bullets, check-boxes, icons, and geometric tabs
        text = re.sub(r'^\s*([•▪◦►■○*-]|\d+[\).\s]|\-\-\s*)\s*', ' ', text, flags=re.MULTILINE)
        
        # Replace complex control spaces, tab structures, and vertical breaks with simple spacing
        text = re.sub(r'[\t\r\f\v]+', ' ', text)
        text = re.sub(r' {2,}', ' ', text)
        text = re.sub(r'\n{2,}', '\n', text)
        
        return text.strip()