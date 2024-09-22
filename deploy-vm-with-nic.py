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

# Key variables
vnet_name = "swatishahi"
subnet_name = "swati_subnet"
nic_name = "NIc-SwatiShahi"
vm_name = "VM-SwatiShahi"
admin_username = "azureuser"
admin_password = "your-secure-password"

# Retrieve the NIC
nic = network_client.network_interfaces.get(resource_group_name, nic_name)

# Define VM parameters
vm_params = {
    'location': location,
    'os_profile': OSProfile(
        computer_name=vm_name,
        admin_username=admin_username,
        admin_password=admin_password  # You can use SSH keys instead for better security
    ),
    'hardware_profile': HardwareProfile(
        vm_size='Standard_DS1_v2'  # VM size can be adjusted
    ),
    'storage_profile': StorageProfile(
        image_reference=ImageReference(
            publisher='Canonical',
            offer='UbuntuServer',
            sku='18.04-LTS',
            version='latest'
        ),
        os_disk=OSDisk(
            name=f'{vm_name}-osdisk',
            caching='ReadWrite',
            create_option='FromImage'
        )
    ),
    'network_profile': NetworkProfile(
        network_interfaces=[{
            'id': nic.id,
            'primary': True
        }]
    )
}

# Deploy the VM
async_vm_creation = compute_client.virtual_machines.begin_create_or_update(
    resource_group_name,
    vm_name,
    vm_params
)

vm_result = async_vm_creation.result()  # Wait for completion
print(f"VM {vm_name} created with ID: {vm_result.id}")
