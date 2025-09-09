#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from debate_crewai.crew import DebateCrewai

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': "The working week should be shortened to 4 days, with a 3-day weekend."
    }
    
    try:
        result = DebateCrewai().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
