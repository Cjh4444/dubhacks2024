import os
import network_as_code as nac
from dotenv import load_dotenv
from network_as_code.models.device import DeviceIpv4Addr

load_dotenv()
token = os.getenv('NAC_TOKEN')

client = nac.NetworkAsCodeClient(
    token=token
)
my_device = client.devices.get("05e11f17-2600-41b5-bb99-e7f66a874c7c@testcsp.net")

# get location of the device
location = my_device.location(max_age=3600)

longitude = location.longitude
latitude = location.latitude
print(longitude)
print(latitude)

# For estimations, use the is_there object
# followed by the `verify_location()` method
# with the geo-coordinates and maximum age in seconds.
# If the amount in seconds is not given, the default will be 60 seconds.
is_there = my_device.verify_location(
    longitude=27,
    latitude=37,
    radius=100_000,
    max_age=3600
)

