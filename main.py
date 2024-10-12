import os
import requests
import network_as_code as nac
from dotenv import load_dotenv
from network_as_code.models.device import DeviceIpv4Addr

def main():
    device = get_device()
    get_distance("40.7128,-74.0060", "34.0522,-118.2437")


def get_device():
    """returns device object

    Returns:
        Device: Device object
    """
    load_dotenv()
    token = os.getenv('NAC_TOKEN')
    device_id = os.getenv('DEVICE_ID')

    client = nac.NetworkAsCodeClient(
        token=token
    )
    return client.devices.get(device_id)


def get_location(device):
    """returns longitude, latitude of device

    Returns:
        List: [longitude, latitude]
    """
    location = device.location(max_age=3600)

    longitude = location.longitude
    latitude = location.latitude
    return f'{longitude}, {latitude}'

def get_distance(location1, location2):
    load_dotenv()
    google_token = os.getenv('GOOGLE_API_KEY')
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={location1}&destinations={location2}&key={google_token}'
    # Make the request
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()

    if data['status'] == 'OK':
        distance = data['rows'][0]['elements'][0]['distance']['text']
        duration = data['rows'][0]['elements'][0]['duration']['text']
        print(f"Distance: {distance}, Duration: {duration}")
    else:
        print("Error in request")

if __name__ == '__main__':
    main()