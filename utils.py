from csv import writer

def append_list_as_row(fileName, listProperties):
    with open(fileName, "a+", newline="") as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(listProperties)

