from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.storage import StorageManagementClient

# Define subscription ID and resource group
SUBSCRIPTION_ID = 'aee8556f-d2fd-4efd-a6bd-f341a90fa76e'
RESOURCE_GROUP = 'Data_Engineer'

# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()

from azure.mgmt.network.models import VirtualNetwork, Subnet

network_client = NetworkManagementClient(credential, SUBSCRIPTION_ID)

# Create VNet
vnet_params = {
    "location": "westeu",
    "address_space": {"address_prefixes": ["10.0.0.0/16"]}
}
vnet = network_client.virtual_networks.begin_create_or_update(
    RESOURCE_GROUP,
    'swatishahi',
    vnet_params
).result()

# Create Subnet
subnet_params = {
    "address_prefix": "10.0.0.0/24"
}
subnet = network_client.subnets.begin_create_or_update(
    RESOURCE_GROUP,
    'swatishahi',
    'swati-subnet',
    subnet_params
).result()

print(f"VNet created: {vnet.id}")
print(f"Subnet created: {subnet.id}")

