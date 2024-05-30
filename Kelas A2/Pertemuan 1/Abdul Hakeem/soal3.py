import sys
import numpy as np

def niucheck():
    niu = int(input("Masukkan NIU: "))
    while len(str(niu)) != 6:
        print("NIU Invalid!")
        niu = int(input("Masukkan NIU: "))
    return int(niu)

def basescore():
    global ntugas, nlaporan
    ntugas = int(input("Masukkan nilai tugas: "))
    nlaporan = int(input("Masukkan nilai laporan: "))
    baseavg = np.average([ntugas, nlaporan])
    if baseavg < 40:
        print("K")
        sys.exit()
    else:
        return ntugas, nlaporan

def finalscore():
    global finalavg
    nujian = int(input("Masukkan nilai ujian: "))
    finalavg = np.average([np.average([ntugas, nlaporan]), nujian])

def hurufoutput():
    if finalavg >= 80:
        print("A")
    elif finalavg >= 70:
        print("B")
    elif finalavg >= 60:
        print("C")
    elif finalavg >= 50:
        print("D")
    else:
        print("E")


def main():
    niucheck()
    basescore()
    finalscore()
    hurufoutput()

if __name__ == "__main__":
    main()
