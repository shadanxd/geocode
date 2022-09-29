from flask import Flask, request, jsonify
import requests
import json
import xml.etree.ElementTree as ET


#Init app
app=Flask(__name__)

@app.route('/getAddressDetails', methods=['POST'])
def map_det():
    address1=request.json["address"]
    format=request.json["output_format"]
    add1=address1.replace(' ', '+')
    add1=add1.replace('#', '')
    apikey=input()
    url=('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(add1,apikey))
    response=requests.get(url).json()
    lat = response['results'][0]['geometry']['location']['lat']
    lng = response['results'][0]['geometry']['location']['lng']
    if format == "json":
        
        x={"coordinates":{
            "lat":lat,
            "lng":lng
        }, "address": address1}
        return json.dumps(x)
    if format=="xml":
        root=ET.Element('root')
        m1=ET.Element('address')
        m1.text=address1
        root.append(m1)

        m2=ET.Element('coordinates')
        c1=ET.SubElement(m2, 'lat')
        c1.text=str(lat)
        c2=ET.SubElement(m2, 'lng')
        c2.text=str(lng)
        root.append(m2)
        
        return ET.tostring(root, encoding='utf8').decode('utf8')
    else:
        return jsonify("wrong input")



#Run server
if __name__=='__main__':
    app.run(debug=True, port=5001)
        

    
