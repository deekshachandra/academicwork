import sys
import json
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python google_search.py <credentials_file.json>")
        return

    credentials_file = sys.argv[1]

    try:
        with open(credentials_file, 'r') as f:
            json_content = f.read()
        print("Credentials file content:\n", json_content)

        credentials = json.loads(json_content)
        api_key = credentials['key']
        search_engine_id = credentials['search_engine_id']

        while True:
            query = input("\nSearch term?\n")
            if query.lower() == "stop":
                break

            params = {
                'key': api_key,
                'cx': search_engine_id,
                'q': query
            }
            response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)

            print("\nHTTP response status code:", response.status_code)
            print("\nHTTP response headers:")
            for header, value in response.headers.items():
                print(f"{header} : {value}")

            data = response.json()
            print("\nSearch results:")
            for item in data.get('items', []):
                print(f"{item['title']} ----- {item['link']}")

    except FileNotFoundError:
        print(f"Error: File '{credentials_file}' not found.")
    except KeyError as e:
        print(f"Error: Missing key in credentials file: {e}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()