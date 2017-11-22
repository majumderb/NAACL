
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
            words = [r.find('headword').text for r in results]
            lexids = [r.find('lexids').text for r in results]
            final_list.append([file_name] +
                                [','.join([id if id is not None else '0' for id in morphids])] + 
                                [','.join([word for word in words if word is not None])] + 
                                [','.join([id if id is not None else '0' for id in lexids])])

prepare_data('MBhRenum')
prepare_data('pt1-2000xmlRenum')

df = pd.DataFrame(final_list, columns=['sentID', 'sent', 'words', 'lexids'])
df.to_csv("combined_maha_pt.csv", index=False, encoding='utf-8')