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
# Create a subscription
connectivity_subscription = client.connectivity.subscribe(
    event_type="org.camaraproject.device-status.v0.connectivity-data",
    device=my_device,
    # Use HTTPS to send notifications
    notification_url="https://example.com/notifications",
)
 
# Get the subscription previously created by its ID
subscription = client.connectivity.get_subscription(connectivity_subscription.id)
 
# Retrieve list of active Device Status subscriptions for a client:
subscriptions = client.connectivity.get_subscriptions()
 
# Check the connectivity or roaming status
# subscriptions of a given device
connectivity_status = my_device.get_connectivity()
 
roaming_status = my_device.get_roaming()


print(connectivity_status)
print(roaming_status)