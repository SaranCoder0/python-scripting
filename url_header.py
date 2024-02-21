import requests
import sys

def main(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the headers of the response
            print("Response Headers:")
            for header, value in response.headers.items():
                print(f"{header}: {value}")
        else:
            print("Failed to retrieve webpage. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    # Check if the URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <url>")
        sys.exit(1)
    
    # Get the URL from the command-line arguments
    url = sys.argv[1]
    main(url)
