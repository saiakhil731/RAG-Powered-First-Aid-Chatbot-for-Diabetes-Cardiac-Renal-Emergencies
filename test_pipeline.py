import sys
import os

# Dynamically get the absolute path to modules/ directory
current_dir = os.path.dirname(os.path.abspath(__file__))
modules_path = os.path.abspath(os.path.join(current_dir, "..", "modules"))
sys.path.append(modules_path)

from triage_module import TriageClassifier
from generator import AnswerGenerator

def test_triage():
    triage = TriageClassifier()
    condition, _ = triage.classify("My glucometer shows 55 mg/dL and I feel shaky.")
    assert condition.lower() == "hypoglycemia"

def test_generator():
    generator = AnswerGenerator()
    query = "shaky and low sugar"
    condition = "hypoglycemia"
    docs = [("Low sugar requires glucose intake", 0.95)]
    response = generator.generate(query, condition, docs, web=None)
    assert "Likely Condition:" in response
    assert "First-Aid Steps:" in response
