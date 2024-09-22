from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute.models import (HardwareProfile, NetworkProfile,
                                       OSProfile, VirtualMachine, StorageProfile,
                                       OSDisk, ImageReference)

# Set up authentication
credential = DefaultAzureCredential()

subscription_id = "aee8556f-d2fd-4efd-a6bd-f341a90fa76e"
resource_group_name = "Data_Engineer"
location = "westeu"

# Create clients
resource_client = ResourceManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)