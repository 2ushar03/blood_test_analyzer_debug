## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import BaseTool
from crewai_tools import tools
from crewai_tools import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader
from typing import ClassVar

# 🌐 Web search tool (unchanged)
search_tool = SerperDevTool()

class BloodTestReportTool(BaseTool):
    name: str = "blood_test_report_tool"
    description: str = "Load and return full text from a blood test PDF."

    def _run(self, path: str = "data/blood_test_report.pdf") -> str:
        # Resolve absolute path
        abs_path = os.path.abspath(path)
        if not os.path.isfile(abs_path):
            raise FileNotFoundError(f"No PDF found at {abs_path}")

        loader = PyPDFLoader(abs_path)
        docs = loader.load()

        # Concatenate and clean content
        full_report = ""
        for doc in docs:
            content = doc.page_content.replace("\n\n", "\n")
            full_report += content + "\n"
        return full_report

## Creating Nutrition Analysis Tool
class NutritionTool:
    async def analyze_nutrition_tool(blood_report_data):
        # Process and analyze the blood report data
        processed_data = blood_report_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement nutrition analysis logic here
        return "Nutrition analysis functionality to be implemented"

## Creating Exercise Planning Tool
class ExerciseTool:
    async def create_exercise_plan_tool(blood_report_data):        
        # TODO: Implement exercise planning logic here
        return "Exercise planning functionality to be implemented"