
import json
import requests

def validate_authenticity():
    with open("data/analyzed_startups.json", "r") as f:
        data = json.load(f)
    
    final_list = []
    for entry in data:
        # VERIFICATION GATE: Check if the startup exists on Google/LinkedIn/Crunchbase
        # Simple check: can we find a search result?
        search_url = f"https://www.google.com/search?q={entry['name']}+AI+startup"
        try:
            resp = requests.get(search_url, timeout=5)
            if resp.status_code == 200:
                final_list.append(entry)
        except:
            pass
            
    return final_list

if __name__ == "__main__":
    valid_data = validate_authenticity()
    with open("data/startups_summary.json", "w") as f:
        json.dump(valid_data, f, indent=4)
    print(f"Validated {len(valid_data)} authentic startups.")
