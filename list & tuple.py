import sys

server_name = sys.argv[1]

servers=["aws_server" , "contabo_server", "gcp_server", "azure_server"]

config=[4,  "GB",  "CPU",  4,  "CORE"]
print(config)

slice=servers[1:3]

print(slice)