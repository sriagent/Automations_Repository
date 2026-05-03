import requests

def fetch_top_starred_repos(limit=15):
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "stars:>1",
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        repos = data.get('items', [])
        with open('data/top_15_repos.txt', 'w') as f:
            for repo in repos:
                f.write(f"{repo['full_name']} - {repo['html_url']}\n")
        
        print(f"Successfully saved {len(repos)} repositories to data/top_15_repos.txt")
    except Exception as e:
        print(f"Error fetching repos: {e}")

if __name__ == "__main__":
    fetch_top_starred_repos()
