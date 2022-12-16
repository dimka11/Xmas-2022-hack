import requests


def get_req():
	url = 'http://127.0.0.1:8000/status'
	resp = requests.get(url=url)
	print(resp.json())


def post_req():
	url = 'http://127.0.0.1:8000/fit'
	json_body = {"keyword": "Testiiiiii"}
	resp = requests.post(url=url, json=json_body)
	print(resp.json())



if __name__ == "__main__":
	get_req()
	post_req()

	