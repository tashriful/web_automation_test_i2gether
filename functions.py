

# msc configuration checking
def msc_config_check(rows):
    commands = rows
    msc_flag = []
    msc_flag.clear()
    for row in commands:

        if "GT name  =  VLHS01_MSISDN_" in row:
            msc_flag.append('true')
        if "GT address information" in row:
            msc_flag.append('true')

        if "Load share DSP group name  =  SPS01_SPS02_LDSH" in row:
            msc_flag.append('true')

    return msc_flag

# Sps configuration checking
def sps_config_check(rows):
    commands = rows
    sps_flag = []
    sps_flag.clear()
    for row in commands:

        if "GT name  =  E.164_" in row:
            sps_flag.append('true')
        if "SCCP addressing policy name  =  VLHSS01_ALHSS01" in row:
            sps_flag.append('true')
        if "Address message  =  88" in row:
            sps_flag.append('true')

    return sps_flag

# MSC/SPS node cheking
def node_checker(rows,msc,sps):
    mscList = msc
    spsList = sps

    commands = rows
    for row in commands:
        if 'NE :' in row:
            x = row.split(":")
            x = x[1].strip()
            for msc in mscList:
                if x in msc:
                    status = "msc"
                    return status
            for sps in spsList:
                if x in sps:
                    status = "sps"
                    return status


# matching result cheking...numbers are defined or not
def number_defined_check(row):
    k = 0
    for line in row:

        if "RETCODE = 0" in line:
            if 'No matching result is found' == row[k+2]:
                return "Number Not Defined"
            else:
                return "Number Defined"
        k = k+1