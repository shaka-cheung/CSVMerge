import numpy
import csv

def getNumData(file_path):
    data = []
    try:
        csv = numpy.genfromtxt(file_path, delimiter=',')
        first = csv[:,0]
        second = csv[:,1]
        data.append(first)
        data.append(second)
    except ValueError:
        #print("Unexpected error:", ValueError)
        #raise
        pass
    return data

def getData(file_path):
    data = []
    with open(file_path, 'rU', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',')#, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        #print(file_path)
        try:
            column1 = []
            column2 = []
            for row in csv_reader:
                column1.append(row[0])
                column2.append(row[1])
                #print(row)
            data.append(column1)
            data.append(column2)
        except UnicodeDecodeError:
            print("Unexpected error:", UnicodeDecodeError)
    return data

def getDataByDict(file_path, headers):
    data = {}
    with open(file_path, 'rU') as f:
        reader = csv.DictReader(f, delimiter = ',')
        try:
            for header in headers:
                data[header] = []
            for row in reader:
                for header, value in row.items():
                    if header in headers:
                        data[header].append(value)
        except KeyError:
            print("Unexpected error:", KeyError)
        except UnicodeDecodeError:
            print("Unexpected error:", UnicodeDecodeError)
    return data

def writeData(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            csv_writer.writerow(row)