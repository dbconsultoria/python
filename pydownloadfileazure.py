#pip install azure-storage-blob
from azure.storage.blob import BlobServiceClient

STORAGEACCOUNTURL = "https://dbaplexbipoc.blob.core.windows.net"
STORAGEACCOUNTKEY = "vEzvUZkN/huOQmwdsLyc5CmO08k+Pf5mOJFcvM6Vs0YbSIuXATMrHBCv4MLn3O/xSsf6M1V7xvPj+AStuXR/uA=="
CONTAINERNAME = "dbaplex-bi-poc"
BLOBNAME = "products_azure.csv"

blob_service_client_instance = BlobServiceClient(
    account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)

blob_client_instance = blob_service_client_instance.get_blob_client(
    CONTAINERNAME, BLOBNAME, snapshot=None)

blob_data = blob_client_instance.download_blob()
data = blob_data.readall()
print(data)