"""
feature_extractor.py

Extract structured information from resumes.
"""

import re


class FeatureExtractor:

    def __init__(self):

        self.skills = {
            "python","java","c","c++","sql","mysql","mongodb",
            "html","css","javascript","react","nodejs","flask",
            "django","machine learning","deep learning","nlp",
            "artificial intelligence","data science",
            "tensorflow","pytorch","pandas","numpy",
            "scikit-learn","git","github","docker",
            "aws","azure","linux"
        }

        self.education_keywords = {
            "b.e","b.tech","m.tech","bachelor",
            "master","phd","computer science",
            "information science","engineering"
        }

    def extract_skills(self, text):

        text = text.lower()

        found = []

        for skill in self.skills:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):

                found.append(skill)

        return sorted(set(found))

    def extract_education(self, text):

        text = text.lower()

        education = []

        for keyword in self.education_keywords:

            if keyword in text:

                education.append(keyword)

        return sorted(set(education))

    def extract_experience(self, text):

        text = text.lower()

        patterns = [

            r"(\d+)\+?\s*years?",

            r"(\d+)\+?\s*yrs?",

            r"experience\s*:\s*(\d+)",

        ]

        years = []

        for pattern in patterns:

            matches = re.findall(pattern, text)

            for match in matches:

                years.append(str(match) + " years")

        return sorted(set(years))

    def extract_projects(self, text):

        keywords = [

            "project",

            "developed",

            "implemented",

            "built",

            "designed"

        ]

        projects = []

        lower = text.lower()

        for word in keywords:

            if word in lower:

                projects.append(word)

        return sorted(set(projects))

    def extract_certifications(self, text):

        keywords = [

            "certified",

            "certificate",

            "coursera",

            "udemy",

            "aws",

            "azure",

            "google"

        ]

        certs = []

        lower = text.lower()

        for word in keywords:

            if word in lower:

                certs.append(word)

        return sorted(set(certs))

    def extract_features(self, text):

        return {

            "skills": self.extract_skills(text),

            "education": self.extract_education(text),

            "experience": self.extract_experience(text),

            "projects": self.extract_projects(text),

            "certifications": self.extract_certifications(text)

        }