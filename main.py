import os
import network_as_code as nac

token = os.getenv('NAC_TOKEN')

client = nac.NetworkAsCodeClient(
    token=token
)