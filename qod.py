import os
import network_as_code as nac
from dotenv import load_dotenv
from network_as_code.models.device import DeviceIpv4Addr

load_dotenv()
token = os.getenv('NAC_TOKEN')

client = nac.NetworkAsCodeClient(
    token=token
)
my_device = client.devices.get("05e11f17-2600-41b5-bb99-e7f66a874c7c@testcsp.net", 
    # ipv4_address=DeviceIpv4Addr(
    #     public_address="233.252.0.2",
    #     private_address="192.0.2.25",
    #     public_port=80
    # ),
    ipv6_address="2001:db8:1234:5678:9abc:def0:fedc:ba98"
)
# ...and create a QoD session for the device
my_session = my_device.create_qod_session(
    service_ipv4="233.252.0.2",
    # service_ipv6="2001:db8:1234:5678:9abc:def0:fedc:ba98",
    profile="DOWNLINK_L_UPLINK_L",
    # We create the session for 3600 seconds, so up to an hour
    duration=3600
)

# Get all sessions
all_sessions = my_device.sessions()
 
# Notice how we can use the number '0'
# to retrieve our first session in this case:
first_session = all_sessions[0]
print(first_session)
 
# Let's confirm that the device has the newly created session
# print(my_device.sessions())
 
# Finally, remember to clear out the sessions for the device
my_device.clear_sessions()
