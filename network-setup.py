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
