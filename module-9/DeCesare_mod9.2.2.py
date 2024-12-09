import requests
import json

def responses(obj):
    formatted_obj = json.dumps(obj, sort_keys=True, indent=4) # Formatting
    return formatted_obj  # Return the formatted JSON string.

def main():
    url = 'https://jsonplaceholder.typicode.com/posts' # Use a valid endpoint that returns JSON data
    r = requests.get(url)

    if r.status_code == 200: # Make sure the request is successful
        obj = r.json()
        print(responses(obj))  # Call the function and print the formatted JSON.
    else:
        print(f"Failed to fetch data. HTTP Status Code: {r.status_code}")

if __name__ == '__main__':
    main()
