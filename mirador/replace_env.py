#open /summerschool/index.json

import json
import os
import sys

#open summerschool/index.json and replace all occurrencies of "iptoreplace" with environment variable ip_host
def replace():
    with open('summerschool/index.json') as f:
        #read line by line
        data = f.readlines()
        #replace all occurrencies of "iptoreplace" with environment variable ip_host
        data = [line.replace('iptoreplace', os.environ['ip_host']) for line in data]
        #write the new file
        with open('summerschool/index.json', 'w') as f:
            f.writelines(data)






if __name__ == '__main__':
    replace()