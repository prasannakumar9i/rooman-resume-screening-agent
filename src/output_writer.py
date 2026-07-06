"""
output_writer.py

Saves ranked candidates to CSV and JSON.
"""

import os
import json
import pandas as pd


class OutputWriter:

    def __init__(self, output_folder="output"):

        self.output_folder = output_folder

        os.makedirs(self.output_folder, exist_ok=True)

    def save_csv(self, ranked_candidates):

        df = pd.DataFrame(ranked_candidates)

        csv_path = os.path.join(
            self.output_folder,
            "ranked_candidates.csv"
        )

        df.to_csv(csv_path, index=False)

        print(f"\n✅ CSV saved successfully -> {csv_path}")

    def save_json(self, ranked_candidates):

        json_path = os.path.join(
            self.output_folder,
            "ranked_candidates.json"
        )

        clean_data = []

        for candidate in ranked_candidates:

            temp = {}

            for key, value in candidate.items():

                try:
                    temp[key] = float(value)
                except (ValueError, TypeError):
                    temp[key] = value

            clean_data.append(temp)

        with open(
            json_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                clean_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"✅ JSON saved successfully -> {json_path}")