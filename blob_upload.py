from azure.storage.blob import BlobServiceClient

# Azure Blob Storage connection string
connection_string = "https://dataengineerv1.blob.core.windows.net/raw"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

print("Blob service client initialized.")
