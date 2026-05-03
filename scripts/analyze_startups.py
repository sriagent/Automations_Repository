import json
import random
from typing import List, Dict

def apply_moat_test(startup: Dict) -> float:
    """
    Scores a startup based on the 'Moat Test' / 10x Rule.
    Heuristics:
    - Generic 'AI wrapper' (e.g., 'AI summary tool') -> Low score.
    - Proprietary data or vertical integration -> High score.
    - Systemic architectural change -> Very high score.
    """
    desc = startup['desc'].lower()
    score = 5.0 # Base score
    
    # Wrappers/Generic attributes
    if any(word in desc for word in ['summary tool', 'chatbot', 'personalized', 'companion']):
        score -= 3.0
        
    # Proprietary/Technical Moats
    if any(word in desc for word in ['optimization', 'infrastructure', 'interoperability', 'native operating system']):
        score += 4.0
        
    if 'chip' in desc or 'hardware' in startup.get('industry', '').lower():
        score += 2.0
        
    return score

def analyze_startup(startup: Dict) -> Dict:
    """
    Analysis layer identifying USP and Competitors.
    """
    desc = startup['desc']
    usp = f"Proprietary approach to {desc.split(' ', 1)[1] if ' ' in desc else desc}"
    
    # Simulated competitor analysis
    competitors = ["Generic AI Inc", "BigTech Corp"]
    if "chip" in desc.lower():
        competitors = ["Nvidia", "AMD", "Intel"]
    elif "health" in desc.lower():
        competitors = ["Epic Systems", "Google Health"]
        
    return {
        **startup,
        "usp": usp,
        "competitors": competitors,
        "moat_score": apply_moat_test(startup)
    }

def process_startups(input_path: str, output_path: str):
    with open(input_path, 'r') as f:
        startups = json.load(f)
        
    analyzed = [analyze_startup(s) for s in startups]
    
    # Sort by Moat Score descending and take top 50
    top_50 = sorted(analyzed, key=lambda x: x['moat_score'], reverse=True)[:50]
    
    with open(output_path, 'w') as f:
        json.dump(top_50, f, indent=4)
    
    print(f"Processed {len(startups)} startups, saved top 50 high-moat startups to {output_path}")

if __name__ == "__main__":
    raw_data = "/root/Automations_Repository/data/raw_startups.json"
    final_data = "/root/Automations_Repository/data/startups_summary.json"
    process_startups(raw_data, final_data)
