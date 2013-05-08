import sys
import json

# load a file containing one JSON object per line
# returns an iterator of dictionaries
def load_json(fileName):
    with open(fileName) as f:
        for line in f:
            yield json.loads(line)


# Test application
if  __name__ == "__main__":
    i = 0

    for d in load_json(sys.argv[1]):
	i += 1
    	print i, ":", d
