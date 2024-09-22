from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient

container_name = "raw"

# Azure Blob Storage connection string
connection_string = "https://dataengineerv1.blob.core.windows.net/raw"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

print("Blob service client initialized.")

# Check if container exists, if not, create it
container_client = blob_service_client.get_container_client(container_name)
if not container_client.exists():
    container_client.create_container()
    print(f"Container '{container_name}' created.")
else:
    print(f"Container '{container_name}' already exists.")
