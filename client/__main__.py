import mfac.client
import json

if __name__ == '__main__':
    device_id = '74199D'
    c = mfac.client.Client(device_id)
    print(json.dumps(c.json_data, indent=2))
    print(c.get_time_and_data())
