from ncclient import manager

m = manager.connect(
    host="ios-xe-mgmt.cisco.com",
    port=10000,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )

#test Rev02

print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)
