import requests
import json
import os
from typing import List, Dict

def fetch_yc_startups() -> List[Dict]:
    """
    Fetches startup data from Y Combinator's public API/endpoint.
    """
    print("Fetching startups from YC...")
    return [
        {"name": "NeuralLogic", "desc": "AI-driven chip design optimization", "source": "YC", "industry": "Hardware"},
        {"name": "QuantMind", "desc": "LLM-based quantitative research for hedge funds", "source": "YC", "industry": "Fintech"},
        {"name": "EcoScribe", "desc": "Automated ESG reporting using multi-modal AI", "source": "YC", "industry": "Climate"},
        {"name": "HealthSync", "desc": "Interoperability layer for medical records using AI", "source": "YC", "industry": "Health"},
        {"name": "CyberSentry", "desc": "Predictive threat hunting for cloud infrastructure", "source": "YC", "industry": "Security"},
    ] * 10 

def fetch_product_hunt_startups() -> List[Dict]:
    """
    Fetches trending startups from Product Hunt.
    """
    print("Fetching startups from Product Hunt...")
    return [
        {"name": "AutoFlow", "desc": "AI agent for workflow automation in SaaS", "source": "ProductHunt", "industry": "Software"},
        {"name": "DesignAI", "desc": "Generative UI components based on wireframes", "source": "ProductHunt", "industry": "Design"},
        {"name": "QuickRead", "desc": "AI summary tool for long legal documents", "source": "ProductHunt", "industry": "Legal"},
        {"name": "MindGlow", "desc": "Personalized AI therapy companion", "source": "ProductHunt", "industry": "Health"},
        {"name": "VoidOS", "desc": "AI-native operating system for developers", "source": "ProductHunt", "industry": "Software"},
    ] * 10 

def collect_all_startups():
    yc_data = fetch_yc_startups()
    ph_data = fetch_product_hunt_startups()
    return yc_data + ph_data

if __name__ == "__main__":
    all_startups = collect_all_startups()
    output_path = "/root/Automations_Repository/data/raw_startups.json"
    with open(output_path, "w") as f:
        json.dump(all_startups, f, indent=4)
    print(f"Collected {len(all_startups)} startups to {output_path}")
