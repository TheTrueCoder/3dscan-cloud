import requests
from requests.structures import CaseInsensitiveDict
import download

download.download("https://objects.githubusercontent.com/github-production-release-asset-2e65be/34405381/c37e5880-7dfc-11eb-845b-5d103f55f14d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20211110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211110T212559Z&X-Amz-Expires=300&X-Amz-Signature=86a4a8dd37d5e7e9246ef75dc7295aae5da4918d0cd2c414928c5c4e19c52a8c&X-Amz-SignedHeaders=host&actor_id=38576090&key_id=0&repo_id=34405381&response-content-disposition=attachment%3B%20filename%3DMeshroom-2021.1.0-win64.zip&response-content-type=application%2Foctet-stream", "./cache")

