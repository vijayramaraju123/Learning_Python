














import json

# Example metadata dictionary
metadict = {
    'etl_stp_parms':
        '{"cfxinpath": "/data/claims/2025/"}'
}

data = json.loads(metadict.get('etl_stp_parms')).get('cfxinpath')
print(data)
# Extracting the claims file path
cfxInpath = json.loads(metadict.get('etl_stp_parms')).get('cfxinpath', 'na')

print(cfxInpath)


ARGS = { 'metadata_dict': '{"file1": "/data/files/file1.txt", "file2": "/data/files/file2.txt"}'
}
data1 = json.loads(ARGS.get('metadata_dict')).get('file1')
print(data1)


metadict = json.loads(ARGS['metadata_dict'])
print(metadict)

detail  = {
    'data': '{"name":"raju","age":34}'
}

output=json.loads(detail.get('data')).get('name')
print(output)