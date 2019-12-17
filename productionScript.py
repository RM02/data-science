import matplotlib.pyplot as plt
import pandas as pd
import os

# This class builds data frame well
# well_list = ["BP-01", "BP-02", "BP-04", "BI-01", "BI-03", "AP-01", "AP-02", "AP-06", "AP-05", "AP-04", "BP-05", "EP-04", "EP-03", "EP-02", "EP-01", "BP-03", "AP-03"]
class Production:
    path = '/home/rafael/Documentos/Produccion_Petrolera_Data/DATOS_PRODUCCION/data_oil.xlsx'
    columns = ["BP-01", "BP-01 Np\n(BN)", "BP-01 Gp\n(PCN)", "BP-02", "BP-02 Np\n(BN)", "BP-02 Gp\n(PCN)", "BP-04", "BP-04 Np\n(BN)", "BP-04 Gp\n(PCN)", "BI-01", "BI-01 Np\n(BN)", "BI-01 Gp\n(PCN)", "BI-03", "BI-03 Np\n(BN)", "BI-03 Gp\n(PCN)", "AP-01", "AP-01 Np\n(BN)", "AP-01 Gp\n(PCN)", "AP-02", "AP-02 Np\n(BN)", "AP-02 Gp\n(PCN)", "AP-06", "AP-06 Np\n(BN)", "AP-06 Gp\n(PCN)", "AP-05", "AP-05 Np\n(BN)", "AP-05 Gp\n(PCN)", "AP-04", "AP-04 Np\n(BN)", "AP-04 Gp\n(PCN)", "BP-05", "BP-05 Np\n(BN)", "BP-05 Gp\n(PCN)", "EP-04", "EP-04 Np\n(BN)", "EP-04 Gp\n(PCN)", "EP-03", "EP-03 Np\n(BN)", "EP-03 Gp\n(PCN)", "EP-02", "EP-02 Np\n(BN)", "EP-02 Gp\n(PCN)", "EP-01", "EP-01 Np\n(BN)", "EP-01 Gp\n(PCN)", "BP-03", "BP-03 Np\n(BN)", "BP-03 Gp\n(PCN)", "AP-03", "AP-03 Np\n(BN)", "AP-03 Gp\n(PCN)"]
    filename = ''
    wellName = ''
    def __init__(self, well):
        self.wellName = well
        file = pd.read_excel(self.path, squeeze=True, header=None, sep="\t")
        data = pd.DataFrame(file)
        data.columns = self.columns
        data = data.drop([0], axis=0)
        self.data_set = data
    def Frame(self):
        #wellsFrames = []
        try:
            if self.wellName in self.data_set.columns:
                index = [i for i,x in enumerate(self.data_set.columns) if x in [self.wellName, self.wellName + " Np\n(BN)", self.wellName + " Gp\n(PCN)"]]
                frame = pd.DataFrame(self.data_set[self.data_set.columns[index]])
            #for element in self.data_set.columns:
            #    if self.wellName in element:
            #        data_frame = pd.DataFrame(self.data_set[element])
            #result = pd.concat([pd.to_datetime(wellsFrames[0], infer_datetime_format=True), pd.to_numeric(wellsFrames[1]), pd.to_numeric(wellsFrames[2])], axis=1).dropna()
            return frame
        except:
            print("Pozo no incluido en data set")
