import mfac.client

if __name__ == '__main__':
    device_id = '74199D'
    c = mfac.client.Client(device_id)
    j = c.json_data
    for i in range(0, 2):
        print((
            j["data"][i]["time"],
            j["data"][i]["data"]))
