import shutil
import zipfile
import os

downloads = os.listdir('D:/Downloads/')

i = 0

for elm in downloads:
    downloads[i] = 'D:/Downloads/'+ elm
    i += 1
    
i = 0

for n in downloads:
    a = os.path.splitext(downloads[i])

    if a[1] == '.zip':
        shutil.move(downloads[i], 'zips_for_attribution/')
    i += 1
    
decompress = os.listdir('zips_for_attribution/') 

for z in decompress: 
    folder_a = zipfile.ZipFile('zips_for_attribution/' + z,'r')
    folder_a.extractall('folders_for_attribution/')
    folder_a.close()
#    os.remove('zips_for_attribution/' + z)
    
path = r'folders_for_attribution/' 

for filefolder in os.listdir(path): 
    folder_path = path +'/'+filefolder
    print ' '
    print str(filefolder) + ' - this is dir! '
    print ' '
    
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            if file.endswith(".py"):
                print file
                if os.path.exists(folder_path + '/' + file) is False:
                    shutil.move(os.path.join(root,file), folder_path)
        
            for dir in dirs:
                dirdel = os.path.join(root, dir)
                shutil.rmtree(dirdel)
            
            if file_extension != '.java': 
                    print str(file_extension) + '   NO PY'
                    os.remove(folder_path + '/' + file) 
                    
for filefolder in os.listdir(path): 
    shutil.move(path + '/' + filefolder, 'authors')
    print str(filefolder) + ' - this is dir! '