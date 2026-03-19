import urllib.request
import shutil

def download_file(url: str, local_path:str):    
    with urllib.request.urlopen(url) as response, open(local_path, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)