import os
import network_as_code as nac
import dotenv as load_dotenv

load_dotenv()

token = os.getenv('NAC_TOKEN')

client = nac.NetworkAsCodeClient(
    token=token
)