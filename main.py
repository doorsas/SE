import glob
import csv
import matplotlib.pyplot as plt


csv_files = glob.glob(r"C:\Users\PC\Desktop\Projektai\naujasprojektukas\SEprojektas\*.csv")


list1 = []
list2 = []
list4 = []
list6 = []
listt1 = []
listt2 = []
listt4 = []
listt6 = []
listtt1 = []
listtt2 = []
listtt4 = []
listtt6 = []
listttt1 = []
listttt2 = []
listttt4 = []
listttt6 = []


class SE:

    def __init__(self, fName):
        self.fName = fName
        self.U = None
        self.I = None
        self.santykis = None
        self.j = None
        self.failu_skaicius = 0
        self.FF = None
        self.pce_list = []
        self.jsc = []
        self.minimalusPCEsarasas = []
        self.minimalusJSCsarasas = []
        self.minimalusUOCsarasas = []
        self.minimalusFFsarasas = []
        self.read()

    def read(self):
        for i in range(0,len(csv_files)):

            with open(csv_files[i], 'r') as f:
                reader = csv.reader(f)
                next(reader)
                next(reader)
                self.failu_skaicius += 1
                self.pce_list = []
                U_list = []
                J_list = []
                self.santykis = float(csv_files[i][-7:-4])
                for row in reader :
                    self.U = float(row[0])
                    self.I = float(row[1])
                    self.j = self.I * 1000 / 0.09
                    J_list.append(self.j)
                    U_list.append(self.U)
                    self.PCE = self.j * self.U/100
                    self.pce_list.append(self.PCE)
                min_val, maziausio_U_indexas = min([(abs(val), idx) for (idx, val) in enumerate(U_list)])
                self.jsc = J_list[maziausio_U_indexas]
                min_val, maziausio_J_indexas = min([(abs(val), idx) for (idx, val) in enumerate(J_list)])
                self.Uoc = U_list[maziausio_J_indexas]
                self.FF = max(U_list) * max(J_list) / self.jsc * self.Uoc
                self.rusioti()

#     FF = Umax * jmax/jsc * Uoc

    def rusioti(self):

        if self.santykis == 0.1:
            list1.append(min(self.pce_list)* -100)
            listt1.append(self.jsc * -1)
            listtt1.append(self.Uoc * -1)
            listttt1.append(self.FF * -1)
        elif self.santykis == 0.2:
            list2.append(min(self.pce_list)* -100)
            listt2.append(self.jsc * -1)
            listtt2.append(self.Uoc * -1)
            listttt2.append(self.FF * -1)
        elif self.santykis == 0.4:
            list4.append(min(self.pce_list)* -100)
            listt4.append(self.jsc * -1)
            listtt4.append(self.Uoc * -1)
            listttt4.append(self.FF * -1)
        elif self.santykis == 0.6:
            list6.append(min(self.pce_list)* -100)
            listt6.append(self.jsc * -1 )
            listtt6.append(self.Uoc * -1)
            listttt6.append(self.FF * -1)


    def  gauti(self,name):
        if name == 'PCE':
            self.minimalusPCEsarasas = [list1,list2,list4,list6]
            return self.minimalusPCEsarasas
        elif name == 'JSC':
            self.minimalusJSCsarasas = [listt1,listt2,listt4,listt6]
            return self.minimalusJSCsarasas
        elif name == 'UOC':
            self.minimalusUOCsarasas = [listtt1,listtt2,listtt4,listtt6]
            return self.minimalusUOCsarasas
        elif name == 'FF':
            self.minimalusFFsarasas = [listttt1,listttt2,listttt4,listttt6]
            return self.minimalusFFsarasas
        else:
            print ('Nėra tokio')
            return []


    def atvaizduoti(self,name):
        fig, ax = plt.subplots(figsize=(6,6))
        ax.boxplot(a.gauti(name), showmeans=True, showfliers=True)
        ax.set_ylabel( name ,fontsize = 15)
        ax.set_xlabel('S/(S+Se)',fontsize = 15)
        ax.grid( which='major', axis='both')
        ax.set_xticks([1,2,3,4])
        ax.set_xticklabels(['0,1','0,2','0,4','0,6'])
        plt.show()


a = SE(csv_files)
a.atvaizduoti('PCE')
a.atvaizduoti('UOC')
a.atvaizduoti('JSC')
a.atvaizduoti('FF')
# a.gauti('JSC')

# %matplotlib qt
