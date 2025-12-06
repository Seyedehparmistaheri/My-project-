import sys
import requests


if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    amount = float(sys.argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

url = "https://api.coincap.io/v2/assets/bitcoin"
API = "0b37f5ba32ca2500d54891e1e37f220a6d9bf1ab947151c69e19d6e6134af727"


headers = {
    "Authorization": f"Bearer {API}"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    print("API request failed")
    sys.exit(1)

ghimat = price * amount

print(f"${ghimat:,.4f}")


