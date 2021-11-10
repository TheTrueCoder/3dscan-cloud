import requests
from requests.structures import CaseInsensitiveDict
import download

def get_fosshub_url(projectId: str, releaseId: str, projectUri: str, fileName: str, source: str = "CF") -> str:
    url = "https://api.fosshub.com/download/"
    
    headers = CaseInsensitiveDict()
    headers["content-type"] = "application/json; charset=UTF-8"

    data = {
        "projectId":projectId,
        "releaseId":releaseId,
        "projectUri":projectUri,
        "fileName":fileName,
        "source":source
    }

    resp = requests.post(url, headers=headers, data=data)
    return str(resp.json()['data']['url'])

