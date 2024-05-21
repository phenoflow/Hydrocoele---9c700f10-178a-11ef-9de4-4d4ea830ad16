# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"7C08200","system":"readv2"},{"code":"K23..00","system":"readv2"},{"code":"7C08712","system":"readv2"},{"code":"7C08400","system":"readv2"},{"code":"7C08600","system":"readv2"},{"code":"K231.00","system":"readv2"},{"code":"K23z.00","system":"readv2"},{"code":"1782.0","system":"readv2"},{"code":"35126.0","system":"readv2"},{"code":"4010.0","system":"readv2"},{"code":"98633.0","system":"readv2"},{"code":"31183.0","system":"readv2"},{"code":"521.0","system":"readv2"},{"code":"1226.0","system":"readv2"},{"code":"N43.1","system":"readv2"},{"code":"N43.3","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hydrocoele-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hydrocoele-incl-infected-hydrocele---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hydrocoele-incl-infected-hydrocele---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hydrocoele-incl-infected-hydrocele---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
