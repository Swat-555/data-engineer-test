from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

# Connect to the Azure Storage Account using DefaultAzureCredential
account_url = "https://dataengineerv1.blob.core.windows.net"
blob_service_client = BlobServiceClient(account_url, credential=DefaultAzureCredential())

# Access the 'raw' container and 'tourism_dataset.csv'
container_client = blob_service_client.get_container_client("raw")
blob_client = container_client.get_blob_client("tourism_dataset.csv")

# Download CSV file content into a Pandas DataFrame
csv_data = blob_client.download_blob().readall()
df = pd.read_csv(io.BytesIO(csv_data))

# Display first few rows
print(df.head())
