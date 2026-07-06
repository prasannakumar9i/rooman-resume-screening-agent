# 🚀 AI Resume Screening & Ranking System

An AI-powered Resume Screening and Ranking System that automatically parses resumes, extracts important candidate information, compares resumes with a Job Description using Natural Language Processing (NLP), and ranks candidates using semantic similarity scoring.

---

## 🎯 Project Objective

The objective of this project is to automate the initial resume screening process by analyzing candidate resumes, extracting key information, comparing them against a job description, and ranking candidates based on their suitability.

This helps recruiters reduce manual effort and quickly identify the most relevant candidates.

---

## ✨ Features

- 📄 Resume Parsing (PDF, DOCX, TXT)
- 📝 Job Description Processing
- 🧹 Text Preprocessing using spaCy
- 🧠 NLP-based Resume Matching
- 🤖 Semantic Similarity using Sentence Transformers
- 📊 Candidate Ranking
- 📁 CSV Report Generation
- 📄 JSON Report Generation
- ⭐ Candidate Recommendation System
- 🏗 Modular Architecture

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
              CSV & JSON Report Generator
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
│   └── ranked_candidates.json
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
| NLP | spaCy |
| Semantic Similarity | Sentence Transformers |
| ML Utilities | Scikit-Learn |
| PDF Parsing | PyMuPDF |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Output | CSV, JSON |

---

# 🔄 Workflow

```text
Resume
    │
    ▼
Resume Parser
    │
    ▼
Text Cleaning
    │
    ▼
Feature Extraction
    │
    ▼
Sentence Embedding
    │
    ▼
Similarity Calculation
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

The system extracts the following information from each resume:

- Technical Skills
- Educational Qualification
- Experience
- Projects
- Certifications

---

# 📊 Candidate Scoring Strategy

The final candidate score is calculated using weighted semantic similarity.

| Feature | Weight |
|----------|---------|
| Skills | **45%** |
| Experience | **25%** |
| Education | **15%** |
| Projects | **10%** |
| Certifications | **5%** |

---

# ▶️ Installation

```bash
git clone https://github.com/<your-username>/rooman-resume-screening-agent.git

cd rooman-resume-screening-agent

pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 📊 Sample Console Output

```text
============================================================
 AI Resume Screening & Ranking System
============================================================

Job Description Loaded Successfully.

Found 5 resumes.

Processing Resume : resume_test.txt
✓ Resume Processed Successfully

============================================================

FINAL RANKING

1. resume_test.txt

Overall Score : 91.97%

Recommendation : Highly Recommended
```

---

# 📁 Generated Output

After execution, the following files are generated automatically:

```
output/
│
├── ranked_candidates.csv
└── ranked_candidates.json
```

---

# ⚖️ Design Trade-offs

### Advantages

- Modular architecture
- Easy to extend
- Semantic similarity instead of simple keyword matching
- Generates structured reports
- Lightweight and easy to deploy

### Current Limitations

- Image-based resumes require OCR support
- Uses rule-based feature extraction
- Uses a single Job Description at a time

---

# 🚀 Future Improvements

- OCR support for scanned resumes
- LLM-powered resume understanding
- Advanced Named Entity Recognition (NER)
- Skill Ontology Integration
- Streamlit / Flask Dashboard
- ATS Integration
- Cloud Deployment
- Recruiter Authentication

---

# 👨‍💻 Author

**Prasanna Kumar**

Computer Science Engineer

AI • Machine Learning • NLP • Data Science

---

## ⭐ If you found this project useful, consider giving it a Star!