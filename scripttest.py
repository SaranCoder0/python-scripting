import requests

def main():
    # URL of the website you want to request
    url = 'https://www.positka.com'
    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the content of the response
            print("Response Content:")
            print(response.text)
        else:
            print("Failed to retrieve webpage. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()