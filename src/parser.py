"""
parser.py

This module is responsible for reading resumes from different file formats
such as PDF, DOCX, and TXT, and extracting their text content.
"""

import fitz  # PyMuPDF
import docx
import os


class ResumeParser:
    """
    A class to parse resumes from different file formats.
    """

    def extract_text(self, file_path):
        """
        Detect the file type and extract text accordingly.
        """

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return self._extract_pdf(file_path)

        elif extension == ".docx":
            return self._extract_docx(file_path)

        elif extension == ".txt":
            return self._extract_txt(file_path)

        else:
            raise ValueError(f"Unsupported file format: {extension}")

    def _extract_pdf(self, file_path):
        """
        Extract text from PDF.
        """

        text = ""

        document = fitz.open(file_path)

        for page in document:
            page_text= page.get_text("text")
            print(f"Page text length: {len(page_text)}")
            text += page_text

        document.close()

        return text

    def _extract_docx(self, file_path):
        """
        Extract text from DOCX.
        """

        document = docx.Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    def _extract_txt(self, file_path):
        """
        Extract text from TXT.
        """

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()