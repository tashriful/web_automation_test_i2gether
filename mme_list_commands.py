
import pandas as pd
# import run_rnc_scripts_ericsson
# from utils.logger import Logger
# from workflow import config

class MmllistCommands:

    def __init__(self):
        loc = ("C:/Users/123/Downloads/Tac Define/tac2.xlsx")
        # mmeloc = ("E:/RPA/mme.xlsx")
        self.data = pd.read_excel(loc, 'Sheet1')
        # self.mmedata = pd.read_excel(mmeloc,'Sheet1')
        self.size = self.data['Unnamed: 0'].size


    def planfile_format_get(self):
        i = 1
        g = self.data.columns.get_loc("ADD DNSN for S11")
        print(g)
        print(self.data.nrows)



    def step01_mme3G(self):
        i = 1
        j = 0
        output = []
        # print(self.data.columns)
        g = self.data.columns.get_loc("ADD LAIVLR")
        print(g)
        while i < len(self.data):
            if self.data.iloc[i,g] == '' or pd.isna(self.data.iloc[i,g]) :
                break
            rnc = self.data.iloc[i, g]
            lai = self.data.iloc[i, g + 1]
            msc = self.data.iloc[i, g + 2]
            vlrn = self.data.iloc[i, g + 3]
            result = f"""LST LAIVLR:BGNLAI="{lai}",VLRNO="{vlrn}";"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step02_mme3G(self):
        i = 1
        j = 0
        output = []
        # print(self.data.columns)
        g = self.data.columns.get_loc("ADD DNSN for S11")
        # print(g)
        while i < len(self.data) - 1:
            if self.data.iloc[i,g] == '' or pd.isna(self.data.iloc[i,g]) :
                break
            fqdn = self.data.iloc[i, g + 4]
            hsindex = self.data.iloc[i, g + 5]

            result = f"""LST DNSN:FQDN="{fqdn}",HSINDEX={hsindex},ENTITY=SGW,INTYPE=S11;"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step03_mme3G(self):
        i = 1
        j = 0
        output = []
        # print(self.data.columns)
        g = self.data.columns.get_loc("ADD TALST")
        # print(g)
        while i < len(self.data) - 1:
            if self.data.iloc[i, g] == '' or pd.isna(self.data.iloc[i, g]):
                break
            tai = self.data.iloc[i, g + 1]
            lai = self.data.iloc[i, g + 4]

            result = f"""LST TAILAI:TAI="{tai}",LAI="{lai}";"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step04_mme3G(self):
        i = 1
        j = 0
        output = []
        # print(self.data.columns)
        g = self.data.columns.get_loc("ADD TALST")
        # print(g)
        while i < len(self.data) - 1:
            if self.data.iloc[i, g] == '' or pd.isna(self.data.iloc[i, g]):
                break
            taiId = self.data.iloc[i, g]
            tai = self.data.iloc[i, g + 1]
            description = self.data.iloc[i, g + 2]

            result = f""""LST TALST:TALISTID={taiId},TAI="{tai}";"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step05_mme3G(self):
        i = 1
        j = 0
        output = []
        # print(self.data.columns)
        g = self.data.columns.get_loc("ADD DNSN for S11")
        # print(g)
        while i < len(self.data) - 1:
            if self.data.iloc[i,g] == '' or pd.isna(self.data.iloc[i,g]) :
                break
            taiH = self.data.iloc[i, g+1]

            result = f""""LST AREAGPMEM:IDTYPE=TA,TAC="{taiH}"; """
            output.append(result)
            print(result)
            i += 1
        return output

    def step06_mme3G(self):
        i = 1
        j = 0
        output = []
        # print(self.data.columns)
        g = self.data.columns.get_loc("ADD Perfobj")
        # print(g)
        while i < len(self.data) - 1:
            if self.data.iloc[i,g] == '' or pd.isna(self.data.iloc[i,g]) :
                break
            taigroupNum = self.data.iloc[i, g + 1]

            result = f"""LST PERFOBJ:MOC=TAIGP,TAIGPN="{taigroupNum}";"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step07_mme3G(self):
        i = 1
        j = 0
        output = []
        # print(self.data.columns)
        g = self.data.columns.get_loc("ADD Perfobj")
        g1 = self.data.columns.get_loc("ADD TALST")
        # print(g)
        while i < len(self.data) - 1:
            if self.data.iloc[i,g] == '' or pd.isna(self.data.iloc[i,g]) :
                break
            taigroupNum = self.data.iloc[i, g + 1]
            Tai = self.data.iloc[i, g1 + 1]
            endTai = self.data.iloc[i, g + 3]

            result = f"""LST PERFOBJRULE:MOC=TAIGP,TAIGPN="{taigroupNum}",TAI="{Tai}";"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step08_09_mme3G(self):
        i = 0

        j = 0
        p, q = 0, 0
        output = []
        while i < len(self.data) - 1:
            i = i + 1
            j = 0
            while j < len(self.data.columns) - 1:
                if self.data.iloc[i, j] == 'ADD DNSN for S10 & Gn':
                    p, q = i, j
                j = j + 1
        p = p + 2
        while p < len(self.data):
            if self.data.iloc[p, q] == '' or pd.isna(self.data.iloc[p, q]):
                break
            fdqn = self.data.iloc[p, q + 4]
            hi = self.data.iloc[p, q + 5]

            result = f"""LST DNSN:FQDN="{fdqn}",HSINDEX={hi},ENTITY=MME,INTYPE=S10;"""
            result1 = f"""LST DNSN:FQDN="{fdqn}",HSINDEX={hi},ENTITY=MME,INTYPE=Gn;"""
            output.append(result)
            output.append(result1)
            print(result)
            print(result1)
            p = p + 1
        return output

    def step01_ADD(self):
        i = 1
        j = 0
        output = []
        # print(self.data.columns)
        colIndex = self.data.columns.get_loc("ADD LAIVLR")
        mmeIndex = 0  # fixed index
        while i < len(self.data) - 1:
            if self.data.iloc[i,colIndex] == '' or pd.isna(self.data.iloc[i,colIndex]) :
                break
            mmeName = self.data.iloc[i, mmeIndex]
            lai = self.data.iloc[i, colIndex + 1]
            vlrNo = self.data.iloc[i, colIndex + 3]

            result = f"""ADD LAIVLR: BGNLAI = "{lai}", ENDLAI = "{lai}", VLRNO = "{vlrNo}", DFLVLR = YES;[{mmeName}]"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step02_ADD(self):
        i = 1
        j = 0
        output = []
        colIndex = self.data.columns.get_loc("ADD DNSN for S11")
        mmeIndex = 0  # fixed index
        while i < len(self.data) - 1:
            if self.data.iloc[i,colIndex] == '' or pd.isna(self.data.iloc[i,colIndex]) :
                break
            mmeName = self.data.iloc[i, mmeIndex]
            fqdn = self.data.iloc[i, colIndex + 4]  # FQDN
            hi = self.data.iloc[i, colIndex + 5]  #HI
            priority = self.data.iloc[i, colIndex + 7]  #Priority
            weight = self.data.iloc[i, colIndex + 8]  #Weight
            description  = self.data.iloc[i, colIndex + 9]  #Description

            result =f"""ADD DNSN: FQDN = "{fqdn}", HSINDEX = {hi}, ENTITY = SGW, INTYPE = S11, S5PROTOCOL = GTP, S8PROTOCOL = GTP, PRIORITY = {priority}, WEIGHT = {weight}, DESC = "{description}";[{mmeName}]"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step03_ADD(self):
        i = 1
        j = 0
        output = []
        colIndex = self.data.columns.get_loc("ADD TALST")
        colIndexLai = self.data.columns.get_loc("ADD LAIVLR")
        mmeIndex = 0  # fixed index
        while i < len(self.data) - 1:
            if self.data.iloc[i, colIndex] == '' or pd.isna(self.data.iloc[i, colIndex]):
                break
            if self.data.iloc[i, colIndexLai] == '' or pd.isna(self.data.iloc[i, colIndexLai]):
                break
            mmeName = self.data.iloc[i, mmeIndex]
            tai = self.data.iloc[i, colIndex + 1]  # TAI
            lai = self.data.iloc[i, colIndexLai + 1]  # lai


            result =f"""ADD TAILAI: BGNTAI="{tai}", ENDTAI="{tai}", SUBRANGE=ALL_USER, LAI="{lai}";[{mmeName}]"""
            output.append(result)
            print(result)
            i += 1
        return output


    def step04_ADD(self):
        i = 1
        j = 0
        output = []
        colIndex = self.data.columns.get_loc("ADD TALST")
        mmeIndex = 0  # fixed index
        while i < len(self.data) - 1:
            if self.data.iloc[i, colIndex] == '' or pd.isna(self.data.iloc[i, colIndex]):
                break
            mmeName = self.data.iloc[i, mmeIndex]
            talID = self.data.iloc[i, colIndex]  # TAL ID
            tai = self.data.iloc[i, colIndex + 1]  # TAI


            result =f"""ADD TALST:TALISTID={talID},TAI="{tai}",DESC="RNC_DRH21 ";[{mmeName}]"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step05_ADD(self):
        i = 1
        j = 0
        output = []
        colIndex = self.data.columns.get_loc("ADD DNSN for S11")
        mmeIndex = 0  # fixed index
        while i < len(self.data) - 1:
            if self.data.iloc[i, colIndex] == '' or pd.isna(self.data.iloc[i, colIndex]):
                break
            mmeName = self.data.iloc[i, mmeIndex]
            tacH = self.data.iloc[i, colIndex+1]  # TAC H

            result =f"""ADD AREAGPMEM: AREAID=1, IDTYPE=TA, MCC="470", MNC="02", TAC="{tacH}";[{mmeName}]"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step06_ADD(self):
        i = 1
        j = 0
        output = []
        colIndex = self.data.columns.get_loc("ADD Perfobj")
        mmeIndex = 0  # fixed index
        while i < len(self.data) - 1:
            if self.data.iloc[i, colIndex] == '' or pd.isna(self.data.iloc[i, colIndex]):
                break
            mmeName = self.data.iloc[i, mmeIndex]
            tacGroupName = self.data.iloc[i, colIndex+1]  # TAI Group Name

            result = f"""ADD PERFOBJ: MOC=TAIGP, TAIGPN="{tacGroupName}";[{mmeName}]"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step07_ADD(self):
        i = 1
        j = 0
        output = []
        colIndex = self.data.columns.get_loc("ADD Perfobj")
        colIndexTalst = self.data.columns.get_loc("ADD TALST")
        mmeIndex = 0  # fixed index
        while i < len(self.data) - 1:
            if self.data.iloc[i, colIndex] == '' or pd.isna(self.data.iloc[i, colIndex]):
                break

            if self.data.iloc[i, colIndexTalst] == '' or pd.isna(self.data.iloc[i, colIndexTalst]):
                break

            mmeName = self.data.iloc[i, mmeIndex]
            tacGroupName = self.data.iloc[i, colIndex+1]  # TAI Group Name
            tai = self.data.iloc[i, colIndex+1]  # TAI

            result = f"""ADD PERFOBJRULE: MOC=TAIGP, TAIGPN="{tacGroupName}", BGNTAI="{tai}", ENDTAI="{tai}";[{mmeName}]"""
            output.append(result)
            print(result)
            i += 1
        return output

    def step08_09_ADD(self):
        i = 0

        j = 0
        p, q = 0, 0
        output = []
        while i < len(self.data) - 1:
            i = i + 1
            j = 0
            while j < len(self.data.columns) - 1:
                if self.data.iloc[i, j] == 'ADD DNSN for S10 & Gn':
                    p,q = i,j
                j = j + 1
        p = p + 2
        while p < len(self.data):
            if self.data.iloc[p, q] == '' or pd.isna(self.data.iloc[p, q]):
                break
            fdqn = self.data.iloc[p, q + 4]
            hi = self.data.iloc[p, q + 5]
            priority = self.data.iloc[p, q + 7]
            weight = self.data.iloc[p, q + 8]
            description = self.data.iloc[p, q + 9]

            result = f"""ADD DNSN:FQDN="{fdqn}",HSINDEX={hi},ENTITY=MME,INTYPE=S10,PRIORITY={priority},WEIGHT={weight},DESC="{description}";"""
            result1 = f"""ADD DNSN:FQDN="{fdqn}",HSINDEX={hi},ENTITY=MME,INTYPE=Gn,PRIORITY={priority},WEIGHT={weight},DESC="{description}";"""
            output.append(result)
            output.append(result1)
            print(result)
            print(result1)
            p = p + 1
        return output

    def mme_commands(self):
        self.step01_mme3G()
        self.step02_mme3G()
        self.step03_mme3G()
        self.step04_mme3G()
        self.step05_mme3G()
        self.step06_mme3G()
        self.step07_mme3G()
        self.step08_09_mme3G()
        print("-----------------ADD Script========================")
        self.step01_ADD()
        self.step02_ADD()
        self.step03_ADD()
        self.step04_ADD()
        self.step05_ADD()
        self.step06_ADD()
        self.step07_ADD()
        self.step08_09_ADD()
        print("-----------------Post verification========================")
        self.step01_mme3G()
        self.step02_mme3G()
        self.step03_mme3G()
        self.step04_mme3G()
        self.step05_mme3G()
        self.step06_mme3G()
        self.step07_mme3G()
        self.step08_09_mme3G()

