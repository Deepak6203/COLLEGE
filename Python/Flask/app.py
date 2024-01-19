#Methods one
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True, host='10.11.0.109', port=5000)
#     # app.run(debug=True, host='fe80::47e4:a291:9a4:e12e', port=5000)


# How to use This
    # Open Seting On your Windows GO TO
    # Network & internet > Advanced network settings > Hardware & Connection properties
    # Wi-Fi (Qualcomm QCA9377 802.11ac Wireless Adapter):

        # Physical address (MAC): 48:5f:99:9a:de:27
        # Status: Operational
        # IPv4 address: 10.11.0.109/16
        # IPv6 address: fe80::47e4:a291:9a4:e12e%6/64
        # IPv4 default gateway: 10.11.12.1
        # DNS servers: 103.85.93.93 (Unencrypted), 8.8.8.8 (Unencrypted)
        # Network name: SISTec TP 225 M1 8
        # Network category: Public
        # Connectivity (IPv4/IPv6): Connected to Internet / Connected to unknown network




