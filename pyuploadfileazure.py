#dia: 21/10/2022
#Fonte: https://www.youtube.com/watch?v=OZGPAKTXGDs
from azure.storage.blob import BlobServiceClient

root_path = r"C:\Users\Rodrigo\Documents\GitHub\python"
dir_name = "files"
path = f"{root_path}/{dir_name}"

storage_account_name = "https://your_storage_account.blob.core.windows.net"
storage_account_key = ""#go to keys and paste here
container_name = "dbaplex-bi-poc" #get your container name 
connection_string = ""#on keys get the conn string

def uploadToBlobStorage(file_path,file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    
    with open(file_path,"rb") as data:
        blob_client.upload_blob(data)
    print(f"Uploaded {file_name}")


uploadToBlobStorage("C:\\Users\\Rodrigo\\Documents\\GitHub\\python\\files\\file.txt","file1.txt")

