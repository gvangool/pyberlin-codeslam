import base64
import datetime
import json

if __name__ == "__main__":
    data = {
        "hello": "world",
        "location": "Berlin, DE",
        "event": "PyBerlin 7",
        "date": datetime.date(2019, 8, 28).toordinal(),
    }
    to_encode = json.dumps(data).encode("utf-8")
    print(f"{base64.b64encode(to_encode)=}")
    print(f"{base64.b32encode(to_encode)=}")
    print(f"{base64.b16encode(to_encode)=}")
    print(f"{base64.b85encode(to_encode)=}")
