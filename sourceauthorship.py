import os
import zipfile
import warnings 

warnings.filterwarnings('ignore')
directory_authors = 'authors'

coefs = []
sample = []
source = []
entropy = []

#H(T/Si) = (C(SiT)-C(T))/T, где Si - сжатый подклееваемый текст, T - образец

sample_project = os.listdir('sample_folder')
with open('sample_project.txt', 'w') as outfile:
    for fname in sample_project:
        with open('sample_folder/' + fname) as infile:
            outfile.write(infile.read())
            
sample_project_zip = zipfile.ZipFile('sample_project.zip','w')
sample_project_zip.write('sample_project.txt', compress_type = zipfile.ZIP_DEFLATED)
sample_project_zip.close()

for filefolder in os.listdir(directory_authors): #authors 1..n
    folder_path = directory_authors+'/'+filefolder
    if os.path.isdir(folder_path): 
 
        for filefolderdown in os.listdir(folder_path): #projects 1..n
            folderdown_path = folder_path + '/' +filefolderdown 
            if os.path.isdir(folderdown_path): 
                source_project = os.listdir(folderdown_path)
                
                with open(folderdown_path + '/source_project.txt', 'w') as outfile: #конкатенация файлов project in authors
                    for fname in source_project:
                        with open(folderdown_path + '/' + fname) as infile:
                            outfile.write(infile.read())
                            
            sourcetxt = open(folderdown_path + '/source_project.txt','r')
            sampletxt = open('sample_project.txt','r')
            entropy_coef = open('entropy_coef.txt','w')
            source = sourcetxt.read()
            sample = sampletxt.read()
            sampletxt.close()
            sourcetxt.close()
            entropy = sample + source
            entropy_coef.write(entropy) 
            entropy_coef.close()

            entropy_coef_zip = zipfile.ZipFile('entropy_coef.zip','w')
            entropy_coef_zip.write('entropy_coef.txt', compress_type = zipfile.ZIP_DEFLATED)
            entropy_coef_zip.close()

            sample_lesscompress = sample_project_zip.getinfo('sample_project.txt').file_size
            sample_withcompress = sample_project_zip.getinfo('sample_project.txt').compress_size
            entropy_withcompress = entropy_coef_zip.getinfo('entropy_coef.txt').compress_size
            
#            print 'DEBUG IO SAMPLE:   ' + str(sample_project_zip.namelist())
#            print 'DEBUG IO ENTROPY:   ' + str(entropy_coef_zip.namelist())
            
            result = float(entropy_withcompress - sample_withcompress)/sample_lesscompress
            coefs.append(result)
                
#            print 'The resulting compression ratio: ' + str(result) + ' for ' + str(folderdown_path)
#            print ' '
            
            if min(coefs) == result:
                path_to_the_min = str(folder_path)
            
print 'Minimum ratio = ' + str(min(coefs)) + '! The most likely author of this code is ' + path_to_the_min + '!'