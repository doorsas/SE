import glob
import math
import csv
import pandas as pd
import matplotlib.pyplot as plt


csv_files = glob.glob(r"C:\Users\PC\Desktop\Projektai\naujasprojektukas\SEprojektas\*.csv")

class SE:

    def __init__(self, fName):
        self.fName = fName
        self.santykis = None
        self.PCE = None
        self.FF = None
        self.Uoc = None
        self.j_cs = None
        self.minPCElist1 = []
        self.minPCElist2 = []
        self.minPCElist4 = []
        self.minPCElist6 = []
        self.minFFlist1 = []
        self.minFFlist2 = []
        self.minFFlist4 = []
        self.minFFlist6 = []
        self.minUoclist1 = []
        self.minUoclist2 = []
        self.minUoclist4 = []
        self.minUoclist6 = []
        self.minj_cslist1 = []
        self.minj_cslist2 = []
        self.minj_cslist4 = []
        self.minj_cslist6 = []
        self.read()

    def read(self):
        for i in range(0,len(csv_files)):
            df = pd.read_csv(csv_files[i])
            df.reset_index(drop=False, inplace=True)
            df.drop(df.index[0:1], axis=0, inplace=True)
            df.drop(['U', 'I'], axis = 1, inplace = True)
            df.rename({'level_0': 'U', 'level_1': 'I'}, axis=1, inplace=True)
            df['U'] = df['U'].astype(float)
            df['I'] = df['I'].astype(float)

            df['j'] = df['I'] * 1000 / 0.09
            j_cs = df.loc[df['U'] == df['U'].abs().min(), 'j'].iloc[0]
            myList = df["j"].tolist()
            min_val, idx = min([(abs(val), idx) for (idx, val) in enumerate(myList)])
            U_oc = df.iloc[idx]['U']
            self.Uoc = U_oc
            self.FF = df['U'].max() * df['j'].max() / j_cs * U_oc
            self.j_cs = j_cs
            self.santykis = float(csv_files[i][-7:-4])
            self.PCE = min(df['j'] * df['U']/100)
            self.apskaiciuoti_pce()
            self.apskaiciuoti_ff()
            self.apskaiciuoti_Uoc()
            self.apskaiciuoti_j_cs()

    def apskaiciuoti_pce(self):

        if self.santykis == 0.1:
            self.minPCElist1.append(self.PCE * -100)
        elif self.santykis == 0.2:
            self.minPCElist2.append(self.PCE * -100)
        elif self.santykis == 0.4:
            self.minPCElist4.append(self.PCE * -100)
        elif self.santykis == 0.6:
            self.minPCElist6.append(self.PCE * -100)

    def apskaiciuoti_ff(self):

        if self.santykis == 0.1:
            self.minFFlist1.append(self.FF * -1)
        elif self.santykis == 0.2:
            self.minFFlist2.append(self.FF* -1)
        elif self.santykis == 0.4:
            self.minFFlist4.append(self.FF* -1)
        elif self.santykis == 0.6:
            self.minFFlist6.append(self.FF* -1)

    def apskaiciuoti_Uoc(self):

        if self.santykis == 0.1:
            self.minUoclist1.append(self.Uoc)
        elif self.santykis == 0.2:
            self.minUoclist2.append(self.Uoc)
        elif self.santykis == 0.4:
            self.minUoclist4.append(self.Uoc)
        elif self.santykis == 0.6:
            self.minUoclist6.append(self.Uoc)

    def apskaiciuoti_j_cs(self):

        if self.santykis == 0.1:
            self.minj_cslist1.append(self.j_cs )
        elif self.santykis == 0.2:
            self.minj_cslist2.append(self.j_cs )
        elif self.santykis == 0.4:
            self.minj_cslist4.append(self.j_cs )
        elif self.santykis == 0.6:
            self.minj_cslist6.append(self.j_cs )


    def atvaizduoti_pce(self):
        fig, ax = plt.subplots()
        bp1 = ax.boxplot(a.minPCElist1, positions=[1], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C0"))
        bp2 = ax.boxplot(a.minPCElist2, positions=[2], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C2"))
        bp3 = ax.boxplot(a.minPCElist4, positions=[3], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C1"))
        bp4 = ax.boxplot(a.minPCElist6, positions=[4], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C3"))

        ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0], bp4["boxes"][0]], ['0.1', '0.2', '0.4', '0.6'],
                  loc='upper right')
        ax.set_title("PSE")

        ax.set_xlim(0, 6)
        plt.show()

    def atvaizduoti_ff(self):
        fig, ax = plt.subplots()
        bp1 = ax.boxplot(a.minFFlist1, positions=[1], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C0"))
        bp2 = ax.boxplot(a.minFFlist2, positions=[2], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C2"))
        bp3 = ax.boxplot(a.minFFlist4, positions=[3], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C1"))
        bp4 = ax.boxplot(a.minFFlist6, positions=[4], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C3"))

        ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0], bp4["boxes"][0]], ['0.1', '0.2', '0.4', '0.6'],
                  loc='upper right')
        ax.set_title('FF')

        ax.set_xlim(0, 6)
        plt.show()

    def atvaizduoti_Uoc(self):
        fig, ax = plt.subplots()
        bp1 = ax.boxplot(a.minUoclist1, positions=[1], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C0"))
        bp2 = ax.boxplot(a.minUoclist2, positions=[2], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C2"))
        bp3 = ax.boxplot(a.minUoclist4, positions=[3], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C1"))
        bp4 = ax.boxplot(a.minUoclist6, positions=[4], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C3"))

        ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0], bp4["boxes"][0]], ['0.1', '0.2', '0.4', '0.6'],
                  loc='upper right')
        ax.set_title('Uoc')

        ax.set_xlim(0, 6)
        plt.show()

    def atvaizduoti_j_cs(self):
        fig, ax = plt.subplots()
        bp1 = ax.boxplot(a.minj_cslist1, positions=[1], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C0"))
        bp2 = ax.boxplot(a.minj_cslist2, positions=[2], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C2"))
        bp3 = ax.boxplot(a.minj_cslist4, positions=[3], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C1"))
        bp4 = ax.boxplot(a.minj_cslist6, positions=[4], widths=0.35,
                         patch_artist=True, boxprops=dict(facecolor="C3"))

        ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0], bp4["boxes"][0]], ['0.1', '0.2', '0.4', '0.6'],
                  loc='upper right')
        ax.set_title('j_cs')

        ax.set_xlim(0, 6)
        plt.show()




def grafikai():
    a.atvaizduoti_pce()
    a.atvaizduoti_Uoc()
    a.atvaizduoti_j_cs()
    a.atvaizduoti_ff()

a = SE(csv_files)
grafikai()









