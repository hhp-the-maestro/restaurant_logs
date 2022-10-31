import csv
import operator
import argparse



class LogReader:
    def __init__(self, filename):
        self.filename = filename
        self.top_result = {}
        self.log = {}


    def csv_reader(self):
        # opening and reading the csv file
        file = open(self.filename)
        reader = csv.reader(file)
        reader.__next__() # skip the csv headers

        '''for row in the csv we will store the foodmenu_id mapping to a list of eater_id,  
        if the eater_id is already present in the array of the particualr foodmenu_id , then we will raise a exception.
        will keep track of the count of each foodmenu_id in another dict and sort it in desc at last and return the first
         3 foodmenu_id'''
         
        for row in reader:

            if row[0] in self.log.get(row[1], []):
                raise Exception("Error: Duplicate eater_id for the same foodmenu_id")

            if self.log.get(row[1]):
                self.log[row[1]].append(row[0])
            else:
                self.log[row[1]] = [row[0]]

            self.top_result[row[1]] = self.top_result.get(row[1], 0) + 1

        sort_dict = sorted(self.top_result.items(), key=operator.itemgetter(1), reverse=True)
        file.close()

        return [i[0] for i in sort_dict[:3]]



if __name__ == "__main__":
    # get the csv filename from the cmd line arg
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--filename", help="csv filename")

    args = parser.parse_args()

    if args.filename:
        filename = args.filename
    else:
        raise Exception("No CSV file was provided")

    # creating the instance of the log reader
    lr = LogReader(filename)
    # calling the csv_reader method which produces the output of the top 3 foodmenu_id
    print(lr.csv_reader())




