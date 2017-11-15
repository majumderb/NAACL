
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
            
            for i, r in enumerate(results):

                temp = [file_name, 
                        i,
                        r.find('padanum').text,
                        r.find('headword').text,
                        r.find('stem').text, 
                        r.find('morphids').text, 
                        r.find('lexids').text, 
                        r.find('root').text,
                        r.find('comment').text, 
                        r.get('selected')]
                
                
                final_list.append(temp)



prepare_data('MBhRenum')
prepare_data('pt1-2000xmlRenum')

df = pd.DataFrame(final_list, columns=['file_name', 'word_order', 'padanum', 'headword', 'stem', 'morphids', 'lexids', 'root', 'comment', 'selected'])
df.to_csv("word_enumerate.csv", index=False, encoding='utf-8')