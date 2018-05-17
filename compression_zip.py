import os 
import zipfile

def zipdir(path,zip_file ):
    
    for root, dirs, files in os.walk(path):
        for file in files:
            zip_file.write(os.path.join(root, file))

zipf_file = zipfile.ZipFile('compress.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('/home/amardeep/haskell_code', zipf_file)
zipf_file.close()