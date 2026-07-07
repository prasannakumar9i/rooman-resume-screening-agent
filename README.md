# 🚀 AI Resume Screening & Ranking System (ATS v2)

An AI-powered Applicant Tracking System (ATS) that automatically parses resumes, extracts structured candidate information, compares resumes with a Job Description using **Natural Language Processing (NLP)** and **Sentence Transformers**, and ranks candidates based on semantic similarity scores.

Unlike traditional keyword-based ATS systems, this project understands the semantic meaning of resumes, enabling more accurate candidate ranking and recommendation.

---

# 🎯 Project Objective

The objective of this project is to automate the initial resume screening process by analyzing candidate resumes, extracting key information, comparing them against a job description, and ranking candidates based on their suitability.

This helps recruiters reduce manual effort, improve candidate shortlisting, and quickly identify the most relevant applicants.

---

# ✨ Features

## 📄 Resume Parsing

- PDF Resume Parsing (PyMuPDF)
- DOCX Resume Parsing
- TXT Resume Parsing
- OCR Support for scanned PDFs (Tesseract OCR + pdf2image)

---

## 🧹 Text Preprocessing

- Text normalization
- Resume cleaning
- Noise removal
- Technical keyword preservation
- Bullet and formatting cleanup

---

## 🧠 Intelligent Feature Extraction

Automatically extracts:

- Technical Skills
- Work Experience
- Education
- Projects
- Certifications

Supports multiple resume formats using dynamic section detection.

---

## 📑 Job Description Processing

Automatically extracts and structures:

- Required Skills
- Experience
- Education
- Projects
- Certifications

---

## 🤖 Semantic Resume Matching

Uses **Sentence Transformers (all-MiniLM-L6-v2)** to perform semantic comparison between resumes and job descriptions instead of simple keyword matching.

---

## 📊 Candidate Ranking

Automatically ranks candidates using:

- Overall ATS Score
- Section-wise Similarity Scores
- Resume Completeness
- Confidence Score
- Recommendation Tier

---

## 📈 Report Generation

Generates detailed candidate reports including:

- Overall Match Score
- Skills Score
- Experience Score
- Education Score
- Project Score
- Certification Score
- Resume Completeness
- Confidence Score
- Matched Skills
- Missing Skills
- Recommendation

---

## 📁 Output Generation

Automatically exports results into:

- CSV Report
- JSON Report
- Execution Log

---

# 🏗 Project Architecture

```text
                        Job Description
                               │
                               ▼
                  Job Description Processor
                               │
                               ▼
                     Feature Extraction
                               │
──────────────────────────────────────────────────────────────
                         Resume Folder
                               │
                               ▼
                         Resume Parser
                               │
                               ▼
                     Text Preprocessing
                               │
                               ▼
                     Feature Extraction
                               │
                               ▼
            Sentence Transformer Embeddings
                               │
                               ▼
                  Cosine Similarity Engine
                               │
                               ▼
                     Candidate Ranking
                               │
                               ▼
               Report Generator (CSV / JSON)
```

---

# 📂 Project Structure

```text
rooman-resume-screening-agent/

│
├── data/
│   ├── resumes/
│   └── job_description/
│       └── jd.txt
│
├── output/
│   ├── ranked_candidates.csv
│   ├── ranked_candidates.json
│   └── ats_pipeline.log
│
├── src/
│   ├── parser.py
│   ├── preprocess.py
│   ├── feature_extractor.py
│   ├── job_description.py
│   ├── similarity.py
│   ├── ranker.py
│   ├── report_generator.py
│   └── output_writer.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

| Category | Technology |
|-----------|------------|
| Language | Python |
| NLP | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| PDF Parsing | PyMuPDF |
| OCR | Tesseract OCR |
| Image Processing | pdf2image |
| Word Parsing | python-docx |
| Numerical Computing | NumPy |
| Output | CSV, JSON |
| Logging | Python Logging |

---

# 🔄 Workflow

```text
Resume
   │
   ▼
Resume Parser
   │
   ▼
Text Preprocessing
   │
   ▼
Feature Extraction
   │
   ▼
Job Description Processing
   │
   ▼
Sentence Embedding
   │
   ▼
Cosine Similarity
   │
   ▼
Candidate Ranking
   │
   ▼
Recommendation Generation
   │
   ▼
CSV / JSON Reports
```

---

# 🧠 Feature Extraction

The system extracts the following resume sections automatically:

- Technical Skills
- Experience
- Education
- Projects
- Certifications

---

# 📊 Candidate Scoring Strategy

The final ATS score is calculated using weighted semantic similarity.

| Section | Weight |
|----------|---------|
| Skills | **45%** |
| Experience | **25%** |
| Education | **15%** |
| Projects | **10%** |
| Certifications | **5%** |

---

# ▶️ Installation

```bash
git clone https://github.com/prasannakumar9i/rooman-resume-screening-agent.git

cd rooman-resume-screening-agent

pip install -r requirements.txt
```

---

# ▶️ Usage

Place resumes inside:

```text
data/resumes/
```

Place the Job Description inside:

```text
data/job_description/jd.txt
```

Run the application:

```bash
python main.py
```

---

# 📊 Sample Console Output

```text
========================================================
AI Resume Screening & Ranking System
========================================================

Job Description Loaded Successfully.

Found 5 resumes.

Processing Resume : resume_test.txt

✓ Resume Parsed Successfully
✓ Feature Extraction Completed
✓ Semantic Similarity Computed
✓ Candidate Ranked

========================================================

FINAL RANKING

1. John_Doe.pdf

Overall Score : 91.97%

Recommendation : Highly Recommended
```

---

# 📁 Generated Output

After execution, the following files are automatically generated:

```text
output/

├── ranked_candidates.csv
├── ranked_candidates.json
└── ats_pipeline.log
```

---

# ⚖️ Design Trade-offs

## Advantages

- Modular architecture
- Semantic similarity instead of keyword matching
- OCR support for scanned resumes
- Structured JSON & CSV reports
- Easily extendable
- Lightweight backend-only implementation
- Clean logging and pipeline execution

## Current Limitations

- Rule-based section extraction
- Single Job Description processing
- No web interface (backend only)
- OCR increases execution time for scanned PDFs

---

# 🚀 Future Improvements

- Large Language Model (LLM) based resume understanding
- Named Entity Recognition (NER)
- Skill ontology matching
- Multi-job comparison
- Explainable AI scoring
- REST API
- Recruiter Dashboard
- Cloud Deployment
- Docker Support
- Authentication & Role Management

---

# 👨‍💻 Author

**Prasanna Kumar**

Computer Science Engineer

**Skills:** AI • Machine Learning • NLP • Computer Vision • Generative AI • Python

---

## ⭐ If you found this project useful, consider giving it a Star!