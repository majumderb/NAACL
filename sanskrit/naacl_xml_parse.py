
import lxml.etree
import os
import pandas as pd


xml_files = os.listdir('MBhRenum')

## remove hidden files such as .DS_Store
final_files= list(set(xml_files).difference(set(['.DS_Store'])))

final_list = []

print len(final_files)

for file_name in final_files:

    with open('MBhRenum/'+file_name, 'r') as f:
        
        root = lxml.etree.fromstring(f.read())
        results = root.findall('pada')
        morphids = [r.find('morphids').text for r in results]
        final_list.append([file_name] + [','.join([id for id in morphids if id is not None])])

df = pd.DataFrame(final_list)
df.to_csv("maha.csv")