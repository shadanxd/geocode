Install flask "pip install flask"

input api key when prompted

If the api traceback says socket error/connection error without giving any output make sure to disable IPV6 in terminal "sysctl net.ipv6.conf.all.disable_ipv6=1" 

Run program using "python3 app.py"


Input format in json use postman (localhost:5001/getAddressDetails method[POST])
{
    "address":"your address",
    "output format":"json/xml"
}


