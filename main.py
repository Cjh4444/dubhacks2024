import os
import requests
import network_as_code as nac
from dotenv import load_dotenv
from network_as_code.models.device import DeviceIpv4Addr

def main():
    device = get_device()
    print(get_distance_time("40.7128,-74.0060", "34.0522,-118.2437"))

token = os.getenv("NAC_TOKEN")
maps_token = os.getenv("MAPS_TOKEN")

client = nac.NetworkAsCodeClient(token=token)
