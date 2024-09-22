from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Set up credentials and storage account information
account_url = "https://dataengineerv1.blob.core.windows.net"
container_name = "raw"
credential = DefaultAzureCredential()

# Connect to the BlobServiceClient
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

# Upload CSV to Azure Storage
blob_client = blob_service_client.get_blob_client(container=container_name, blob="Swati-Shahi/Swati-Shahi.csv")
with open("<YourFirstName-YourLastName>.csv", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
print("Results uploaded to Azure Storage.")
