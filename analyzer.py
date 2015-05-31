import os
import sys
from Tools import getDataByDict
from Tools import writeData

walk_dir = sys.argv[1]
export_file = sys.argv[2]
print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

counter = 0
data_list = []

for root, subdirs, files in os.walk(walk_dir):
    #print('--\nroot = ' + root)

    #for subdir in subdirs:
        #print('\t- subdirectory ' + subdir)

    for filename in files:
        file_path = os.path.join(root, filename)
        extension = filename.split(".")[-1]
        basic_name = filename.split(".")[0].replace("Umsatz pro Kunde in Euro in der Kategorie  ", "").strip()
        #print('Category Name: '+ basic_name)
        if extension == 'csv':
            headers = []
            if counter == 0:
                headers.append('Child_Age_in_Months')
            headers.append('Mean_Revenue_per_Customer')
            data = getDataByDict(file_path, headers)
            headers_replace = {'Child_Age_in_Months': 'Child_Age_in_Months', 'Mean_Revenue_per_Customer': basic_name}
            if len(data) > 0:
                for key in headers:
                    values = data.get(key)
                    values.insert(0, headers_replace[key])
                    data_list.append(values)
                counter = counter + 1

length = len(data_list[0])
export_list = []
for data in data_list:
    if len(data) == length:
        export_list.append(data)

zipped = zip(*export_list)
export_data = list(zipped)

writeData(export_file, export_data)