import requests
requests.packages.urllib3.disable_warnings()
from pprint import pprint


def getticket(projectnumber):
    response = requests.get('https://wbpebeszallito.wessling.priv/projects/kal-u/'
                            'issues.json?tracker_id=10|4&cf_1={}&sort=id&status_id=*'.format(projectnumber),
                            headers={'X-Redmine-API-Key': '7497794a8a4360f5e0e5d0341b51d32ed020f679',
                                     'Content-Type': 'application/json'}, verify=False)
    json_response = response.json()
    if response.status_code == 200 and len(json_response['issues']) != 0:
        pprint(json_response)
        #  print(type(json_response))
        print(json_response['total_count'])
        return json_response['issues'][0]['status']['name']
    else:
        return '---'


print(getticket('2022K04182'))
