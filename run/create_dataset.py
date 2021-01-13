import os
import csv
import json
from config import PERMISSION_LIST


def writedataset(filename_json, folder_jsons, target_value, file_csv):
    flags = []
    for i in range(len(PERMISSION_LIST)):
        flags.append("0")

    with open(os.path.join(folder_jsons, filename_json)) as f:

        json_file = json.load(f)
        permissions_app = json_file['permissions']
        permissions_final = []
        for elem in permissions_app:
            if elem.split('.')[0] == "android":
                permissions_final.append(elem[19:])
            else:
                continue

        for elem in permissions_final:
            try:
                index = PERMISSION_LIST.index(elem)
                if (index):
                    flags[index] = "1"

            except ValueError:
                pass

        flags[-1] = target_value

        return tuple(flags)


if __name__ == "__main__":
    files = []
    SAMPLES = 4000
    c1 = 0
    c2 = 0
    path_benign = os.path.join(os.getcwd(), "benign_samples")
    path_malware = os.path.join(os.getcwd(), "malware_samples")

    for root, dirs, jsons in os.walk(path_benign):
        files_benign = jsons

    print('Total Files Benign : ' + str(len(files_benign)))

    for root, dirs, jsons in os.walk(path_malware):
        files_malware = jsons

    print("Total Files Malware : " + str(len(files_malware)))

    BENIGN_SAMPLES = []
    for sample_benign in files_benign:

        if (c1 == SAMPLES): break
        BENIGN_SAMPLES.append(writedataset(sample_benign, "benign_samples", "0", "Android_permissions_dataset.csv"))
        c1 = c1 + 1

    MALWARE_SAMPLES = []
    for sample_malware in files_malware:
        if (c2 == SAMPLES): break
        MALWARE_SAMPLES.append(writedataset(sample_malware, "malware_samples", "1", "Android_permissions_dataset.csv"))
        c2 = c2 + 1

    with open("Android_permissions_dataset.csv", "wt") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(PERMISSION_LIST)
        writer.writerows(BENIGN_SAMPLES)
        writer.writerows(MALWARE_SAMPLES)




