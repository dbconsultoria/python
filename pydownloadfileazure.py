#pip install azure-storage-blob
from azure.storage.blob import BlobServiceClient

STORAGEACCOUNTURL = "https://storagename.blob.core.windows.net"
STORAGEACCOUNTKEY = "storagekey" #secretkey
CONTAINERNAME = "containername"
BLOBNAME = "products_azure.csv"

blob_service_client_instance = BlobServiceClient(
    account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)

blob_client_instance = blob_service_client_instance.get_blob_client(
    CONTAINERNAME, BLOBNAME, snapshot=None)

blob_data = blob_client_instance.download_blob()
data = blob_data.readall()
print(data)