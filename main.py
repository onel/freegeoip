
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():

    # read headers
    headers = request.headers

    country = headers.get('X-AppEngine-Country', '')

    # if the country header is missing, or is ZZ
    # then app engine doesn't have geoip data
    if not country or country == 'ZZ':
        # return an empty object
        return jsonify({})

    region = headers.get('X-AppEngine-Region', '')
    city = headers.get('X-AppEngine-City', '')
    lat_long = headers.get('X-AppEngine-CityLatLong', ',').split(',')

    latitude = lat_long[0]
    longitude = lat_long[1]

    # Requests are proxid in App engine so request.remote_addr will not work
    # We have this special header to read the original ip address
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    ip_address = x_forwarded_for.split(',')[0]

    geoip_data = {
        'ipAddress': ip_address,
        'countryCode': country,
        'regionCode': region,
        'city': city,
        'latitude': latitude,
        'longitude': longitude,
    }

    return jsonify(geoip_data)

if __name__ == '__main__':
    app.run(debug=True)
