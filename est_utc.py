import sys
import json
from datetime import datetime, timedelta

# Convert 'time' values in json records from EST to UTC

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
TIME_DELTA = timedelta(hours=5)

# TODO check number of args

inPath = sys.argv[1]
outPath = sys.argv[2]

with open(outPath, 'w') as outFile:
    with open(inPath) as inFile:
        for line in inFile:
            json_data = json.loads(line)
            print ('input', json_data)
            est = datetime.strptime(json_data['time'], DATE_FORMAT)
            utc = est + TIME_DELTA
            json_data['time'] = utc.strftime(DATE_FORMAT)
            print ('output', json_data)
            outFile.write(json.dumps(json_data))
            outFile.write('\n')



        
