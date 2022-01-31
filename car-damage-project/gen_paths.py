import os

classes = ['00-damage', '01-whole']

if os.path.exists('trainpaths.txt'):
    os.remove('trainpaths.txt')

root_dir = '../car-damage-project/kaggle_data/training/'
for folder in os.listdir(root_dir):
    for filename in os.listdir(os.path.join(root_dir, folder)):
        path = os.path.join(root_dir, folder, filename).replace("\\","/")
        label = classes.index(folder)
        with open('trainpaths.txt', 'a') as f:
            f.writelines(str(label)+','+path+'\n')
            
if os.path.exists('testpaths.txt'):
    os.remove('testpaths.txt')
            
root_dir = '../car-damage-project/kaggle_data/validation/'
for folder in os.listdir(root_dir):
    for filename in os.listdir(os.path.join(root_dir, folder)):
        path = os.path.join(root_dir, folder, filename).replace("\\","/")
        label = classes.index(folder)
        with open('testpaths.txt', 'a') as f:
            f.writelines(str(label)+','+path+'\n')