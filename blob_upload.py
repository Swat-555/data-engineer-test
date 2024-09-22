from azure.storage.blob import BlobServiceClient

# Azure Blob Storage connection string
connection_string = "<Your_Azure_Storage_Account_Connection_String>"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

print("Blob service client initialized.")
