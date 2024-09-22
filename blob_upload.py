from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient
import os

container_name = "raw"
blob_name = "tourism_dataset.csv"
file_path = "https://dataengineerv1.blob.core.windows.net/raw/tourism_dataset.csv"

# Azure Blob Storage connection string
connection_string = "https://dataengineerv1.blob.core.windows.net/raw"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

print("Blob service client initialized.")

# Check if container exists, if not, create it
container_client = blob_service_client.get_container_client(container_name)
if not container_client.exists():
   # container_client.create_container()
    print(f"Container '{container_name}' created.")
else:
    print(f"Container '{container_name}' already exists.")

 # Ensure file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist.")   

# Upload the file
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open(file_path, "rb") as file:
    blob_client.upload_blob(file)
    print(f"File '{blob_name}' uploaded to container '{container_name}'.")
