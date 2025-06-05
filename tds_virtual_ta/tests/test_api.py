import requests

def test_api():
    res = requests.post("http://localhost:5000/api/", json={"question": "What model should I use for GA5 Q8?"})
    print(res.json())

# Run it
# test_api()
