
import lxml.etree
import os
import pandas as pd

final_list = []

def prepare_data(folder_name):

    xml_files = os.listdir(folder_name)

    ## remove hidden files such as .DS_Store
    final_files= list(set(xml_files).difference(set(['.DS_Store'])))
    
    print len(final_files)

    for file_name in final_files:

        with open(folder_name+'/'+file_name, 'r') as f:
            
            root = lxml.etree.fromstring(f.read())
            results = root.findall('pada')
            morphids = [r.find('morphids').text for r in results]
            final_list.append([file_name] + [','.join([id for id in morphids if id is not None])])

prepare_data('MBhRenum')
prepare_data('pt1-2000xmlRenum')

df = pd.DataFrame(final_list)
df.to_csv("combined_maha_pt.csv", index=False)