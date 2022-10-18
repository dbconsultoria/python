#!/usr/bin/env python
#pip install requests
import requests

def validate_cep(field):
    cep = "".join(field.replace("-"," ").split())
    if cep.isdigit() and len(cep) == 8:
       return cep
    raise Exception('CEP "{field}" Format Invalid'.format(field=field))


if __name__ == '__main__':
    cep = validate_cep('01234000')
    api_cep_url = 'https://example.api.findcep.com/v1/cep/{cep}.json'
    headers = {'Referer': 'https://your-site.com'}

    response = requests.get(api_cep_url.format(cep=cep), headers=headers)
    print(response.json())