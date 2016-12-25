#curl -X DELETE -H "Content-Type: application/json" \
#	-H "Authorization: Bearer $DO_TOKEN" "https://api.digitalocean.com/v2/droplets/35453933"
import sys
import httplib
import os

ARGUMENTS = sys.argv

print ARGUMENTS

if len(ARGUMENTS) > 1 and ARGUMENTS[1]:
    print "Attempting to delete {0}".format(ARGUMENTS[1])

    TOKEN = os.environ['DO_TOKEN']

    URL_ROOT = "api.digitalocean.com"
    URL_SUFF = "/v2/droplets/{0}".format(ARGUMENTS[1])
    AUTH_HEADER = {
        "Content-type": "application/json",
        "Authorization": "Bearer {0}".format(TOKEN)
        }
    BODY = ''
    CONN = httplib.HTTPSConnection(URL_ROOT)

    CONN.request('DELETE', URL_SUFF, BODY, AUTH_HEADER)
    RESPONSE = CONN.getresponse()
    CONTENT = RESPONSE.read()

    print CONTENT
else:
    print "Incorrect, must enter argument."
