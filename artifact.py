import requests
from requests.models import HTTPBasicAuth

USERNAME = "USERNAME" 
TOKEN = "Access token form https://github.com/settings/tokens"
REPO_NAME="REPO_NAME"

URL = "https://api.github.com/repos/"
ID_FILE_NAME = "ID_STORAGE"

def main():
    response = requests.get(URL + USERNAME + "/" + REPO_NAME + "/actions/artifacts", auth=HTTPBasicAuth(USERNAME, TOKEN))
    artifact = response.json()["artifacts"][0]
    id = artifact["id"]
    if(str(id) == read_id_from_file()):
        return
    file_url = artifact["archive_download_url"]
    file_name = artifact["name"]
    content = requests.get(file_url, auth=HTTPBasicAuth(USERNAME, TOKEN))
    download_file_from_response(content, file_name)
    write_id_to_file(id)

def write_id_to_file(id):
    file = open(ID_FILE_NAME, 'w')
    file.write(str(id))
    file.close()

def read_id_from_file():
    try:
        file = open(ID_FILE_NAME)
        id = file.read()
        file.close
        return id
    except:
        return 0

def download_file_from_response(response, file_name):
    file = open(file_name+".zip", "wb")
    file.write(response.content)
    file.close

if __name__ == "__main__":
    main()
