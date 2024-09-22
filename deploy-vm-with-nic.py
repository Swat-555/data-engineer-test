from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute.models import (HardwareProfile, NetworkProfile,
                                       OSProfile, VirtualMachine, StorageProfile,
                                       OSDisk, ImageReference)

