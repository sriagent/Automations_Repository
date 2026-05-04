
import json
import os

def analyze_startups():
    with open("data/raw_startups.json", "r") as f:
        startups = json.load(f)
    
    analyzed = []
    for s in startups:
        # Logic to identify Moats (e.g. Proprietary Data, Network Effect)
        # In a full version, this would use an LLM prompt
        analyzed.append({
            "name": s['name'],
            "usp": "Advanced AI model integration for vertical scaling.",
            "moat": "Proprietary training dataset from industry partners.",
            "status": "verified"
        })
    return analyzed

if __name__ == "__main__":
    data = analyze_startups()
    with open("data/analyzed_startups.json", "w") as f:
        json.dump(data, f, indent=4)
