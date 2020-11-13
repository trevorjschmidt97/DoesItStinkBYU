from DoesItStinkBYUData import *

class Building:
    def __init__(self):
        self.buildingID = ''
        self.fullBuildingName = ''
        self.buildingLocationLat = 0.0
        self.buildingLocationLong = 0.0
class Bathroom:
    def __init__(self, bathroomID, buildingID, bathroomName, bathroomNumber, floorNumber):
        self.bathroomID = bathroomID
        self.buildingID = buildingID
        self.bathroomName = bathroomName
        self.bathroomNumber = bathroomNumber
        self.floorNumber = floorNumber
class Person:
    def __init__(self):
        import json
        import random
        import string
        import secrets

        print('\tCreating Random Person Data')
        self.mnames = []
        with open('mnames.json') as json_file:
            data = json.load(json_file)
            for p in data['data']:
                self.mnames.append(p)

        self.fnames = []
        with open('fnames.json') as json_file:
            data = json.load(json_file)
            for p in data['data']:
                self.fnames.append(p)

        self.snames = []
        with open('snames.json') as json_file:
            data = json.load(json_file)
            for p in data['data']:
                self.snames.append(p)

        self.firstName = ""
        self.lastName = self.snames[random.randrange(0, len(self.snames) - 1)]
        self.gender = ""
        if random.randint(0,1) == 0:
            self.gender = "f"
            self.firstName = self.fnames[random.randrange(0, len(self.fnames) - 1)]
        else:
            self.gender = "m"
            self.firstName = self.mnames[random.randrange(0, len(self.mnames) - 1)]

        self.username = self.firstName.lower() + self.lastName.lower() + str(random.randint(100000,9999999))

        alphabet = string.ascii_letters + string.digits
        self.password = ''.join(secrets.choice(alphabet) for i in range(12))

        self.birthYear = random.randint(1970, 2002)
        self.birthMonth = random.randint(1,12)
        self.birthDay = 1
        if self.birthMonth == 1 or self.birthMonth == 3 or self.birthMonth == 5 or self.birthMonth == 7 or self.birthMonth == 8 or self.birthMonth == 10 or self.birthMonth == 12:
            self.birthDay = random.randint(1,31)
        elif self.birthMonth == 4 or self.birthMonth == 6 or self.birthMonth == 9 or self.birthMonth == 11:
            self.birthDay = random.randint(1,30)
        else:
            self.birthDay = random.randint(1,28)

def populateAllBuildings():
    allBuildings = []

    ellb = Building()
    ellb.buildingID = "ELLB"
    ellb.fullBuildingName = "Leo B. Ellsworth Building"
    ellb.buildingLocationLat = 40.264398
    ellb.buildingLocationLong = -111.659417
    allBuildings.append(ellb)

    b67 = Building()
    b67.buildingID = "B67"
    b67.fullBuildingName = "B-67 Service Buildings"
    b67.buildingLocationLat = 40.262982 
    b67.buildingLocationLong = -111.657866
    allBuildings.append(b67)

    lves = Building()
    lves.buildingID = "LVES"
    lves.fullBuildingName = "Lavell Edwards Stadium"
    lves.buildingLocationLat = 40.257521 
    lves.buildingLocationLong = -111.654545
    allBuildings.append(lves)

    upc = Building()
    upc.buildingID = "UPC"
    upc.fullBuildingName = "University Parkway Center"
    upc.buildingLocationLat = 40.256293 
    upc.buildingLocationLong = -111.658064
    allBuildings.append(upc)

    flsr = Building()
    flsr.buildingID = "FLSR"
    flsr.fullBuildingName = "Foreign Language Student Residence"
    flsr.buildingLocationLat = 40.259723 
    flsr.buildingLocationLong = -111.642201
    allBuildings.append(flsr)

    shc = Building()
    shc.buildingID = "SHC"
    shc.fullBuildingName = "Student Health Center"
    shc.buildingLocationLat = 40.257787 
    shc.buildingLocationLong = -111.642620
    allBuildings.append(shc)

    upb = Building()
    upb.buildingID = "UPB"
    upb.fullBuildingName = "University Press Building"
    upb.buildingLocationLat = 40.257594 
    upb.buildingLocationLong = -111.645942
    allBuildings.append(upb)

    hceb = Building()
    hceb.buildingID = "HCEB"
    hceb.fullBuildingName = "Caroline Hemenway Harman Bldg. (Cont. Ed.)"
    hceb.buildingLocationLat = 40.256149 
    hceb.buildingLocationLong = -111.645416
    allBuildings.append(hceb)

    conf = Building()
    conf.buildingID = "CONF"
    conf.fullBuildingName = "BYU Conference Center"
    conf.buildingLocationLat = 40.255535 
    conf.buildingLocationLong = -111.645507
    allBuildings.append(conf)

    mlrp = Building()
    mlrp.buildingID = "MLRP"
    mlrp.fullBuildingName = "Miller Park (Baseball/Softball Complex)"
    mlrp.buildingLocationLat = 40.254999 
    mlrp.buildingLocationLong = -111.652465
    allBuildings.append(mlrp)

    byub = Building()
    byub.buildingID = "BYUB"
    byub.fullBuildingName = "BYU Broadcasting Building"
    byub.buildingLocationLat = 40.254553 
    byub.buildingLocationLong = -111.647700
    allBuildings.append(byub)

    mc = Building()
    mc.buildingID = "MC"
    mc.fullBuildingName = "J. Willard Marriott Center"
    mc.buildingLocationLat = 40.254065 
    mc.buildingLocationLong = -111.649316
    allBuildings.append(mc)

    mlbm = Building()
    mlbm.buildingID = "MLBM"
    mlbm.fullBuildingName = "Monte L. Bean Life Science Museum"
    mlbm.buildingLocationLat = 40.253394 
    mlbm.buildingLocationLong = -111.647335
    allBuildings.append(mlbm)

    itb = Building()
    itb.buildingID = "ITB"
    itb.fullBuildingName = "Information Technology Building"
    itb.buildingLocationLat = 40.252620 
    itb.buildingLocationLong = -111.657657
    allBuildings.append(itb)

    canc = Building()
    canc.buildingID = "CANC"
    canc.fullBuildingName = "Helaman Halls and Cannon Center (HI)"
    canc.buildingLocationLat = 40.252411 
    canc.buildingLocationLong = -111.652942
    allBuildings.append(canc)

    hc = Building()
    hc.buildingID = "HC"
    hc.fullBuildingName = "Hinckley Alumni and Visitors Center"
    hc.buildingLocationLat = 40.251785 
    hc.buildingLocationLong = -111.651694
    allBuildings.append(hc)

    asb = Building()
    asb.buildingID = "ASB"
    asb.fullBuildingName = "Abraham O. Smoot Administration Building"
    asb.buildingLocationLat = 40.250880 
    asb.buildingLocationLong = -111.649227
    allBuildings.append(asb)

    moa = Building()
    moa.buildingID = "MOA"
    moa.fullBuildingName = "Museum of Art"
    moa.buildingLocationLat = 40.250774 
    moa.buildingLocationLong = -111.647971
    allBuildings.append(moa)

    tnrb = Building()
    tnrb.buildingID = "TNRB"
    tnrb.fullBuildingName = "N. Eldon Tanner Building"
    tnrb.buildingLocationLat = 40.250446 
    tnrb.buildingLocationLong = -111.652261
    allBuildings.append(tnrb)

    hrcn = Building()
    hrcn.buildingID = "HRCN"
    hrcn.fullBuildingName = "Heritage Halls and Central Building (Hr)"
    hrcn.buildingLocationLat = 40.250647 
    hrcn.buildingLocationLong = -111.645172
    allBuildings.append(hrcn)

    cone = Building()
    cone.buildingID = "CONE"
    cone.fullBuildingName = "Creamery On Ninth East"
    cone.buildingLocationLat = 40.250082 
    cone.buildingLocationLong = -111.643547
    allBuildings.append(cone)

    tlrb = Building()
    tlrb.buildingID = "TLRB"
    tlrb.fullBuildingName = "John Taylor Building (Comprehensive Clinic)"
    tlrb.buildingLocationLat = 40.249312 
    tlrb.buildingLocationLong = -111.642587
    allBuildings.append(tlrb)

    jrcb = Building()
    jrcb.buildingID = "JRCB"
    jrcb.fullBuildingName = "J. Reuben Clark Building (Law School)"
    jrcb.buildingLocationLat = 40.249361 
    jrcb.buildingLocationLong = -111.645269
    allBuildings.append(jrcb)

    jkb = Building()
    jkb.buildingID = "JKB"
    jkb.fullBuildingName = "Jesse Knight Building"
    jkb.buildingLocationLat = 40.249947 
    jkb.buildingLocationLong = -111.649950
    allBuildings.append(jkb)

    tmcb = Building()
    tmcb.buildingID = "TMCB"
    tmcb.fullBuildingName = "Talmage Math Sciences / Computer Science Building"
    tmcb.buildingLocationLat = 40.249455 
    tmcb.buildingLocationLong = -111.650824
    allBuildings.append(tmcb)

    hfac = Building()
    hfac.buildingID = "HFAC"
    hfac.fullBuildingName = "FRANKLIN S. HARRIS FINE ARTS CENTER"
    hfac.buildingLocationLat = 40.249971 
    hfac.buildingLocationLong = -111.648000
    allBuildings.append(hfac)

    hbll = Building()
    hbll.buildingID = "HBLL"
    hbll.fullBuildingName = "Harold B. Lee Library"
    hbll.buildingLocationLat = 40.248804 
    hbll.buildingLocationLong = -111.649256
    allBuildings.append(hbll)

    wsc = Building()
    wsc.buildingID = "WSC"
    wsc.fullBuildingName = "Ernest L. Wilkinson Student Center"
    wsc.buildingLocationLat = 40.248526 
    wsc.buildingLocationLong = -111.647425
    allBuildings.append(wsc)

    jfsb = Building()
    jfsb.buildingID = "JFSB"
    jfsb.fullBuildingName = "Joseph F. Smith Building"
    jfsb.buildingLocationLat = 40.248428 
    jfsb.buildingLocationLong = -111.651204
    allBuildings.append(jfsb)

    rb = Building()
    rb.buildingID = "RB"
    rb.fullBuildingName = "Stephen L. Richards Building"
    rb.buildingLocationLat = 40.248935 
    rb.buildingLocationLong = -111.653491
    allBuildings.append(rb)

    sab = Building()
    sab.buildingID = "SAB"
    sab.fullBuildingName = "Student Athlete Building"
    sab.buildingLocationLat = 40.248198 
    sab.buildingLocationLong = -111.655316
    allBuildings.append(sab)

    ipf = Building()
    ipf.buildingID = "IPF"
    ipf.fullBuildingName = "Indoor Practice Facility"
    ipf.buildingLocationLat = 40.247183 
    ipf.buildingLocationLong = -111.656824
    allBuildings.append(ipf)

    sfh = Building()
    sfh.buildingID = "SFH"
    sfh.fullBuildingName = "George Albert Smith Fieldhouse"
    sfh.buildingLocationLat = 40.247400 
    sfh.buildingLocationLong = -111.654387
    allBuildings.append(sfh)

    msrb = Building()
    msrb.buildingID = "MSRB"
    msrb.fullBuildingName = "Karl G. Maeser Building"
    msrb.buildingLocationLat = 40.245381 
    msrb.buildingLocationLong = -111.653491
    allBuildings.append(msrb)

    hgb = Building()
    hgb.buildingID = "hgb"
    hgb.fullBuildingName = "Heber J. Grant Building"
    hgb.buildingLocationLat = 40.245467 
    hgb.buildingLocationLong = -111.652476
    allBuildings.append(hgb)

    brmb = Building()
    brmb.buildingID = "BRMB"
    brmb.fullBuildingName = "George H. Brimhall Building"
    brmb.buildingLocationLat = 40.246229 
    brmb.buildingLocationLong = -111.652348
    allBuildings.append(brmb)

    fph = Building()
    fph.buildingID = "FPH"
    fph.fullBuildingName = "Former Presidents' Home"
    fph.buildingLocationLat = 40.246634 
    fph.buildingLocationLong = -111.652829
    allBuildings.append(fph)

    mckb = Building()
    mckb.buildingID = "MCKB"
    mckb.fullBuildingName = "David O. McKay Building"
    mckb.buildingLocationLat = 40.247163 
    mckb.buildingLocationLong = -111.651830
    allBuildings.append(mckb)

    kmbl = Building()
    kmbl.buildingID = "KMBL"
    kmbl.fullBuildingName = "Spencer W. Kimball Tower"
    kmbl.buildingLocationLat = 40.247400 
    kmbl.buildingLocationLong = -111.651154
    allBuildings.append(kmbl)

    jsb = Building()
    jsb.buildingID = "JSB"
    jsb.fullBuildingName = "Joseph Smith Building"
    jsb.buildingLocationLat = 40.245860 
    jsb.buildingLocationLong = -111.651567
    allBuildings.append(jsb)

    esc = Building()
    esc.buildingID = "ESC"
    esc.fullBuildingName = "Carl F. Eyring Science Center"
    esc.buildingLocationLat = 40.247130 
    esc.buildingLocationLong = -111.650172
    allBuildings.append(esc)

    nicb = Building()
    nicb.buildingID = "NICB"
    nicb.fullBuildingName = "Joseph K. Nicholes Building"
    nicb.buildingLocationLat = 40.246368 
    nicb.buildingLocationLong = -111.650325
    allBuildings.append(nicb)

    bnsn = Building()
    bnsn.buildingID = "BNSN"
    bnsn.fullBuildingName = "Ezra Taft Benson Building"
    bnsn.buildingLocationLat = 40.245877 
    bnsn.buildingLocationLong = -111.650808
    allBuildings.append(bnsn)

    lsb = Building()
    lsb.buildingID = "LSB"
    lsb.fullBuildingName = "Life Science Building"
    lsb.buildingLocationLat = 40.245025 
    lsb.buildingLocationLong = -111.649294
    allBuildings.append(lsb)

    rmb = Building()
    rmb.buildingID = "RMB"
    rmb.fullBuildingName = "Risk Management Building"
    rmb.buildingLocationLat = 40.244022 
    rmb.buildingLocationLong = -111.650366
    allBuildings.append(rmb)

    hrcb = Building()
    hrcb.buildingID = "HRCB"
    hrcb.fullBuildingName = "Herald R. Clark Building"
    hrcb.buildingLocationLat = 40.247637 
    hrcb.buildingLocationLong = -111.649347
    allBuildings.append(hrcb)

    marb = Building()
    marb.buildingID = "MARB"
    marb.fullBuildingName = "Thomas L. Martin Building"
    marb.buildingLocationLat = 40.246843 
    marb.buildingLocationLong = -111.649251
    allBuildings.append(marb)

    cb = Building()
    cb.buildingID = "CB"
    cb.fullBuildingName = "W. W. Clyde Engineering Building"
    cb.buildingLocationLat = 40.246905 
    cb.buildingLocationLong = -111.648123
    allBuildings.append(cb)

    eb = Building()
    eb.buildingID = "EB"
    eb.fullBuildingName = "Engineering Building"
    eb.buildingLocationLat = 40.246262 
    eb.buildingLocationLong = -111.647925
    allBuildings.append(eb)

    ctb = Building()
    ctb.buildingID = "CTB"
    ctb.fullBuildingName = "Roland A. Crabtree Technology Building"
    ctb.buildingLocationLat = 40.247752 
    ctb.buildingLocationLong = -111.646513
    allBuildings.append(ctb)

    ppch = Building()
    ppch.buildingID = "PPCH"
    ppch.fullBuildingName = "Central Heating and Cooling Plants"
    ppch.buildingLocationLat = 40.247244 
    ppch.buildingLocationLong = -111.646261
    allBuildings.append(ppch)

    snlb = Building()
    snlb.buildingID = "SNLB"
    snlb.fullBuildingName = "William H. Snell Building"
    snlb.buildingLocationLat = 40.247396 
    snlb.buildingLocationLong = -111.645300
    allBuildings.append(snlb)

    cmb = Building()
    cmb.buildingID = "CMB"
    cmb.fullBuildingName = "Chemicals Management Building"
    cmb.buildingLocationLat = 40.247723 
    cmb.buildingLocationLong = -111.644548
    allBuildings.append(cmb)

    rotc = Building()
    rotc.buildingID = "ROTC"
    rotc.fullBuildingName = "Daniel H. Wells Building (Air Force / Army Reserve)"
    rotc.buildingLocationLat = 40.247965 
    rotc.buildingLocationLong = -111.644025
    allBuildings.append(rotc)

    b66 = Building()
    b66.buildingID = "B66"
    b66.fullBuildingName = "B-66 Classroom/Lab Building"
    b66.buildingLocationLat = 40.247224 
    b66.buildingLocationLong = -111.644594
    allBuildings.append(b66)

    brwb = Building()
    brwb.buildingID = "BRWB"
    brwb.fullBuildingName = "San F. Brewster Building"
    brwb.buildingLocationLat = 40.246466 
    brwb.buildingLocationLong = -111.645060
    allBuildings.append(brwb)

    csc = Building()
    csc.buildingID = "CSC"
    csc.fullBuildingName = "Culinary Support Center"
    csc.buildingLocationLat = 40.254442 
    csc.buildingLocationLong = -111.646198
    allBuildings.append(csc)

    return allBuildings
def populateBathrooms():
    allBathrooms =[]

    # ELLB BUILDING
    ellb110 = Bathroom(bathroomID="ellb110", buildingID="ellb", bathroomName="Men's/Single Use Restroom/Storage", bathroomNumber="110", floorNumber=1)
    allBathrooms.append(ellb110)

    ellb113 = Bathroom(bathroomID="ellb113", buildingID="ellb", bathroomName="Women's Restroom", bathroomNumber="113", floorNumber=1)
    allBathrooms.append(ellb113)

    ellb117 = Bathroom(bathroomID="ellb117", buildingID="ellb", bathroomName="Men's Restroom", bathroomNumber="117", floorNumber=1)
    allBathrooms.append(ellb117)

    ellb176A = Bathroom(bathroomID="ellb176A", buildingID="ellb", bathroomName="Single Use Restroom/Employee", bathroomNumber="176A", floorNumber=1)
    allBathrooms.append(ellb176A)

    ellb176B = Bathroom(bathroomID="ellb176B", buildingID="ellb", bathroomName="Single Use Restroom/Employee", bathroomNumber="176B", floorNumber=1)
    allBathrooms.append(ellb176B)

    ellb213 = Bathroom(bathroomID="ellb213", buildingID="ellb", bathroomName="Women's Restroom", bathroomNumber="213", floorNumber=2)
    allBathrooms.append(ellb213)

    ellb219 = Bathroom(bathroomID="ellb219", buildingID="ellb", bathroomName="Men's Restroom", bathroomNumber="219", floorNumber=2)
    allBathrooms.append(ellb219)

    # B67 BUILDING
    b67106 = Bathroom(bathroomID="b67106", buildingID="b67", bathroomName="Women's Restroom", bathroomNumber="106", floorNumber=1)
    allBathrooms.append(b67106)

    b67107 = Bathroom(bathroomID="b67107", buildingID="b67", bathroomName="Men's Restroom", bathroomNumber="107", floorNumber=1)
    allBathrooms.append(b67107)

    b67123A = Bathroom(bathroomID="b67123A", buildingID="b67", bathroomName="Single Use Restroom", bathroomNumber="123A", floorNumber=1)
    allBathrooms.append(b67123A)

    b67123B = Bathroom(bathroomID="b67123B", buildingID="b67", bathroomName="Single Use Restroom", bathroomNumber="123B", floorNumber=1)
    allBathrooms.append(b67123B)

    # LVES FLOOR 1
    lvesE140 = Bathroom(bathroomID="lvesE140", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="E140", floorNumber=1)
    allBathrooms.append(lvesE140)

    lvesE160 = Bathroom(bathroomID="lvesE160", buildingID="lves", bathroomName="Womens's Restroom", bathroomNumber="E160", floorNumber=1)
    allBathrooms.append(lvesE160)

    lvesE196 = Bathroom(bathroomID="lvesE196", buildingID="lves", bathroomName="Single Use Restroom", bathroomNumber="E196", floorNumber=1)
    allBathrooms.append(lvesE196)

    lvesL125 = Bathroom(bathroomID="lvesL125", buildingID="lves", bathroomName="Restroom Vestibule", bathroomNumber="L125", floorNumber=1)
    allBathrooms.append(lvesL125)

    lvesL125B = Bathroom(bathroomID="lvesL125B", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="L125B", floorNumber=1)
    allBathrooms.append(lvesL125B)

    lvesL127 = Bathroom(bathroomID="lvesL127", buildingID="lves", bathroomName="Restroom Vestibule", bathroomNumber="L127", floorNumber=1)
    allBathrooms.append(lvesL127)

    lvesL127B = Bathroom(bathroomID="lvesL127B", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="L127B", floorNumber=1)
    allBathrooms.append(lvesL127B)

    lvesN110 = Bathroom(bathroomID="lvesN110", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="N110", floorNumber=1)
    allBathrooms.append(lvesN110)

    lvesN120 = Bathroom(bathroomID="lvesN120", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="N120", floorNumber=1)
    allBathrooms.append(lvesN120)

    lvesN130 = Bathroom(bathroomID="lvesN130", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="N130", floorNumber=1)
    allBathrooms.append(lvesN130)

    lvesN140 = Bathroom(bathroomID="lvesN140", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="N140", floorNumber=1)
    allBathrooms.append(lvesN140)

    lvesN160 = Bathroom(bathroomID="lvesN160", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="N160", floorNumber=1)
    allBathrooms.append(lvesN160)

    lvesN170 = Bathroom(bathroomID="lvesN170", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="N170", floorNumber=1)
    allBathrooms.append(lvesN170)

    lvesN180 = Bathroom(bathroomID="lvesN180", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="N180", floorNumber=1)
    allBathrooms.append(lvesN180)

    lvesN190 = Bathroom(bathroomID="lvesN190", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="N190", floorNumber=1)
    allBathrooms.append(lvesN190)

    lvesS110 = Bathroom(bathroomID="lvesS110", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="S110", floorNumber=1)
    allBathrooms.append(lvesS110)

    lvesS120 = Bathroom(bathroomID="lvesS120", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="S120", floorNumber=1)
    allBathrooms.append(lvesS120)

    lvesS130 = Bathroom(bathroomID="lvesS130", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="S130", floorNumber=1)
    allBathrooms.append(lvesS130)

    lvesS140 = Bathroom(bathroomID="lvesS140", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="S140", floorNumber=1)
    allBathrooms.append(lvesS140)

    lvesS160 = Bathroom(bathroomID="lvesS160", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="S160", floorNumber=1)
    allBathrooms.append(lvesS160)

    lvesS170 = Bathroom(bathroomID="lvesS170", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="S170", floorNumber=1)
    allBathrooms.append(lvesS170)

    lvesS180 = Bathroom(bathroomID="lvesS180", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="S180", floorNumber=1)
    allBathrooms.append(lvesS180)

    lvesS190 = Bathroom(bathroomID="lvesS190", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="S190", floorNumber=1)
    allBathrooms.append(lvesS190)

    lvesW105A = Bathroom(bathroomID="lvesW105A", buildingID="lves", bathroomName="Women's Bathroom", bathroomNumber="W105A", floorNumber=1)
    allBathrooms.append(lvesW105A)

    lvesW105B = Bathroom(bathroomID="lvesW105B", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="W105B", floorNumber=1)
    allBathrooms.append(lvesW105B)

    lvesW105C = Bathroom(bathroomID="lvesW105C", buildingID="lves", bathroomName="Restroom Vestibule", bathroomNumber="W105C", floorNumber=1)
    allBathrooms.append(lvesW105C)

    lvesW118 = Bathroom(bathroomID="lvesW118", buildingID="lves", bathroomName="Single Use Restroom", bathroomNumber="W118", floorNumber=1)
    allBathrooms.append(lvesW118)

    lvesW120 = Bathroom(bathroomID="lvesW120", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="W120", floorNumber=1)
    allBathrooms.append(lvesW120)

    lvesW130 = Bathroom(bathroomID="lvesW130", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="W130", floorNumber=1)
    allBathrooms.append(lvesW130)

    lvesW131 = Bathroom(bathroomID="lvesW131", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="W131", floorNumber=1)
    allBathrooms.append(lvesW131)

    lvesW133 = Bathroom(bathroomID="lvesW133", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="W133", floorNumber=1)
    allBathrooms.append(lvesW133)

    lvesW190 = Bathroom(bathroomID="lvesW190", buildingID="lves", bathroomName="Restroom Vestibule", bathroomNumber="W190", floorNumber=1)
    allBathrooms.append(lvesW190)

    lvesW190A = Bathroom(bathroomID="lvesW190A", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="W190A", floorNumber=1)
    allBathrooms.append(lvesW190A)

    lvesW190B = Bathroom(bathroomID="lvesW190B", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="W190B", floorNumber=1)
    allBathrooms.append(lvesW190B)

    # LVES FLOOR 2
    lvesL231 = Bathroom(bathroomID="lvesL231", buildingID="lves", bathroomName="Restroom Vestibule", bathroomNumber="L231", floorNumber=2)
    allBathrooms.append(lvesL231)

    lvesL231B = Bathroom(bathroomID="lvesL231B", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="L231B", floorNumber=2)
    allBathrooms.append(lvesL231B)

    lvesL233 = Bathroom(bathroomID="lvesL233", buildingID="lves", bathroomName="Restroom Vestibule", bathroomNumber="L233", floorNumber=2)
    allBathrooms.append(lvesL233)

    lvesL233B = Bathroom(bathroomID="lves233B", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="L233B", floorNumber=2)
    allBathrooms.append(lvesL233B)

    lvesN210 = Bathroom(bathroomID="lvesN210", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="N210", floorNumber=2)
    allBathrooms.append(lvesN210)

    lvesN220 = Bathroom(bathroomID="lvesN220", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="N220", floorNumber=2)
    allBathrooms.append(lvesN220)

    lvesN222 = Bathroom(bathroomID="lvesN222", buildingID="lves", bathroomName="Single Use Restroom", bathroomNumber="N222", floorNumber=2)
    allBathrooms.append(lvesN222)

    lvesN232 = Bathroom(bathroomID="lvesN232", buildingID="lves", bathroomName="Single Use Restroom", bathroomNumber="N232", floorNumber=2)
    allBathrooms.append(lvesN232)

    lvesN240 = Bathroom(bathroomID="lvesN240", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="N240", floorNumber=2)
    allBathrooms.append(lvesN240)

    lvesN250 = Bathroom(bathroomID="lvesN250", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="N250", floorNumber=2)
    allBathrooms.append(lvesN250)

    lvesS210 = Bathroom(bathroomID="lvesS210", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="S210", floorNumber=2)
    allBathrooms.append(lvesS210)

    lvesS220 = Bathroom(bathroomID="lvesS220", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="S220", floorNumber=2)
    allBathrooms.append(lvesS220)

    lvesS222 = Bathroom(bathroomID="lvesS222", buildingID="lves", bathroomName="Single Use Restroom", bathroomNumber="S222", floorNumber=2)
    allBathrooms.append(lvesS222)

    lvesS232 = Bathroom(bathroomID="lvesS232", buildingID="lves", bathroomName="Single Use Restroom", bathroomNumber="S232", floorNumber=2)
    allBathrooms.append(lvesS232)

    lvesS240 = Bathroom(bathroomID="lvesS240", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="S240", floorNumber=2)
    allBathrooms.append(lvesS240)

    lvesS250 = Bathroom(bathroomID="lvesS250", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="S250", floorNumber=2)
    allBathrooms.append(lvesS250)

    lvesW272 = Bathroom(bathroomID="lvesW272", buildingID="lves", bathroomName="Single Use Restroom/Employee", bathroomNumber="W272", floorNumber=2)
    allBathrooms.append(lvesW272)

    # LVES FLOOR 3
    lvesE320 = Bathroom(bathroomID="lvesE320", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="E320", floorNumber=3)
    allBathrooms.append(lvesE320)

    lvesE330 = Bathroom(bathroomID="lvesE330", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="E330", floorNumber=3)
    allBathrooms.append(lvesE330)

    lvesE380 = Bathroom(bathroomID="lvesE380", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="E380", floorNumber=3)
    allBathrooms.append(lvesE380)

    lvesE390 = Bathroom(bathroomID="lvesE390", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="E390", floorNumber=3)
    allBathrooms.append(lvesE390)

    lvesL332 = Bathroom(bathroomID="lvesL332", buildingID="lves", bathroomName="Restroom Vestibule", bathroomNumber="L332", floorNumber=3)
    allBathrooms.append(lvesL332)

    lvesL332B = Bathroom(bathroomID="lvesL332B", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="L332B", floorNumber=3)
    allBathrooms.append(lvesL332B)

    lvesL362 = Bathroom(bathroomID="lvesL362", buildingID="lves", bathroomName="Single Use Women's Restroom", bathroomNumber="L362", floorNumber=3)
    allBathrooms.append(lvesL362)

    lvesW320 = Bathroom(bathroomID="lvesW320", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="W320", floorNumber=3)
    allBathrooms.append(lvesW320)

    lvesW330 = Bathroom(bathroomID="lvesW330", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="W330", floorNumber=3)
    allBathrooms.append(lvesW330)

    lvesW370 = Bathroom(bathroomID="lvesW370", buildingID="lves", bathroomName="Men's Restroom", bathroomNumber="W370", floorNumber=3)
    allBathrooms.append(lvesW370)

    lvesW380 = Bathroom(bathroomID="lvesW380", buildingID="lves", bathroomName="Women's Restroom", bathroomNumber="W380", floorNumber=3)
    allBathrooms.append(lvesW380)

    # UPC
    upc112 = Bathroom(bathroomID="upc112", buildingID="upc", bathroomName="Men's Restroom", bathroomNumber="112", floorNumber=1)
    allBathrooms.append(upc112)

    upc116 = Bathroom(bathroomID="upc116", buildingID="upc", bathroomName="Women's Restroom", bathroomNumber="116", floorNumber=1)
    allBathrooms.append(upc116)

    upc212 = Bathroom(bathroomID="upc212", buildingID="upc", bathroomName="Men's Restroom", bathroomNumber="212", floorNumber=2)
    allBathrooms.append(upc212)

    upc216 = Bathroom(bathroomID="upc216", buildingID="upc", bathroomName="Women's Restroom", bathroomNumber="216", floorNumber=2)
    allBathrooms.append(upc216)

    upc312 = Bathroom(bathroomID="upc312", buildingID="upc", bathroomName="Men's Restroom", bathroomNumber="312", floorNumber=3)
    allBathrooms.append(upc312)

    upc316 = Bathroom(bathroomID="upc316", buildingID="upc", bathroomName="Women's Restroom", bathroomNumber="316", floorNumber=3)
    allBathrooms.append(upc316)

    # FLSR
    flsrA107 = Bathroom(bathroomID="flsrA107", buildingID="flsr", bathroomName="Foyer To Bathroom (Stg)", bathroomNumber="A107", floorNumber=1)
    allBathrooms.append(flsrA107)

    flsrA109 = Bathroom(bathroomID="flsrA109", buildingID="flsr", bathroomName="Single Use Restroom", bathroomNumber="A109", floorNumber=1)
    allBathrooms.append(flsrA109)

    # SHC
    shc1037 = Bathroom(bathroomID="shc1037", buildingID="shc", bathroomName="Single Use Restroom/Employee", bathroomNumber="1037", floorNumber=1)
    allBathrooms.append(shc1037)

    shc1054 = Bathroom(bathroomID="shc1054", buildingID="shc", bathroomName="Men's Restroom", bathroomNumber="1054", floorNumber=1)
    allBathrooms.append(shc1054)

    shc1056 = Bathroom(bathroomID="shc1056", buildingID="shc", bathroomName="Women's Restroom", bathroomNumber="1056", floorNumber=1)
    allBathrooms.append(shc1056)

    shc1122 = Bathroom(bathroomID="shc1122", buildingID="shc", bathroomName="Single Use Restroom/Employee", bathroomNumber="1122", floorNumber=1)
    allBathrooms.append(shc1122)

    shc1319 = Bathroom(bathroomID="shc1319", buildingID="shc", bathroomName="Single Use Restroom/Employee", bathroomNumber="1319", floorNumber=1)
    allBathrooms.append(shc1319)

    shc1520 = Bathroom(bathroomID="shc1520", buildingID="shc", bathroomName="Single Use Restroom/Patient", bathroomNumber="1520", floorNumber=1)
    allBathrooms.append(shc1520)

    shc1524 = Bathroom(bathroomID="shc1524", buildingID="shc", bathroomName="Single Use Restroom/Patient", bathroomNumber="1524", floorNumber=1)
    allBathrooms.append(shc1524)

    shc2404 = Bathroom(bathroomID="shc2404", buildingID="shc", bathroomName="Women's Restroom", bathroomNumber="2404", floorNumber=2)
    allBathrooms.append(shc2404)

    shc2406 = Bathroom(bathroomID="shc2406", buildingID="shc", bathroomName="Men's Restroom", bathroomNumber="2406", floorNumber=2)
    allBathrooms.append(shc2406)


    # UPB BUILIDING
    upb226 = Bathroom(bathroomID="upb226", buildingID="upb", bathroomName="Women's Restroom", bathroomNumber="226", floorNumber=2)
    allBathrooms.append(upb226)

    upb227 = Bathroom(bathroomID="upb227", buildingID="upb", bathroomName="Men's Restroom", bathroomNumber="227", floorNumber=2)
    allBathrooms.append(upb227)

    upb263 = Bathroom(bathroomID="upb263", buildingID="upb", bathroomName="Men's Restroom", bathroomNumber="263", floorNumber=2)
    allBathrooms.append(upb263)

    upb267 = Bathroom(bathroomID="upb267", buildingID="upb", bathroomName="Women's Restroom", bathroomNumber="267", floorNumber=2)
    allBathrooms.append(upb267)

    upb267A = Bathroom(bathroomID="upb267A", buildingID="upb", bathroomName="Women's Lounge", bathroomNumber="267A", floorNumber=2)
    allBathrooms.append(upb267A)

    upb280A = Bathroom(bathroomID="upb280A", buildingID="upb", bathroomName="Men's Restroom", bathroomNumber="280A", floorNumber=2)
    allBathrooms.append(upb280A)

    upb281 = Bathroom(bathroomID="upb281", buildingID="upb", bathroomName="Women's Lounge", bathroomNumber="281", floorNumber=2)
    allBathrooms.append(upb281)

    upb281A = Bathroom(bathroomID="upb281A", buildingID="upb", bathroomName="Women's Restroom", bathroomNumber="281A", floorNumber=2)
    allBathrooms.append(upb281A)

    # HCEB BUILDING
    hcebB119 = Bathroom(bathroomID="hcebB119", buildingID="hceb", bathroomName="Men's Restroom", bathroomNumber="B119", floorNumber=0)
    allBathrooms.append(hcebB119)

    hcebB121 = Bathroom(bathroomID="hcebB121", buildingID="hceb", bathroomName="Women's Restroom", bathroomNumber="B121", floorNumber=0)
    allBathrooms.append(hcebB121)

    hceb120A = Bathroom(bathroomID="hceb120A", buildingID="hceb", bathroomName="Men's Restroom", bathroomNumber="120A", floorNumber=1)
    allBathrooms.append(hceb120A)

    hceb120C = Bathroom(bathroomID="hceb120C", buildingID="hceb", bathroomName="Women's Restroom", bathroomNumber="120C", floorNumber=1)
    allBathrooms.append(hceb120C)

    hceb218A = Bathroom(bathroomID="hceb218A", buildingID="hceb", bathroomName="Men's Restroom", bathroomNumber="218A", floorNumber=2)
    allBathrooms.append(hceb218A)

    hceb218C = Bathroom(bathroomID="hceb218C", buildingID="hceb", bathroomName="Women's Restroom", bathroomNumber="218C", floorNumber=2)
    allBathrooms.append(hceb218C)

    hceb222 = Bathroom(bathroomID="hceb222", buildingID="hceb", bathroomName="Single Use Bathroom", bathroomNumber="222", floorNumber=2)
    allBathrooms.append(hceb222)

    hceb244C = Bathroom(bathroomID="hceb244C", buildingID="hceb", bathroomName="Women's Restroom", bathroomNumber="244C", floorNumber=2)
    allBathrooms.append(hceb244C)

    hceb244E = Bathroom(bathroomID="hceb244E", buildingID="hceb", bathroomName="Men's Restroom", bathroomNumber="244E", floorNumber=2)
    allBathrooms.append(hceb244E)

    hceb318A = Bathroom(bathroomID="hceb318A", buildingID="hceb", bathroomName="Men's Restroom", bathroomNumber="318A", floorNumber=3)
    allBathrooms.append(hceb318A)

    hceb318C = Bathroom(bathroomID="hceb318C", buildingID="hceb", bathroomName="Women's Restroom", bathroomNumber="318C", floorNumber=3)
    allBathrooms.append(hceb318C)

    hceb344C = Bathroom(bathroomID="hceb344C", buildingID="hceb", bathroomName="Women's Restroom", bathroomNumber="344C", floorNumber=3)
    allBathrooms.append(hceb344C)

    hceb344E = Bathroom(bathroomID="hceb344E", buildingID="hceb", bathroomName="Men's Restroom", bathroomNumber="344E", floorNumber=3)
    allBathrooms.append(hceb344E)

    hceb418A = Bathroom(bathroomID="hceb418A", buildingID="hceb", bathroomName="Men's Restroom", bathroomNumber="418A", floorNumber=4)
    allBathrooms.append(hceb418A)

    hceb418C = Bathroom(bathroomID="hceb418C", buildingID="hceb", bathroomName="Women's Restroom", bathroomNumber="418C", floorNumber=4)
    allBathrooms.append(hceb418C)

    hceb444C = Bathroom(bathroomID="hceb444C", buildingID="hceb", bathroomName="Women's Restroom", bathroomNumber="444C", floorNumber=4)
    allBathrooms.append(hceb444C)

    hceb444E = Bathroom(bathroomID="hceb444E", buildingID="hceb", bathroomName="Men's Restroom", bathroomNumber="444E", floorNumber=4)
    allBathrooms.append(hceb444E)

    # CONF BUILDING
    conf1152 = Bathroom(bathroomID="conf1152", buildingID="conf", bathroomName="Restroom Vestibule", bathroomNumber="1152", floorNumber=1)
    allBathrooms.append(conf1152)

    conf1152A = Bathroom(bathroomID="conf1152A", buildingID="conf", bathroomName="Men's Restroom", bathroomNumber="1152A", floorNumber=1)
    allBathrooms.append(conf1152A)

    conf1154 = Bathroom(bathroomID="conf1154", buildingID="conf", bathroomName="Restroom Vestibule", bathroomNumber="1154", floorNumber=1)
    allBathrooms.append(conf1154)

    conf1154A = Bathroom(bathroomID="conf1154A", buildingID="conf", bathroomName="Women's Restroom", bathroomNumber="1154A", floorNumber=1)
    allBathrooms.append(conf1154A)

    conf1194 = Bathroom(bathroomID="conf1194", buildingID="conf", bathroomName="Restroom Vestibule", bathroomNumber="1194", floorNumber=1)
    allBathrooms.append(conf1194)

    conf1194A = Bathroom(bathroomID="conf1194A", buildingID="conf", bathroomName="Men's Restroom", bathroomNumber="1194A", floorNumber=1)
    allBathrooms.append(conf1194A)

    conf1196 = Bathroom(bathroomID="conf1196", buildingID="conf", bathroomName="Bathroom Vestibule", bathroomNumber="1196", floorNumber=1)
    allBathrooms.append(conf1196)

    conf1196A = Bathroom(bathroomID="conf1196A", buildingID="conf", bathroomName="Women's Restroom", bathroomNumber="1196A", floorNumber=1)
    allBathrooms.append(conf1196A)

    conf2271 = Bathroom(bathroomID="conf2271", buildingID="conf", bathroomName="Restroom Vestibule", bathroomNumber="2271", floorNumber=2)
    allBathrooms.append(conf2271)

    conf2271A = Bathroom(bathroomID="conf2271A", buildingID="conf", bathroomName="Men's Restroom", bathroomNumber="2271A", floorNumber=2)
    allBathrooms.append(conf2271A)

    conf2273 = Bathroom(bathroomID="conf2273", buildingID="conf", bathroomName="Restroom Vestibule", bathroomNumber="2273", floorNumber=2)
    allBathrooms.append(conf2273)

    conf2273A = Bathroom(bathroomID="conf2273A", buildingID="conf", bathroomName="Women's Restroom", bathroomNumber="2273A", floorNumber=2)
    allBathrooms.append(conf2273A)

    conf2291 = Bathroom(bathroomID="conf2291", buildingID="conf", bathroomName="Restroom Vestibule", bathroomNumber="2291", floorNumber=2)
    allBathrooms.append(conf2291)

    conf2291A = Bathroom(bathroomID="conf2291A", buildingID="conf", bathroomName="Men's Restroom", bathroomNumber="2291A", floorNumber=2)
    allBathrooms.append(conf2291A)

    conf2293 = Bathroom(bathroomID="conf2293", buildingID="conf", bathroomName="Restroom Vestibule", bathroomNumber="2293", floorNumber=2)
    allBathrooms.append(conf2293)

    conf2293A = Bathroom(bathroomID="conf2293A", buildingID="conf", bathroomName="Women's Restroom", bathroomNumber="2293A", floorNumber=2)
    allBathrooms.append(conf2293A)

    # MLRP BUILDING
    mlrp204 = Bathroom(bathroomID="mlrp204", buildingID="mlrp", bathroomName="Restroom Vestibule", bathroomNumber="204", floorNumber=2)
    allBathrooms.append(mlrp204)

    mlrp206 = Bathroom(bathroomID="mlrp206", buildingID="mlrp", bathroomName="Men's Restroom", bathroomNumber="206", floorNumber=2)
    allBathrooms.append(mlrp206)

    mlrp208 = Bathroom(bathroomID="mlrp208", buildingID="mlrp", bathroomName="Women's Restroom", bathroomNumber="208", floorNumber=2)
    allBathrooms.append(mlrp208)

    mlrp209 = Bathroom(bathroomID="mlrp209", buildingID="mlrp", bathroomName="Restroom Vestibule", bathroomNumber="209", floorNumber=2)
    allBathrooms.append(mlrp209)

    mlrp214 = Bathroom(bathroomID="mlrp214", buildingID="mlrp", bathroomName="Single Use Restroom", bathroomNumber="214", floorNumber=2)
    allBathrooms.append(mlrp214)

    mlrp216 = Bathroom(bathroomID="mlrp216", buildingID="mlrp", bathroomName="Single Use Restroom", bathroomNumber="216", floorNumber=2)
    allBathrooms.append(mlrp216)

    mlrp222 = Bathroom(bathroomID="mlrp222", buildingID="mlrp", bathroomName="Women's Restroom", bathroomNumber="222", floorNumber=2)
    allBathrooms.append(mlrp222)

    mlrp224 = Bathroom(bathroomID="mlrp224", buildingID="mlrp", bathroomName="Men's Restroom", bathroomNumber="224", floorNumber=2)
    allBathrooms.append(mlrp224)

    mlrp225 = Bathroom(bathroomID="mlrp225", buildingID="mlrp", bathroomName="Restroom Vestibule", bathroomNumber="225", floorNumber=2)
    allBathrooms.append(mlrp225)

    mlrp305 = Bathroom(bathroomID="mlrp305", buildingID="mlrp", bathroomName="Single Use Restroom / Press Box", bathroomNumber="305", floorNumber=3)
    allBathrooms.append(mlrp305)

    #BYUB BUILDING
    byub1013A = Bathroom(bathroomID="byub1013A", buildingID="byub", bathroomName="Men's Restroom", bathroomNumber="1013A", floorNumber=1)
    allBathrooms.append(byub1013A)

    byub1013C = Bathroom(bathroomID="byub1013C", buildingID="byub", bathroomName="Women's Restroom", bathroomNumber="1013C", floorNumber=1)
    allBathrooms.append(byub1013C)

    byub1134A = Bathroom(bathroomID="byub1134A", buildingID="byub", bathroomName="Single Use Restroom", bathroomNumber="1134A", floorNumber=1)
    allBathrooms.append(byub1134A)

    byub1134B = Bathroom(bathroomID="byub1134B", buildingID="byub", bathroomName="Single Use Restroom", bathroomNumber="1134B", floorNumber=1)
    allBathrooms.append(byub1134B)

    byub1226A = Bathroom(bathroomID="byub1126A", buildingID="byub", bathroomName="Women's Restroom", bathroomNumber="1126A", floorNumber=1)
    allBathrooms.append(byub1226A)

    byub1226C = Bathroom(bathroomID="byub1226C", buildingID="byub", bathroomName="Men's Restroom", bathroomNumber="1126C", floorNumber=1)
    allBathrooms.append(byub1226C)

    byub2122A = Bathroom(bathroomID="byub2122A", buildingID="byub", bathroomName="Women's Restroom", bathroomNumber="2122A", floorNumber=2)
    allBathrooms.append(byub2122A)

    byub2122C = Bathroom(bathroomID="byub2122C", buildingID="byub", bathroomName="Men's Restroom", bathroomNumber="2122C", floorNumber=2)
    allBathrooms.append(byub2122C)

    byub2208A = Bathroom(bathroomID="byub2208A", buildingID="byub", bathroomName="Men's Restroom", bathroomNumber="2208A", floorNumber=2)
    allBathrooms.append(byub2208A)

    byub2208C = Bathroom(bathroomID="byub2208C", buildingID="byub", bathroomName="Women's Restroom", bathroomNumber="2208C", floorNumber=2)
    allBathrooms.append(byub2208C)

    byub3140A = Bathroom(bathroomID="byub3140A", buildingID="byub", bathroomName="Men's Restroom", bathroomNumber="3140A", floorNumber=3)
    allBathrooms.append(byub3140A)

    byub3140C = Bathroom(bathroomID="byub3140C", buildingID="byub", bathroomName="Women's Restroom", bathroomNumber="3140C", floorNumber=3)
    allBathrooms.append(byub3140C)

    #CSC BUILDING
    csc62A = Bathroom(bathroomID="csc62A", buildingID="csc", bathroomName="Men's Restroom", bathroomNumber="62A", floorNumber=0)
    allBathrooms.append(csc62A)

    csc63 = Bathroom(bathroomID="csc63", buildingID="csc", bathroomName="Women's Restroom", bathroomNumber="63", floorNumber=0)
    allBathrooms.append(csc63)

    csc65A = Bathroom(bathroomID="csc65A", buildingID="csc", bathroomName="Women's Restroom", bathroomNumber="65A", floorNumber=0)
    allBathrooms.append(csc65A)

    csc105 = Bathroom(bathroomID="csc105", buildingID="csc", bathroomName="Single Use Restroom", bathroomNumber="105", floorNumber=1)
    allBathrooms.append(csc105)

    csc177 = Bathroom(bathroomID="csc177", buildingID="csc", bathroomName="Women's Restroom", bathroomNumber="177", floorNumber=1)
    allBathrooms.append(csc177)

    csc179 = Bathroom(bathroomID="csc179", buildingID="csc", bathroomName="Men's Restroom", bathroomNumber="179", floorNumber=1)
    allBathrooms.append(csc179)

    #MC BUILDING
    mc1148 = Bathroom(bathroomID="mc1148", buildingID="mc", bathroomName="Single Use Restroom/Press Staff", bathroomNumber="1148", floorNumber=1)
    allBathrooms.append(mc1148)

    mc2129 = Bathroom(bathroomID="mc2129", buildingID="mc", bathroomName="Single Use Restroom/Employee", bathroomNumber="2129", floorNumber=2)
    allBathrooms.append(mc2129)

    mc2135 = Bathroom(bathroomID="mc2135", buildingID="mc", bathroomName="Single Use Restroom/Employee", bathroomNumber="2135", floorNumber=2)
    allBathrooms.append(mc2135)

    mc3107 = Bathroom(bathroomID="mc3107", buildingID="mc", bathroomName="Men's Restroom", bathroomNumber="3107", floorNumber=3)
    allBathrooms.append(mc3107)

    mc3109 = Bathroom(bathroomID="mc3109", buildingID="mc", bathroomName="Women's Restroom", bathroomNumber="3109", floorNumber=3)
    allBathrooms.append(mc3109)

    mc3112 = Bathroom(bathroomID="mc3112", buildingID="mc", bathroomName="Men's Restroom", bathroomNumber="3112", floorNumber=3)
    allBathrooms.append(mc3112)

    mc3205 = Bathroom(bathroomID="mc3205", buildingID="mc", bathroomName="Women's Restroom", bathroomNumber="3205", floorNumber=3)
    allBathrooms.append(mc3205)

    mc3207 = Bathroom(bathroomID="mc3207", buildingID="mc", bathroomName="Men's Restroom", bathroomNumber="3207", floorNumber=3)
    allBathrooms.append(mc3207)

    mc3210 = Bathroom(bathroomID="mc3210", buildingID="mc", bathroomName="Women's Restroom", bathroomNumber="3210", floorNumber=3)
    allBathrooms.append(mc3210)

    mc3306 = Bathroom(bathroomID="mc3306", buildingID="mc", bathroomName="Men's Restroom", bathroomNumber="3306", floorNumber=3)
    allBathrooms.append(mc3306)

    mc3308 = Bathroom(bathroomID="mc3308", buildingID="mc", bathroomName="Women's Restroom", bathroomNumber="3308", floorNumber=3)
    allBathrooms.append(mc3308)

    mc3311 = Bathroom(bathroomID="mc3311", buildingID="mc", bathroomName="Men's Restroom", bathroomNumber="3311", floorNumber=3)
    allBathrooms.append(mc3311)

    mc3405 = Bathroom(bathroomID="mc3405", buildingID="mc", bathroomName="Women's Restroom", bathroomNumber="3405", floorNumber=3)
    allBathrooms.append(mc3405)

    mc3407 = Bathroom(bathroomID="mc3407", buildingID="mc", bathroomName="Men's Restroom", bathroomNumber="3407", floorNumber=3)
    allBathrooms.append(mc3407)

    mc3410 = Bathroom(bathroomID="mc3410", buildingID="mc", bathroomName="Women's Restroom", bathroomNumber="3410", floorNumber=3)
    allBathrooms.append(mc3410)

    # MLBM BUILDING
    mlbm1107 = Bathroom(bathroomID="mlbm1107", buildingID="mlbm", bathroomName="Men's Restroom", bathroomNumber="1107", floorNumber=1)
    allBathrooms.append(mlbm1107)

    mlbm1113 = Bathroom(bathroomID="mlbm1113", buildingID="mlbm", bathroomName="Women's Restroom", bathroomNumber="1113", floorNumber=1)
    allBathrooms.append(mlbm1113)

    mlbm2004 = Bathroom(bathroomID="mlbm2004", buildingID="mlbm", bathroomName="Women's Restroom", bathroomNumber="2004", floorNumber=2)
    allBathrooms.append(mlbm2004)

    mlbm2008 = Bathroom(bathroomID="mlbm2008", buildingID="mlbm", bathroomName="Men's Restroom", bathroomNumber="2008", floorNumber=2)
    allBathrooms.append(mlbm2008)

    mlbm2020 = Bathroom(bathroomID="mlbm2020", buildingID="mlbm", bathroomName="Men's Restroom", bathroomNumber="2020", floorNumber=2)
    allBathrooms.append(mlbm2020)

    mlbm2022 = Bathroom(bathroomID="mlbm2022", buildingID="mlbm", bathroomName="Women's Restroom", bathroomNumber="2022", floorNumber=2)
    allBathrooms.append(mlbm2022)

    # ITB BUILDING
    itb1019A = Bathroom(bathroomID="itb1019A", buildingID="itb", bathroomName="Men's Restroom", bathroomNumber="1019A", floorNumber=1)
    allBathrooms.append(itb1019A)

    itb1019B = Bathroom(bathroomID="itb1019B", buildingID="itb", bathroomName="Women's Restroom", bathroomNumber="1019B", floorNumber=1)
    allBathrooms.append(itb1019B)

    itb1019C = Bathroom(bathroomID="itb1019C", buildingID="itb", bathroomName="Shower", bathroomNumber="1019C", floorNumber=1)
    allBathrooms.append(itb1019C)

    itb1019D = Bathroom(bathroomID="itb1019D", buildingID="itb", bathroomName="Shower", bathroomNumber="1019D", floorNumber=1)
    allBathrooms.append(itb1019D)

    itb2005A = Bathroom(bathroomID="itb2005A", buildingID="itb", bathroomName="Men's Restroom", bathroomNumber="2005A", floorNumber=2)
    allBathrooms.append(itb2005A)

    itb2005B = Bathroom(bathroomID="itb2005B", buildingID="itb", bathroomName="Women's Restroom", bathroomNumber="2005B", floorNumber=2)
    allBathrooms.append(itb2005B)

    itb3005A = Bathroom(bathroomID="itb3005A", buildingID="itb", bathroomName="Men's Restroom", bathroomNumber="3005A", floorNumber=3)
    allBathrooms.append(itb3005A)

    itb3005B = Bathroom(bathroomID="itb3005B", buildingID="itb", bathroomName="Women's Restroom", bathroomNumber="3005B", floorNumber=3)
    allBathrooms.append(itb3005B)

    # CANC BUILDING
    canc121 = Bathroom(bathroomID="canc121", buildingID="canc", bathroomName="Women's Restroom", bathroomNumber="121", floorNumber=1)
    allBathrooms.append(canc121)

    canc122 = Bathroom(bathroomID="canc122", buildingID="canc", bathroomName="Men's Restroom", bathroomNumber="122", floorNumber=1)
    allBathrooms.append(canc122)

    canc123 = Bathroom(bathroomID="canc123", buildingID="canc", bathroomName="Single Use Restroom", bathroomNumber="123", floorNumber=1)
    allBathrooms.append(canc123)

    canc131 = Bathroom(bathroomID="canc131", buildingID="canc", bathroomName="Women's Restroom", bathroomNumber="131", floorNumber=1)
    allBathrooms.append(canc131)

    canc133 = Bathroom(bathroomID="canc133", buildingID="canc", bathroomName="Men's Restroom", bathroomNumber="133", floorNumber=1)
    allBathrooms.append(canc133)

    canc144 = Bathroom(bathroomID="canc144", buildingID="canc", bathroomName="Single Use Restroom And Lockers/Employee", bathroomNumber="144", floorNumber=1)
    allBathrooms.append(canc144)

    canc145 = Bathroom(bathroomID="canc145", buildingID="canc", bathroomName="Single Use Restroom And Lockers/Employee", bathroomNumber="145", floorNumber=1)
    allBathrooms.append(canc145)

    # HC BUILDING
    hcB17 = Bathroom(bathroomID="hcB17", buildingID="hc", bathroomName="Women's Restroom", bathroomNumber="B17", floorNumber=0)
    allBathrooms.append(hcB17)

    hcB21 = Bathroom(bathroomID="hcB21", buildingID="hc", bathroomName="Men's Restroom", bathroomNumber="B21", floorNumber=0)
    allBathrooms.append(hcB21)

    hcB59 = Bathroom(bathroomID="hcB59", buildingID="hc", bathroomName="Shower", bathroomNumber="B59", floorNumber=0)
    allBathrooms.append(hcB59)

    hc106 = Bathroom(bathroomID="hc106", buildingID="hc", bathroomName="Women's Restroom", bathroomNumber="106", floorNumber=1)
    allBathrooms.append(hc106)

    hc108 = Bathroom(bathroomID="hc108", buildingID="hc", bathroomName="Men's Restroom", bathroomNumber="108", floorNumber=1)
    allBathrooms.append(hc108)

    hc144 = Bathroom(bathroomID="hc144", buildingID="hc", bathroomName="Men's Restroom", bathroomNumber="144", floorNumber=1)
    allBathrooms.append(hc144)

    hc146 = Bathroom(bathroomID="hc146", buildingID="hc", bathroomName="Women's Restroom", bathroomNumber="146", floorNumber=1)
    allBathrooms.append(hc146)

    hc149 = Bathroom(bathroomID="hc149", buildingID="hc", bathroomName="Single Use Restroom", bathroomNumber="149", floorNumber=1)
    allBathrooms.append(hc149)

    hc151 = Bathroom(bathroomID="hc151", buildingID="hc", bathroomName="Single Use Restroom", bathroomNumber="151", floorNumber=1)
    allBathrooms.append(hc151)

    hc259 = Bathroom(bathroomID="hc259", buildingID="hc", bathroomName="Women's Restroom", bathroomNumber="259", floorNumber=2)
    allBathrooms.append(hc259)

    hc261 = Bathroom(bathroomID="hc261", buildingID="hc", bathroomName="Men's Restroom", bathroomNumber="261", floorNumber=2)
    allBathrooms.append(hc261)

    hc281 = Bathroom(bathroomID="hc281", buildingID="hc", bathroomName="Men's Restroom", bathroomNumber="281", floorNumber=2)
    allBathrooms.append(hc281)

    hc283 = Bathroom(bathroomID="hc283", buildingID="hc", bathroomName="Women's Restroom", bathroomNumber="283", floorNumber=2)
    allBathrooms.append(hc283)

    hc359 = Bathroom(bathroomID="hc359", buildingID="hc", bathroomName="Women's Restroom", bathroomNumber="359", floorNumber=3)
    allBathrooms.append(hc359)

    hc361 = Bathroom(bathroomID="hc361", buildingID="hc", bathroomName="Men's Restroom", bathroomNumber="361", floorNumber=3)
    allBathrooms.append(hc361)

    hc381 = Bathroom(bathroomID="hc381", buildingID="hc", bathroomName="Men's Restroom", bathroomNumber="381", floorNumber=3)
    allBathrooms.append(hc381)

    hc383 = Bathroom(bathroomID="hc383", buildingID="hc", bathroomName="Women's Restroom", bathroomNumber="383", floorNumber=3)
    allBathrooms.append(hc383)

    #ASB BUILDING
    asbA36 = Bathroom(bathroomID="asbA36", buildingID="asb", bathroomName="Restroom Vestibule", bathroomNumber="A36", floorNumber=0)
    allBathrooms.append(asbA36)

    asbA36A = Bathroom(bathroomID="asbA36A", buildingID="asb", bathroomName="Men's             Restroom", bathroomNumber="A36A", floorNumber=0)
    allBathrooms.append(asbA36A)

    asbB39 = Bathroom(bathroomID="asbB39", buildingID="asb", bathroomName="Women's Lounge", bathroomNumber="B39", floorNumber=0)
    allBathrooms.append(asbB39)

    asbB39A = Bathroom(bathroomID="asbB39A", buildingID="asb", bathroomName="Women's Restroom", bathroomNumber="B39A", floorNumber=0)
    allBathrooms.append(asbB39A)

    asbA138 = Bathroom(bathroomID="asbA138", buildingID="asb", bathroomName="Men's Restroom", bathroomNumber="A138", floorNumber=1)
    allBathrooms.append(asbA138)

    asbB135A = Bathroom(bathroomID="asbB135A", buildingID="asb", bathroomName="Women's Restroom", bathroomNumber="B135A", floorNumber=1)
    allBathrooms.append(asbB135A)

    asbC136 = Bathroom(bathroomID="asbC136", buildingID="asb", bathroomName="Women's Lounge", bathroomNumber="C136", floorNumber=1)
    allBathrooms.append(asbC136)

    asbC136A = Bathroom(bathroomID="asbC136A", buildingID="asb", bathroomName="Women's Restroom", bathroomNumber="C136A", floorNumber=1)
    allBathrooms.append(asbC136A)

    asbD137 = Bathroom(bathroomID="asbD137", buildingID="asb", bathroomName="Restroom Vestibule", bathroomNumber="D137", floorNumber=1)
    allBathrooms.append(asbD137)

    asbD137A = Bathroom(bathroomID="asbD137A", buildingID="asb", bathroomName="Men's Restroom", bathroomNumber="D137A", floorNumber=1)
    allBathrooms.append(asbD137A)

    asbA238 = Bathroom(bathroomID="asbA238", buildingID="asb", bathroomName="Restroom Vestibule", bathroomNumber="A238", floorNumber=2)
    allBathrooms.append(asbA238)

    asbA238A = Bathroom(bathroomID="asbA238A", buildingID="asb", bathroomName="Men's Restroom", bathroomNumber="A238A", floorNumber=2)
    allBathrooms.append(asbA238A)

    asbB237 = Bathroom(bathroomID="asbB237", buildingID="asb", bathroomName="Women's Restroom", bathroomNumber="B237", floorNumber=2)
    allBathrooms.append(asbB237)

    asbB237A = Bathroom(bathroomID="asbB237A", buildingID="asb", bathroomName="Women's Lounge", bathroomNumber="B237A", floorNumber=2)
    allBathrooms.append(asbB237A)

    asbC234 = Bathroom(bathroomID="asbC234", buildingID="asb", bathroomName="Restroom Vestibule & Lounge", bathroomNumber="C234", floorNumber=2)
    allBathrooms.append(asbC234)

    asbC234A = Bathroom(bathroomID="asbC234A", buildingID="asb", bathroomName="Women's Restroom", bathroomNumber="C234A", floorNumber=2)
    allBathrooms.append(asbC234A)

    asbD239 = Bathroom(bathroomID="asbD239", buildingID="asb", bathroomName="Restroom Vestibule", bathroomNumber="D239", floorNumber=2)
    allBathrooms.append(asbD239)

    asbD239A = Bathroom(bathroomID="asbD239A", buildingID="asb", bathroomName="Men's Restroom", bathroomNumber="D239A", floorNumber=2)
    allBathrooms.append(asbD239A)

    asbA336 = Bathroom(bathroomID="asbA336", buildingID="asb", bathroomName="Men's Restroom", bathroomNumber="A336", floorNumber=3)
    allBathrooms.append(asbA336)

    asbB339 = Bathroom(bathroomID="asbB339", buildingID="asb", bathroomName="Restroom Vestibule", bathroomNumber="B339", floorNumber=3)
    allBathrooms.append(asbB339)

    asbB339A = Bathroom(bathroomID="asbB339A", buildingID="asb", bathroomName="Women's Restroom", bathroomNumber="B339A", floorNumber=3)
    allBathrooms.append(asbB339A)

    asbC334 = Bathroom(bathroomID="asbC334", buildingID="asb", bathroomName="Single Use Restroom", bathroomNumber="C334", floorNumber=3)
    allBathrooms.append(asbC334)

    asbC336 = Bathroom(bathroomID="asbC336", buildingID="asb", bathroomName="Restroom Vestibule", bathroomNumber="C336", floorNumber=3)
    allBathrooms.append(asbC336)

    asbC336A = Bathroom(bathroomID="asbC336A", buildingID="asb", bathroomName="Women's Restroom", bathroomNumber="C336A", floorNumber=3)
    allBathrooms.append(asbC336A)

    asbD337 = Bathroom(bathroomID="asbD337", buildingID="asb", bathroomName="Restroom Vestibule", bathroomNumber="D337", floorNumber=3)
    allBathrooms.append(asbD337)

    asbD337A = Bathroom(bathroomID="asbD337A", buildingID="asb", bathroomName="Men's Restroom", bathroomNumber="D337A", floorNumber=3)
    allBathrooms.append(asbD337A)

    #MOA BUILDING
    moa154 = Bathroom(bathroomID="moa154", buildingID="moa", bathroomName="Men's Restroom/Employee", bathroomNumber="154", floorNumber=1)
    allBathrooms.append(moa154)

    moa154A = Bathroom(bathroomID="moa154A", buildingID="moa", bathroomName="Men's Restroom Shower Room", bathroomNumber="154A", floorNumber=1)
    allBathrooms.append(moa154A)

    moa154B = Bathroom(bathroomID="moa154B", buildingID="moa", bathroomName="Men's Restroom", bathroomNumber="154B", floorNumber=1)
    allBathrooms.append(moa154B)

    moa156 = Bathroom(bathroomID="moa156", buildingID="moa", bathroomName="Restroom Vestibule", bathroomNumber="156", floorNumber=1)
    allBathrooms.append(moa156)

    moa156A = Bathroom(bathroomID="moa156A", buildingID="moa", bathroomName="Women's Restroom Shower Room", bathroomNumber="156A", floorNumber=1)
    allBathrooms.append(moa156A)

    moa156B = Bathroom(bathroomID="moa156B", buildingID="moa", bathroomName="Women's Restroom/Employee", bathroomNumber="156B", floorNumber=1)
    allBathrooms.append(moa156B)

    moa272 = Bathroom(bathroomID="moa272", buildingID="moa", bathroomName="Restroom Vestibule", bathroomNumber="272", floorNumber=2)
    allBathrooms.append(moa272)

    moa272A = Bathroom(bathroomID="moa272A", buildingID="moa", bathroomName="Women's Restroom", bathroomNumber="272A", floorNumber=2)
    allBathrooms.append(moa272A)

    moa273 = Bathroom(bathroomID="moa273", buildingID="moa", bathroomName="Single Use Restroom", bathroomNumber="273", floorNumber=2)
    allBathrooms.append(moa273)

    moa276 = Bathroom(bathroomID="moa276", buildingID="moa", bathroomName="Restroom Vestibule", bathroomNumber="276", floorNumber=2)
    allBathrooms.append(moa276)

    moa276A = Bathroom(bathroomID="moa276A", buildingID="moa", bathroomName="Men's Restroom", bathroomNumber="276A", floorNumber=2)
    allBathrooms.append(moa276A)

    moa372A = Bathroom(bathroomID="moa372A", buildingID="moa", bathroomName="Men's Restroom", bathroomNumber="372A", floorNumber=3)
    allBathrooms.append(moa372A)

    moa376 = Bathroom(bathroomID="moa376", buildingID="moa", bathroomName="Restroom Vestibule", bathroomNumber="376", floorNumber=3)
    allBathrooms.append(moa376)

    moa376A = Bathroom(bathroomID="moa376A", buildingID="moa", bathroomName="Women's Restroom", bathroomNumber="376A", floorNumber=3)
    allBathrooms.append(moa376A)

    moa462 = Bathroom(bathroomID="moa462", buildingID="moa", bathroomName="Men's/Single Use Restroom/Employee", bathroomNumber="462", floorNumber=4)
    allBathrooms.append(moa462)

    moa464 = Bathroom(bathroomID="moa464", buildingID="moa", bathroomName="Women's/Single Use Restroom/Employee", bathroomNumber="464", floorNumber=4)
    allBathrooms.append(moa464)

    #TNRB BUILDING
    tnrb148 = Bathroom(bathroomID="tnrb148", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="148", floorNumber=1)
    allBathrooms.append(tnrb148)

    tnrb148A = Bathroom(bathroomID="tnrb148A", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="148A", floorNumber=1)
    allBathrooms.append(tnrb148A)

    tnrb150 = Bathroom(bathroomID="tnrb150", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="150", floorNumber=1)
    allBathrooms.append(tnrb150)

    tnrb150A = Bathroom(bathroomID="tnrb150A", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="150A", floorNumber=1)
    allBathrooms.append(tnrb150A)

    tnrbW104 = Bathroom(bathroomID="tnrbW104", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="W104", floorNumber=1)
    allBathrooms.append(tnrbW104)

    tnrbW104A = Bathroom(bathroomID="tnrbW104A", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="W104A", floorNumber=1)
    allBathrooms.append(tnrbW104A)

    tnrbW106 = Bathroom(bathroomID="tnrbW106", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="W106", floorNumber=1)
    allBathrooms.append(tnrbW106)

    tnrbW106A = Bathroom(bathroomID="tnrbW106A", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="W106A", floorNumber=1)
    allBathrooms.append(tnrbW106A)

    tnrbW141 = Bathroom(bathroomID="tnrbW141", buildingID="tnrb", bathroomName="Men's Changing Room", bathroomNumber="W141", floorNumber=1)
    allBathrooms.append(tnrbW141)

    tnrbW143 = Bathroom(bathroomID="tnrbW143", buildingID="tnrb", bathroomName="Women's Changing Room", bathroomNumber="W143", floorNumber=1)
    allBathrooms.append(tnrbW143)

    tnrb248 = Bathroom(bathroomID="tnrb248", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="248", floorNumber=2)
    allBathrooms.append(tnrb248)

    tnrb248A = Bathroom(bathroomID="tnrb248A", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="248A", floorNumber=2)
    allBathrooms.append(tnrb248A)

    tnrb250 = Bathroom(bathroomID="tnrb250", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="250", floorNumber=2)
    allBathrooms.append(tnrb250)

    tnrb250A = Bathroom(bathroomID="tnrb250A", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="250A", floorNumber=2)
    allBathrooms.append(tnrb250A)

    tnrbW204 = Bathroom(bathroomID="tnrbW204", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="W204", floorNumber=2)
    allBathrooms.append(tnrbW204)

    tnrbW204A = Bathroom(bathroomID="tnrbW204A", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="W204A", floorNumber=2)
    allBathrooms.append(tnrbW204A)

    tnrbW206 = Bathroom(bathroomID="tnrbW206", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="W206", floorNumber=2)
    allBathrooms.append(tnrbW206)

    tnrbW206A = Bathroom(bathroomID="tnrbW206A", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="W206A", floorNumber=2)
    allBathrooms.append(tnrbW206A)

    tnrb347 = Bathroom(bathroomID="tnrb347", buildingID="tnrb", bathroomName="Single Use Restroom", bathroomNumber="347", floorNumber=3)
    allBathrooms.append(tnrb347)

    tnrb348 = Bathroom(bathroomID="tnrb348", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="348", floorNumber=3)
    allBathrooms.append(tnrb348)

    tnrb348A = Bathroom(bathroomID="tnrb348A", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="348A", floorNumber=3)
    allBathrooms.append(tnrb348A)

    tnrb350 = Bathroom(bathroomID="tnrb350", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="350", floorNumber=3)
    allBathrooms.append(tnrb350)

    tnrb350A = Bathroom(bathroomID="tnrb350A", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="350A", floorNumber=3)
    allBathrooms.append(tnrb350A)

    tnrbW304 = Bathroom(bathroomID="tnrbW304", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="W304", floorNumber=3)
    allBathrooms.append(tnrbW304)

    tnrbW304A = Bathroom(bathroomID="tnrbW304A", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="W304A", floorNumber=3)
    allBathrooms.append(tnrbW304A)

    tnrbW306 = Bathroom(bathroomID="tnrbW306", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="W306", floorNumber=3)
    allBathrooms.append(tnrbW306)

    tnrbW306A = Bathroom(bathroomID="tnrbW306A", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="W306A", floorNumber=3)
    allBathrooms.append(tnrbW306A)

    tnrbW404 = Bathroom(bathroomID="tnrbW404", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="W404", floorNumber=4)
    allBathrooms.append(tnrbW404)

    tnrbW404A = Bathroom(bathroomID="tnrbW404A", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="W404A", floorNumber=4)
    allBathrooms.append(tnrbW404A)

    tnrbW406 = Bathroom(bathroomID="tnrbW406", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="W406", floorNumber=4)
    allBathrooms.append(tnrbW406)

    tnrbW406A = Bathroom(bathroomID="tnrbW406A", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="W406A", floorNumber=4)
    allBathrooms.append(tnrbW406A)

    tnrb596 = Bathroom(bathroomID="tnrb596", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="596", floorNumber=5)
    allBathrooms.append(tnrb596)

    tnrb596A = Bathroom(bathroomID="tnrb596A", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="596A", floorNumber=5)
    allBathrooms.append(tnrb596A)

    tnrb596P = Bathroom(bathroomID="tnrb596P", buildingID="tnrb", bathroomName="Women's Lounge", bathroomNumber="596P", floorNumber=5)
    allBathrooms.append(tnrb596P)

    tnrb598 = Bathroom(bathroomID="tnrb598", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="598", floorNumber=5)
    allBathrooms.append(tnrb598)

    tnrb598A = Bathroom(bathroomID="tnrb598A", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="598A", floorNumber=5)
    allBathrooms.append(tnrb598A)

    tnrb696 = Bathroom(bathroomID="tnrb696", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="696", floorNumber=6)
    allBathrooms.append(tnrb696)

    tnrb696A = Bathroom(bathroomID="tnrb696A", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="696A", floorNumber=6)
    allBathrooms.append(tnrb696A)

    tnrb698 = Bathroom(bathroomID="tnrb698", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="698", floorNumber=6)
    allBathrooms.append(tnrb698)

    tnrb698A = Bathroom(bathroomID="tnrb698A", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="698A", floorNumber=6)
    allBathrooms.append(tnrb698A)

    tnrb796 = Bathroom(bathroomID="tnrb796", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="796", floorNumber=7)
    allBathrooms.append(tnrb796)

    tnrb796A = Bathroom(bathroomID="tnrb796A", buildingID="tnrb", bathroomName="Women's Restroom", bathroomNumber="796A", floorNumber=7)
    allBathrooms.append(tnrb796A)

    tnrb796P = Bathroom(bathroomID="tnrb796P", buildingID="tnrb", bathroomName="Women's Lounge", bathroomNumber="796P", floorNumber=7)
    allBathrooms.append(tnrb796P)

    tnrb798 = Bathroom(bathroomID="tnrb798", buildingID="tnrb", bathroomName="Restroom Vestibule", bathroomNumber="798", floorNumber=7)
    allBathrooms.append(tnrb798)

    tnrb798A = Bathroom(bathroomID="tnrb798A", buildingID="tnrb", bathroomName="Men's Restroom", bathroomNumber="798A", floorNumber=7)
    allBathrooms.append(tnrb798A)

    # HRCN BUILDING
    hrcn122 = Bathroom(bathroomID="hrcn122", buildingID="hrcn", bathroomName="Women's Restroom", bathroomNumber="122", floorNumber=1)
    allBathrooms.append(hrcn122)

    hrcn124 = Bathroom(bathroomID="hrcn124", buildingID="hrcn", bathroomName="Men's Restroom", bathroomNumber="124", floorNumber=1)
    allBathrooms.append(hrcn124)

    hrcn130 = Bathroom(bathroomID="hrcn130", buildingID="hrcn", bathroomName="Single Use Restroom", bathroomNumber="130", floorNumber=1)
    allBathrooms.append(hrcn130)

    hrcn132 = Bathroom(bathroomID="hrcn132", buildingID="hrcn", bathroomName="Single Use Restroom In Kitchen", bathroomNumber="132", floorNumber=1)
    allBathrooms.append(hrcn132)

    hrcn211 = Bathroom(bathroomID="hrcn211", buildingID="hrcn", bathroomName="Women's Restroom", bathroomNumber="211", floorNumber=2)
    allBathrooms.append(hrcn211)

    hrcn215 = Bathroom(bathroomID="hrcn215", buildingID="hrcn", bathroomName="Men's Restroom", bathroomNumber="215", floorNumber=2)
    allBathrooms.append(hrcn215)

    # CONE BUILDING
    cone107 = Bathroom(bathroomID="cone107", buildingID="cone", bathroomName="Women's Restroom", bathroomNumber="107", floorNumber=1)
    allBathrooms.append(cone107)

    cone108 = Bathroom(bathroomID="cone108", buildingID="cone", bathroomName="Men's Restroom", bathroomNumber="108", floorNumber=1)
    allBathrooms.append(cone108)

    # HFAC BUILDING
    hfacC136 = Bathroom(bathroomID="hfacC136", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="C136", floorNumber=1)
    allBathrooms.append(hfacC136)

    hfacC162 = Bathroom(bathroomID="hfacC162", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="C162", floorNumber=1)
    allBathrooms.append(hfacC162)

    hfacD131B = Bathroom(bathroomID="hfacD131B", buildingID="hfac", bathroomName="Restroom In Women's Dressing Room", bathroomNumber="D131B", floorNumber=1)
    allBathrooms.append(hfacD131B)

    hfacD151B = Bathroom(bathroomID="hfacD151B", buildingID="hfac", bathroomName="Restroom In Men's Dressing Room", bathroomNumber="D151B", floorNumber=1)
    allBathrooms.append(hfacD151B)

    hfacD192A = Bathroom(bathroomID="hfacD192A", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="D192A", floorNumber=1)
    allBathrooms.append(hfacD192A)

    hfacD196A = Bathroom(bathroomID="hfacD196A", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="D196A", floorNumber=1)
    allBathrooms.append(hfacD196A)

    hfacC293B = Bathroom(bathroomID="hfacC293B", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="C293B", floorNumber=2)
    allBathrooms.append(hfacC293B)

    hfacC293C = Bathroom(bathroomID="hfacC293C", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="C293C", floorNumber=2)
    allBathrooms.append(hfacC293C)

    hfacD227 = Bathroom(bathroomID="hfacD227", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="D227", floorNumber=2)
    allBathrooms.append(hfacD227)

    hfacD227A = Bathroom(bathroomID="hfacD227A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="D227A", floorNumber=2)
    allBathrooms.append(hfacD227A)

    hfacD237 = Bathroom(bathroomID="hfacD237", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="D237", floorNumber=2)
    allBathrooms.append(hfacD237)

    hfacD237A = Bathroom(bathroomID="hfacD237A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="D237A", floorNumber=2)
    allBathrooms.append(hfacD237A)

    hfacE315 = Bathroom(bathroomID="hfacE315", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="E315", floorNumber=3)
    allBathrooms.append(hfacE315)

    hfacE315A = Bathroom(bathroomID="hfacE315A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="E315A", floorNumber=3)
    allBathrooms.append(hfacE315A)

    hfacE319 = Bathroom(bathroomID="hfacE319", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="E319", floorNumber=3)
    allBathrooms.append(hfacE319)

    hfacE319A = Bathroom(bathroomID="hfacE319A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="E319A", floorNumber=3)
    allBathrooms.append(hfacE319A)

    hfacF310 = Bathroom(bathroomID="hfacF310", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="F310", floorNumber=3)
    allBathrooms.append(hfacF310)

    hfacF310A = Bathroom(bathroomID="hfacF310A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="F310A", floorNumber=3)
    allBathrooms.append(hfacF310A)

    hfacF314 = Bathroom(bathroomID="hfacF314", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="F314", floorNumber=3)
    allBathrooms.append(hfacF314)

    hfacF314A = Bathroom(bathroomID="hfacF314A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="F314A", floorNumber=3)
    allBathrooms.append(hfacF314A)

    hfacA416 = Bathroom(bathroomID="hfacA416", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="A416", floorNumber=4)
    allBathrooms.append(hfacA416)

    hfacA420 = Bathroom(bathroomID="hfacA420", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="A420", floorNumber=4)
    allBathrooms.append(hfacA420)

    hfacA420A = Bathroom(bathroomID="hfacA420A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="A420A", floorNumber=4)
    allBathrooms.append(hfacA420A)

    hfacE425 = Bathroom(bathroomID="hfacE425", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="E425", floorNumber=4)
    allBathrooms.append(hfacE425)

    hfacE425A = Bathroom(bathroomID="hfacE425A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="E425A", floorNumber=4)
    allBathrooms.append(hfacE425A)

    hfacE429 = Bathroom(bathroomID="hfacE429", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="E429", floorNumber=4)
    allBathrooms.append(hfacE429)

    hfacE429A = Bathroom(bathroomID="hfacE429A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="E429A", floorNumber=4)
    allBathrooms.append(hfacE429A)

    hfacF416 = Bathroom(bathroomID="hfacF416", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="F416", floorNumber=4)
    allBathrooms.append(hfacF416)

    hfacF416A = Bathroom(bathroomID="hfacF416A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="F416A", floorNumber=4)
    allBathrooms.append(hfacF416A)

    hfacF420 = Bathroom(bathroomID="hfacF420", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="F420", floorNumber=4)
    allBathrooms.append(hfacF420)

    hfacF420A = Bathroom(bathroomID="hfacF420A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="F420A", floorNumber=4)
    allBathrooms.append(hfacF420A)

    hfacA516 = Bathroom(bathroomID="hfacA516", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="A516", floorNumber=5)
    allBathrooms.append(hfacA516)

    hfacA516A = Bathroom(bathroomID="hfacA516A", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="A516A", floorNumber=5)
    allBathrooms.append(hfacA516A)

    hfacE523 = Bathroom(bathroomID="hfacE523", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="E523", floorNumber=5)
    allBathrooms.append(hfacE523)

    hfacE523A = Bathroom(bathroomID="hfacE523A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="E523A", floorNumber=5)
    allBathrooms.append(hfacE523A)

    hfacE527 = Bathroom(bathroomID="hfacE527", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="E527", floorNumber=5)
    allBathrooms.append(hfacE527)

    hfacE527A = Bathroom(bathroomID="hfacE527A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="E527A", floorNumber=5)
    allBathrooms.append(hfacE527A)

    hfacF516 = Bathroom(bathroomID="hfacF516", buildingID="hfac", bathroomName="Men's Restroom", bathroomNumber="F516", floorNumber=5)
    allBathrooms.append(hfacF516)

    hfacF516A = Bathroom(bathroomID="hfacF516A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="F516A", floorNumber=5)
    allBathrooms.append(hfacF516A)

    hfacF520 = Bathroom(bathroomID="hfacF520", buildingID="hfac", bathroomName="Women's Restroom", bathroomNumber="F520", floorNumber=5)
    allBathrooms.append(hfacF520)

    hfacF520A = Bathroom(bathroomID="hfacF520A", buildingID="hfac", bathroomName="Restroom Vestibule", bathroomNumber="F520A", floorNumber=5)
    allBathrooms.append(hfacF520A)

    # JKB BUILDING
    jkb1019A = Bathroom(bathroomID="jkb1019A", buildingID="jkb", bathroomName="Women's Restroom", bathroomNumber="1019A", floorNumber=1)
    allBathrooms.append(jkb1019A)

    jkb1019C = Bathroom(bathroomID="jkb1019C", buildingID="jkb", bathroomName="Men's Restroom", bathroomNumber="1019C", floorNumber=1)
    allBathrooms.append(jkb1019C)

    jkb1113B = Bathroom(bathroomID="jkb1113B", buildingID="jkb", bathroomName="Men's Restroom", bathroomNumber="1113B", floorNumber=1)
    allBathrooms.append(jkb1113B)

    jkb1113D = Bathroom(bathroomID="jkb1113D", buildingID="jkb", bathroomName="Women's Restroom", bathroomNumber="1113D", floorNumber=1)
    allBathrooms.append(jkb1113D)

    jkb2017A = Bathroom(bathroomID="jkb2017A", buildingID="jkb", bathroomName="Women's Restroom", bathroomNumber="2017A", floorNumber=2)
    allBathrooms.append(jkb2017A)

    jkb2017B = Bathroom(bathroomID="jkb2017B", buildingID="jkb", bathroomName="Men's Restroom", bathroomNumber="2017B", floorNumber=2)
    allBathrooms.append(jkb2017B)

    jkb3017A = Bathroom(bathroomID="jkb3017A", buildingID="jkb", bathroomName="Men's Restroom", bathroomNumber="3017A", floorNumber=3)
    allBathrooms.append(jkb3017A)

    jkb3017C = Bathroom(bathroomID="jkb3017C", buildingID="jkb", bathroomName="Women's Restroom", bathroomNumber="3017C", floorNumber=3)
    allBathrooms.append(jkb3017C)

    jkb3119B = Bathroom(bathroomID="jkb3119B", buildingID="jkb", bathroomName="Men's Restroom", bathroomNumber="3119B", floorNumber=3)
    allBathrooms.append(jkb3119B)

    jkb3119D = Bathroom(bathroomID="jkb3119D", buildingID="jkb", bathroomName="Women's Restroom", bathroomNumber="3119D", floorNumber=3)
    allBathrooms.append(jkb3119D)

    jkb4091B = Bathroom(bathroomID="jkb4091B", buildingID="jkb", bathroomName="Men's Restroom", bathroomNumber="4091B", floorNumber=4)
    allBathrooms.append(jkb4091B)

    jkb4091D = Bathroom(bathroomID="jkb4091D", buildingID="jkb", bathroomName="Women's Restroom", bathroomNumber="4091D", floorNumber=4)
    allBathrooms.append(jkb4091D)

    # TLRB BUILDING
    tlrb142 = Bathroom(bathroomID="tlrb142", buildingID="tlrb", bathroomName="Women's Restroom", bathroomNumber="142", floorNumber=1)
    allBathrooms.append(tlrb142)

    tlrb146 = Bathroom(bathroomID="tlrb146", buildingID="tlrb", bathroomName="Men's Restroom", bathroomNumber="146", floorNumber=1)
    allBathrooms.append(tlrb146)

    tlrb251 = Bathroom(bathroomID="tlrb251", buildingID="tlrb", bathroomName="Men's Restroom", bathroomNumber="251", floorNumber=2)
    allBathrooms.append(tlrb251)

    tlrb252 = Bathroom(bathroomID="tlrb252", buildingID="tlrb", bathroomName="Women's Restroom", bathroomNumber="252", floorNumber=2)
    allBathrooms.append(tlrb252)

    #JRCB BUILDING
    jrcb142 = Bathroom(bathroomID="jrcb142", buildingID="jrcb", bathroomName="Men's Restroom", bathroomNumber="142", floorNumber=1)
    allBathrooms.append(jrcb142)

    jrcb151 = Bathroom(bathroomID="jrcb151", buildingID="jrcb", bathroomName="Women's Restroom", bathroomNumber="151", floorNumber=1)
    allBathrooms.append(jrcb151)

    jrcb230 = Bathroom(bathroomID="jrcb230", buildingID="jrcb", bathroomName="Women's Restroom", bathroomNumber="230", floorNumber=2)
    allBathrooms.append(jrcb230)

    jrcb232 = Bathroom(bathroomID="jrcb232", buildingID="jrcb", bathroomName="Men's Restroom", bathroomNumber="232", floorNumber=2)
    allBathrooms.append(jrcb232)

    jrcb264 = Bathroom(bathroomID="jrcb264", buildingID="jrcb", bathroomName="Women's Restroom", bathroomNumber="264", floorNumber=2)
    allBathrooms.append(jrcb264)

    jrcb266 = Bathroom(bathroomID="jrcb266", buildingID="jrcb", bathroomName="Men's Restroom", bathroomNumber="266", floorNumber=2)
    allBathrooms.append(jrcb266)

    jrcb269 = Bathroom(bathroomID="jrcb269", buildingID="jrcb", bathroomName="Single Use Restroom", bathroomNumber="269", floorNumber=2)
    allBathrooms.append(jrcb269)

    jrcb330 = Bathroom(bathroomID="jrcb330", buildingID="jrcb", bathroomName="Women's Restroom", bathroomNumber="330", floorNumber=3)
    allBathrooms.append(jrcb330)

    jrcb332 = Bathroom(bathroomID="jrcb332", buildingID="jrcb", bathroomName="Men's Restroom", bathroomNumber="332", floorNumber=3)
    allBathrooms.append(jrcb332)

    jrcb352 = Bathroom(bathroomID="jrcb352", buildingID="jrcb", bathroomName="Single Use Restroom", bathroomNumber="352", floorNumber=3)
    allBathrooms.append(jrcb352)

    jrcb356 = Bathroom(bathroomID="jrcb356", buildingID="jrcb", bathroomName="Single Use Restroom", bathroomNumber="356", floorNumber=3)
    allBathrooms.append(jrcb356)

    jrcb382 = Bathroom(bathroomID="jrcb382", buildingID="jrcb", bathroomName="Women's Restroom", bathroomNumber="382", floorNumber=3)
    allBathrooms.append(jrcb382)

    jrcb385 = Bathroom(bathroomID="jrcb385", buildingID="jrcb", bathroomName="Men's Restroom", bathroomNumber="385", floorNumber=3)
    allBathrooms.append(jrcb385)

    jrcb421A = Bathroom(bathroomID="jrcb421A", buildingID="jrcb", bathroomName="Women's Restroom", bathroomNumber="421A", floorNumber=4)
    allBathrooms.append(jrcb421A)

    jrcb429 = Bathroom(bathroomID="jrcb429", buildingID="jrcb", bathroomName="Men's Restroom", bathroomNumber="429", floorNumber=4)
    allBathrooms.append(jrcb429)

    jrcb521A = Bathroom(bathroomID="jrcb521A", buildingID="jrcb", bathroomName="Women's Restroom", bathroomNumber="521A", floorNumber=5)
    allBathrooms.append(jrcb521A)

    jrcb533 = Bathroom(bathroomID="jrcb533", buildingID="jrcb", bathroomName="Men's Restroom", bathroomNumber="533", floorNumber=5)
    allBathrooms.append(jrcb533)

    # HBLL BUILDING
    hbll1010 = Bathroom(bathroomID="hbll1010", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="1010", floorNumber=1)
    allBathrooms.append(hbll1010)

    hbll1020 = Bathroom(bathroomID="hbll1020", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="1020", floorNumber=1)
    allBathrooms.append(hbll1020)

    hbll1410 = Bathroom(bathroomID="hbll1410", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="1410", floorNumber=1)
    allBathrooms.append(hbll1410)

    hbll1411 = Bathroom(bathroomID="hbll1411", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="1411", floorNumber=1)
    allBathrooms.append(hbll1411)

    hbll2010 = Bathroom(bathroomID="hbll2010", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="2010", floorNumber=2)
    allBathrooms.append(hbll2010)

    hbll2020 = Bathroom(bathroomID="hbll2020", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="2020", floorNumber=2)
    allBathrooms.append(hbll2020)

    hbll2222 = Bathroom(bathroomID="hbll2222", buildingID="hbll", bathroomName="Single Use Restroom", bathroomNumber="2222", floorNumber=2)
    allBathrooms.append(hbll2222)

    hbll2313 = Bathroom(bathroomID="hbll2313", buildingID="hbll", bathroomName="Single Use Restroom", bathroomNumber="2313", floorNumber=2)
    allBathrooms.append(hbll2313)

    hbll2314 = Bathroom(bathroomID="hbll2314", buildingID="hbll", bathroomName="Single Use Restroom", bathroomNumber="2314", floorNumber=2)
    allBathrooms.append(hbll2314)

    hbll2410 = Bathroom(bathroomID="hbll2410", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="2410", floorNumber=2)
    allBathrooms.append(hbll2410)

    hbll2411 = Bathroom(bathroomID="hbll2411", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="2411", floorNumber=2)
    allBathrooms.append(hbll2411)

    hbll2603 = Bathroom(bathroomID="hbll2603", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="2603", floorNumber=2)
    allBathrooms.append(hbll2603)

    hbll2606 = Bathroom(bathroomID="hbll2606", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="2606", floorNumber=2)
    allBathrooms.append(hbll2606)

    hbll3038 = Bathroom(bathroomID="hbll3038", buildingID="hbll", bathroomName="Single Use Restroom/Security", bathroomNumber="3038", floorNumber=3)
    allBathrooms.append(hbll3038)

    hbll3421B = Bathroom(bathroomID="hbll3421B", buildingID="hbll", bathroomName="Infant Care Lounge", bathroomNumber="3421B", floorNumber=3)
    allBathrooms.append(hbll3421B)

    hbll3421E = Bathroom(bathroomID="hbll3421E", buildingID="hbll", bathroomName="Single Use Restroom", bathroomNumber="3421E", floorNumber=3)
    allBathrooms.append(hbll3421E)

    hbll3421F = Bathroom(bathroomID="hbll3421F", buildingID="hbll", bathroomName="Single Use Restroom", bathroomNumber="3421F", floorNumber=3)
    allBathrooms.append(hbll3421F)

    hbll3602 = Bathroom(bathroomID="hbll3602", buildingID="hbll", bathroomName="Restroom Vestibule", bathroomNumber="3602", floorNumber=3)
    allBathrooms.append(hbll3602)

    hbll3603 = Bathroom(bathroomID="hbll3603", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="3603", floorNumber=3)
    allBathrooms.append(hbll3603)

    hbll3606 = Bathroom(bathroomID="hbll3606", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="3606", floorNumber=3)
    allBathrooms.append(hbll3606)

    hbll3702 = Bathroom(bathroomID="hbll3702", buildingID="hbll", bathroomName="Men's Restroom Vestibule", bathroomNumber="3702", floorNumber=3)
    allBathrooms.append(hbll3702)

    hbll3703 = Bathroom(bathroomID="hbll3703", buildingID="hbll", bathroomName="Women's Restroom Vestibule", bathroomNumber="3703", floorNumber=3)
    allBathrooms.append(hbll3703)

    hbll3706 = Bathroom(bathroomID="hbll3706", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="3706", floorNumber=3)
    allBathrooms.append(hbll3706)

    hbll3708 = Bathroom(bathroomID="hbll3708", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="3708", floorNumber=3)
    allBathrooms.append(hbll3708)

    hbll4410 = Bathroom(bathroomID="hbll4410", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="4410", floorNumber=4)
    allBathrooms.append(hbll4410)

    hbll4411 = Bathroom(bathroomID="hbll4411", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="4411", floorNumber=4)
    allBathrooms.append(hbll4411)

    hbll4602 = Bathroom(bathroomID="hbll4602", buildingID="hbll", bathroomName="Women's Lounge", bathroomNumber="4602", floorNumber=4)
    allBathrooms.append(hbll4602)

    hbll4603 = Bathroom(bathroomID="hbll4603", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="4603", floorNumber=4)
    allBathrooms.append(hbll4603)

    hbll4606 = Bathroom(bathroomID="hbll4606", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="4606", floorNumber=4)
    allBathrooms.append(hbll4606)

    hbll5410 = Bathroom(bathroomID="hbll5410", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="5410", floorNumber=5)
    allBathrooms.append(hbll5410)

    hbll5411 = Bathroom(bathroomID="hbll5411", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="5411", floorNumber=5)
    allBathrooms.append(hbll5411)

    hbll5603 = Bathroom(bathroomID="hbll5603", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="5603", floorNumber=5)
    allBathrooms.append(hbll5603)

    hbll5606 = Bathroom(bathroomID="hbll5606", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="5606", floorNumber=5)
    allBathrooms.append(hbll5606)

    hbll6602 = Bathroom(bathroomID="hbll6602", buildingID="hbll", bathroomName="Women's Restroom", bathroomNumber="6602", floorNumber=6)
    allBathrooms.append(hbll6602)

    hbll6602A = Bathroom(bathroomID="hbll6602A", buildingID="hbll", bathroomName="Women's Lounge", bathroomNumber="6602A", floorNumber=6)
    allBathrooms.append(hbll6602A)

    hbll6606 = Bathroom(bathroomID="hbll6606", buildingID="hbll", bathroomName="Men's Restroom", bathroomNumber="6606", floorNumber=6)
    allBathrooms.append(hbll6606)

    #WSC BUILDING
    wsc1151C = Bathroom(bathroomID="wsc1151C", buildingID="wsc", bathroomName="Single Use Restroom At the Wall Employee", bathroomNumber="1151C", floorNumber=1)
    allBathrooms.append(wsc1151C)

    wsc1183 = Bathroom(bathroomID="wsc1183", buildingID="wsc", bathroomName="Women's Restroom Lounge", bathroomNumber="1183", floorNumber=1)
    allBathrooms.append(wsc1183)

    wsc1183A = Bathroom(bathroomID="wsc1183A", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="1183A", floorNumber=1)
    allBathrooms.append(wsc1183A)

    wsc1187 = Bathroom(bathroomID="wsc1187", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="1187", floorNumber=1)
    allBathrooms.append(wsc1187)

    wsc1402 = Bathroom(bathroomID="wsc1402", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="1402", floorNumber=1)
    allBathrooms.append(wsc1402)

    wsc1406 = Bathroom(bathroomID="wsc1406", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="1406", floorNumber=1)
    allBathrooms.append(wsc1406)

    wsc1945 = Bathroom(bathroomID="wsc1945", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="1945", floorNumber=1)
    allBathrooms.append(wsc1945)

    wsc1961A = Bathroom(bathroomID="wsc1961A", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="1961A", floorNumber=1)
    allBathrooms.append(wsc1961A)

    wsc2060 = Bathroom(bathroomID="wsc2060", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="2060", floorNumber=2)
    allBathrooms.append(wsc2060)

    wsc2080 = Bathroom(bathroomID="wsc2080", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="2080", floorNumber=2)
    allBathrooms.append(wsc2080)

    wsc2080A = Bathroom(bathroomID="wsc2080A", buildingID="wsc", bathroomName="Women's Lounge", bathroomNumber="2080A", floorNumber=2)
    allBathrooms.append(wsc2080A)

    wsc2144 = Bathroom(bathroomID="wsc2144", buildingID="wsc", bathroomName="Single Use Restroom", bathroomNumber="2144", floorNumber=2)
    allBathrooms.append(wsc2144)

    wsc2153 = Bathroom(bathroomID="wsc2153", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="2153", floorNumber=2)
    allBathrooms.append(wsc2153)

    wsc2157 = Bathroom(bathroomID="wsc2157", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="2157", floorNumber=2)
    allBathrooms.append(wsc2157)

    wsc2610 = Bathroom(bathroomID="wsc2610", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="2610", floorNumber=2)
    allBathrooms.append(wsc2610)

    wsc2624 = Bathroom(bathroomID="wsc2624", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="2624", floorNumber=2)
    allBathrooms.append(wsc2624)

    wsc3204 = Bathroom(bathroomID="wsc3204", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="3204", floorNumber=3)
    allBathrooms.append(wsc3204)

    wsc3212 = Bathroom(bathroomID="wsc3212", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="3212", floorNumber=3)
    allBathrooms.append(wsc3212)

    wsc3360 = Bathroom(bathroomID="wsc3360", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="3360", floorNumber=3)
    allBathrooms.append(wsc3360)

    wsc3364 = Bathroom(bathroomID="wsc3364", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="3364", floorNumber=3)
    allBathrooms.append(wsc3364)

    wsc3984 = Bathroom(bathroomID="wsc3984", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="3984", floorNumber=3)
    allBathrooms.append(wsc3984)

    wsc3985 = Bathroom(bathroomID="wsc3985", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="3985", floorNumber=3)
    allBathrooms.append(wsc3985)

    wsc4407 = Bathroom(bathroomID="wsc4407", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="4407", floorNumber=4)
    allBathrooms.append(wsc4407)

    wsc4409 = Bathroom(bathroomID="wsc4409", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="4409", floorNumber=4)
    allBathrooms.append(wsc4409)

    wsc5558 = Bathroom(bathroomID="wsc5558", buildingID="wsc", bathroomName="Single Use Restroom", bathroomNumber="5558", floorNumber=5)
    allBathrooms.append(wsc5558)

    wsc5560 = Bathroom(bathroomID="wsc5560", buildingID="wsc", bathroomName="Single Use Restroom", bathroomNumber="5560", floorNumber=5)
    allBathrooms.append(wsc5560)

    wsc6624 = Bathroom(bathroomID="wsc6624", buildingID="wsc", bathroomName="Men's Restroom", bathroomNumber="6624", floorNumber=6)
    allBathrooms.append(wsc6624)

    wsc6630 = Bathroom(bathroomID="wsc6630", buildingID="wsc", bathroomName="Women's Restroom", bathroomNumber="6630", floorNumber=6)
    allBathrooms.append(wsc6630)

    #JFSB BUILDING
    jfsbB021 = Bathroom(bathroomID="jfsbB021", buildingID="jfsb", bathroomName="Single Use Restroom", bathroomNumber="B021", floorNumber=0)
    allBathrooms.append(jfsbB021)

    jfsbB023 = Bathroom(bathroomID="jfsbB023", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="B023", floorNumber=0)
    allBathrooms.append(jfsbB023)

    jfsbB027 = Bathroom(bathroomID="jfsbB027", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="B027", floorNumber=0)
    allBathrooms.append(jfsbB027)

    jfsbB173 = Bathroom(bathroomID="jfsbB173", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="B173", floorNumber=0)
    allBathrooms.append(jfsbB173)

    jfsbB177 = Bathroom(bathroomID="jfsbB177", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="B177", floorNumber=0)
    allBathrooms.append(jfsbB177)

    jfsbB179 = Bathroom(bathroomID="jfsbB179", buildingID="jfsb", bathroomName="Single Use Restroom", bathroomNumber="B179", floorNumber=0)
    allBathrooms.append(jfsbB179)

    jfsb1075 = Bathroom(bathroomID="jfsb1075", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="1075", floorNumber=1)
    allBathrooms.append(jfsb1075)

    jfsb1079 = Bathroom(bathroomID="jfsb1079", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="1079", floorNumber=1)
    allBathrooms.append(jfsb1079)

    jfsb1121 = Bathroom(bathroomID="jfsb1121", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="1121", floorNumber=1)
    allBathrooms.append(jfsb1121)

    jfsb1125 = Bathroom(bathroomID="jfsb1125", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="1125", floorNumber=1)
    allBathrooms.append(jfsb1125)

    jfsb2022 = Bathroom(bathroomID="jfsb2022", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="2022", floorNumber=2)
    allBathrooms.append(jfsb2022)

    jfsb2026 = Bathroom(bathroomID="jfsb2026", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="2026", floorNumber=2)
    allBathrooms.append(jfsb2026)

    jfsb2072 = Bathroom(bathroomID="jfsb2072", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="2072", floorNumber=2)
    allBathrooms.append(jfsb2072)

    jfsb2076 = Bathroom(bathroomID="jfsb2076", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="2076", floorNumber=2)
    allBathrooms.append(jfsb2076)

    jfsb2122 = Bathroom(bathroomID="jfsb2122", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="2122", floorNumber=2)
    allBathrooms.append(jfsb2122)

    jfsb2126 = Bathroom(bathroomID="jfsb2126", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="2126", floorNumber=2)
    allBathrooms.append(jfsb2126)

    jfsb2172 = Bathroom(bathroomID="jfsb2172", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="2172", floorNumber=2)
    allBathrooms.append(jfsb2172)

    jfsb2176 = Bathroom(bathroomID="jfsb2176", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="2176", floorNumber=2)
    allBathrooms.append(jfsb2176)

    jfsb3022 = Bathroom(bathroomID="jfsb3022", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="3022", floorNumber=3)
    allBathrooms.append(jfsb3022)

    jfsb3026 = Bathroom(bathroomID="jfsb3026", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="3026", floorNumber=3)
    allBathrooms.append(jfsb3026)

    jfsb3072 = Bathroom(bathroomID="jfsb3072", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="3072", floorNumber=3)
    allBathrooms.append(jfsb3072)

    jfsb3076 = Bathroom(bathroomID="jfsb3076", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="3076", floorNumber=3)
    allBathrooms.append(jfsb3076)

    jfsb3122 = Bathroom(bathroomID="jfsb3122", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="3122", floorNumber=3)
    allBathrooms.append(jfsb3122)

    jfsb3126 = Bathroom(bathroomID="jfsb3126", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="3126", floorNumber=3)
    allBathrooms.append(jfsb3126)

    jfsb3172 = Bathroom(bathroomID="jfsb3172", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="3172", floorNumber=3)
    allBathrooms.append(jfsb3172)

    jfsb3176 = Bathroom(bathroomID="jfsb3176", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="3176", floorNumber=3)
    allBathrooms.append(jfsb3176)

    jfsb4022 = Bathroom(bathroomID="jfsb4022", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="4022", floorNumber=4)
    allBathrooms.append(jfsb4022)

    jfsb4026 = Bathroom(bathroomID="jfsb4026", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="4026", floorNumber=4)
    allBathrooms.append(jfsb4026)

    jfsb4072 = Bathroom(bathroomID="jfsb4072", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="4072", floorNumber=4)
    allBathrooms.append(jfsb4072)

    jfsb4076 = Bathroom(bathroomID="jfsb4076", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="4076", floorNumber=4)
    allBathrooms.append(jfsb4076)

    jfsb4122 = Bathroom(bathroomID="jfsb4122", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="4122", floorNumber=4)
    allBathrooms.append(jfsb4122)

    jfsb4126 = Bathroom(bathroomID="jfsb4126", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="4126", floorNumber=4)
    allBathrooms.append(jfsb4126)

    jfsb4172 = Bathroom(bathroomID="jfsb4172", buildingID="jfsb", bathroomName="Men's Restroom", bathroomNumber="4172", floorNumber=4)
    allBathrooms.append(jfsb4172)

    jfsb4176 = Bathroom(bathroomID="jfsb4176", buildingID="jfsb", bathroomName="Women's Restroom", bathroomNumber="4176", floorNumber=4)
    allBathrooms.append(jfsb4176)

    # RB BUILDING
    rb114 = Bathroom(bathroomID="rb114", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="114", floorNumber=1)
    allBathrooms.append(rb114)

    rb115 = Bathroom(bathroomID="rb115", buildingID="rb", bathroomName="Men's Restroom", bathroomNumber="115", floorNumber=1)
    allBathrooms.append(rb115)

    rb139H = Bathroom(bathroomID="rb139H", buildingID="rb", bathroomName="Men's Restroom", bathroomNumber="139H", floorNumber=1)
    allBathrooms.append(rb139H)

    rb161G = Bathroom(bathroomID="rb161G", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="161G", floorNumber=1)
    allBathrooms.append(rb161G)

    rb161H = Bathroom(bathroomID="rb161H", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="161H", floorNumber=1)
    allBathrooms.append(rb161H)

    rb161I = Bathroom(bathroomID="rb161I", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="161I", floorNumber=1)
    allBathrooms.append(rb161I)

    rb161J = Bathroom(bathroomID="rb161J", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="161J", floorNumber=1)
    allBathrooms.append(rb161J)

    rb161K = Bathroom(bathroomID="rb161K", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="161K", floorNumber=1)
    allBathrooms.append(rb161K)

    rb161L = Bathroom(bathroomID="rb161L", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="161L", floorNumber=1)
    allBathrooms.append(rb161L)

    rb161M = Bathroom(bathroomID="rb161M", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="161M", floorNumber=1)
    allBathrooms.append(rb161M)

    rb161N = Bathroom(bathroomID="rb161N", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="161N", floorNumber=1)
    allBathrooms.append(rb161N)

    rb180 = Bathroom(bathroomID="rb180", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="180", floorNumber=1)
    allBathrooms.append(rb180)

    rb182 = Bathroom(bathroomID="rb182", buildingID="rb", bathroomName="Men's Restroom", bathroomNumber="182", floorNumber=1)
    allBathrooms.append(rb182)

    rb1119 = Bathroom(bathroomID="rb1119", buildingID="rb", bathroomName="Single Use Restroom", bathroomNumber="1119", floorNumber=1)
    allBathrooms.append(rb1119)

    rb1121 = Bathroom(bathroomID="rb1121", buildingID="rb", bathroomName="Single Use Restroom", bathroomNumber="1121", floorNumber=1)
    allBathrooms.append(rb1121)

    rb204A = Bathroom(bathroomID="rb204A", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="204A", floorNumber=2)
    allBathrooms.append(rb204A)

    rb205 = Bathroom(bathroomID="rb205", buildingID="rb", bathroomName="Men's Restroom", bathroomNumber="205", floorNumber=2)
    allBathrooms.append(rb205)

    rb209C = Bathroom(bathroomID="rb209C", buildingID="rb", bathroomName="Single Use Restroom/Nursing Lab", bathroomNumber="209C", floorNumber=2)
    allBathrooms.append(rb209C)

    rb229M = Bathroom(bathroomID="rb229M", buildingID="rb", bathroomName="Single Use Restroom For Research Participants", bathroomNumber="229M", floorNumber=2)
    allBathrooms.append(rb229M)

    rb277A = Bathroom(bathroomID="rb277A", buildingID="rb", bathroomName="Men's Restroom", bathroomNumber="277A", floorNumber=2)
    allBathrooms.append(rb277A)

    rb277B = Bathroom(bathroomID="rb277B", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="277B", floorNumber=2)
    allBathrooms.append(rb277B)

    rb2207 = Bathroom(bathroomID="rb2207", buildingID="rb", bathroomName="Women's Restroom", bathroomNumber="2207", floorNumber=2)
    allBathrooms.append(rb2207)

    rb2209 = Bathroom(bathroomID="rb2209", buildingID="rb", bathroomName="Men's Restroom", bathroomNumber="2209", floorNumber=2)
    allBathrooms.append(rb2209)

    # SAB BUILDING
    sab103 = Bathroom(bathroomID="sab103", buildingID="sab", bathroomName="Men's Restroom", bathroomNumber="103", floorNumber=1)
    allBathrooms.append(sab103)

    sab104 = Bathroom(bathroomID="sab104", buildingID="sab", bathroomName="Women's Restroom", bathroomNumber="104", floorNumber=1)
    allBathrooms.append(sab104)

    sab109B = Bathroom(bathroomID="sab109B", buildingID="sab", bathroomName="Single Use Restroom - Inside Weight Room", bathroomNumber="109B", floorNumber=1)
    allBathrooms.append(sab109B)

    sab121G = Bathroom(bathroomID="sab121G", buildingID="sab", bathroomName="Alumni Restroom And Locker", bathroomNumber="121G", floorNumber=1)
    allBathrooms.append(sab121G)

    sab123M = Bathroom(bathroomID="sab123M", buildingID="sab", bathroomName="Men's Restroom", bathroomNumber="123M", floorNumber=1)
    allBathrooms.append(sab123M)

    sab123N = Bathroom(bathroomID="sab123N", buildingID="sab", bathroomName="Women's Restroom", bathroomNumber="123N", floorNumber=1)
    allBathrooms.append(sab123N)

    sab220A = Bathroom(bathroomID="sab220A", buildingID="sab", bathroomName="Single Use Restroom", bathroomNumber="220A", floorNumber=2)
    allBathrooms.append(sab220A)

    sab221 = Bathroom(bathroomID="sab221", buildingID="sab", bathroomName="Women's Restroom", bathroomNumber="221", floorNumber=2)
    allBathrooms.append(sab221)

    sab222 = Bathroom(bathroomID="sab222", buildingID="sab", bathroomName="Men's Restroom", bathroomNumber="222", floorNumber=2)
    allBathrooms.append(sab222)

    sab302 = Bathroom(bathroomID="sab302", buildingID="sab", bathroomName="Men's Restroom", bathroomNumber="302", floorNumber=3)
    allBathrooms.append(sab302)

    sab303 = Bathroom(bathroomID="sab303", buildingID="sab", bathroomName="Women's Restroom", bathroomNumber="303", floorNumber=3)
    allBathrooms.append(sab303)

    sab338 = Bathroom(bathroomID="sab338", buildingID="sab", bathroomName="Women's Restroom", bathroomNumber="338", floorNumber=3)
    allBathrooms.append(sab338)

    sab339 = Bathroom(bathroomID="sab339", buildingID="sab", bathroomName="Men's Restroom", bathroomNumber="339", floorNumber=3)
    allBathrooms.append(sab339)

    #SFH BUILDING
    sfh2 = Bathroom(bathroomID="sfh2", buildingID="sfh", bathroomName="Women's Restroom", bathroomNumber="2", floorNumber=0)
    allBathrooms.append(sfh2)

    sfh2B = Bathroom(bathroomID="sfh2B", buildingID="sfh", bathroomName="Restroom Vestibule", bathroomNumber="2B", floorNumber=0)
    allBathrooms.append(sfh2B)

    sfh8B = Bathroom(bathroomID="sfh8B", buildingID="sfh", bathroomName="Restroom In Locker Room", bathroomNumber="8B", floorNumber=0)
    allBathrooms.append(sfh8B)

    sfh30H = Bathroom(bathroomID="sfh30H", buildingID="sfh", bathroomName="Restroom Vestibule", bathroomNumber="30H", floorNumber=0)
    allBathrooms.append(sfh30H)

    sfh30J = Bathroom(bathroomID="sfh30J", buildingID="sfh", bathroomName="Single Use Restroom/Employee", bathroomNumber="30J", floorNumber=0)
    allBathrooms.append(sfh30J)

    sfh91 = Bathroom(bathroomID="sfh91", buildingID="sfh", bathroomName="Men's Restroom", bathroomNumber="91", floorNumber=0)
    allBathrooms.append(sfh91)

    sfh95 = Bathroom(bathroomID="sfh95", buildingID="sfh", bathroomName="Women's Restroom", bathroomNumber="95", floorNumber=0)
    allBathrooms.append(sfh95)

    sfh124C = Bathroom(bathroomID="sfh124C", buildingID="sfh", bathroomName="Men's Restroom", bathroomNumber="124C", floorNumber=1)
    allBathrooms.append(sfh124C)

    sfh126A = Bathroom(bathroomID="sfh126A", buildingID="sfh", bathroomName="Men's Restroom", bathroomNumber="126A", floorNumber=1)
    allBathrooms.append(sfh126A)

    sfh1110A = Bathroom(bathroomID="sfh1110A", buildingID="sfh", bathroomName="Women's Restroom", bathroomNumber="1110A", floorNumber=1)
    allBathrooms.append(sfh1110A)

    sfh1110D = Bathroom(bathroomID="sfh1110D", buildingID="sfh", bathroomName="Women's Restroom", bathroomNumber="1110D", floorNumber=1)
    allBathrooms.append(sfh1110D)

    sfh1126 = Bathroom(bathroomID="sfh1126", buildingID="sfh", bathroomName="Single Use Restroom/Athletics Treatment", bathroomNumber="1126", floorNumber=1)
    allBathrooms.append(sfh1126)

    sfh1152 = Bathroom(bathroomID="sfh1152", buildingID="sfh", bathroomName="Women's Restroom", bathroomNumber="1152", floorNumber=1)
    allBathrooms.append(sfh1152)

    sfh1154 = Bathroom(bathroomID="sfh1154", buildingID="sfh", bathroomName="Men's Restroom", bathroomNumber="1154", floorNumber=1)
    allBathrooms.append(sfh1154)

    sfh1162 = Bathroom(bathroomID="sfh1162", buildingID="sfh", bathroomName="Men's Restroom", bathroomNumber="1162", floorNumber=1)
    allBathrooms.append(sfh1162)

    sfh224B = Bathroom(bathroomID="sfh224B", buildingID="sfh", bathroomName="Single Use Restroom", bathroomNumber="224B", floorNumber=2)
    allBathrooms.append(sfh224B)

    sfh283 = Bathroom(bathroomID="sfh283", buildingID="sfh", bathroomName="Women's Restroom", bathroomNumber="283", floorNumber=2)
    allBathrooms.append(sfh283)

    sfh284 = Bathroom(bathroomID="sfh284", buildingID="sfh", bathroomName="Men's Restroom", bathroomNumber="284", floorNumber=2)
    allBathrooms.append(sfh284)

    #IPF BUILDING
    ipf106 = Bathroom(bathroomID="ipf106", buildingID="ipf", bathroomName="Women's Restroom", bathroomNumber="106", floorNumber=1)
    allBathrooms.append(ipf106)

    ipf108 = Bathroom(bathroomID="ipf108", buildingID="ipf", bathroomName="Men's Restroom", bathroomNumber="108", floorNumber=1)
    allBathrooms.append(ipf108)

    #CB BUILDING
    cb146 = Bathroom(bathroomID="cb146", buildingID="cb", bathroomName="Men's Restroom", bathroomNumber="146", floorNumber=1)
    allBathrooms.append(cb146)

    cb146A = Bathroom(bathroomID="cb146A", buildingID="cb", bathroomName="Men's Restroom Locker Room", bathroomNumber="146A", floorNumber=1)
    allBathrooms.append(cb146A)

    cb146B = Bathroom(bathroomID="cb146B", buildingID="cb", bathroomName="Men's Restroom Shower Room", bathroomNumber="146B", floorNumber=1)
    allBathrooms.append(cb146B)

    cb201 = Bathroom(bathroomID="cb201", buildingID="cb", bathroomName="Restroom Vestibule", bathroomNumber="201", floorNumber=2)
    allBathrooms.append(cb201)

    cb201A = Bathroom(bathroomID="cb201A", buildingID="cb", bathroomName="Men's Restroom", bathroomNumber="201A", floorNumber=2)
    allBathrooms.append(cb201A)

    cb243 = Bathroom(bathroomID="cb243", buildingID="cb", bathroomName="Restroom Vestibule", bathroomNumber="243", floorNumber=2)
    allBathrooms.append(cb243)

    cb243B = Bathroom(bathroomID="cb243B", buildingID="cb", bathroomName="Women's Restroom", bathroomNumber="243B", floorNumber=2)
    allBathrooms.append(cb243B)

    cb301 = Bathroom(bathroomID="cb301", buildingID="cb", bathroomName="Restroom Vestibule", bathroomNumber="301", floorNumber=3)
    allBathrooms.append(cb301)

    cb301A = Bathroom(bathroomID="cb301A", buildingID="cb", bathroomName="Men's Restroom", bathroomNumber="301A", floorNumber=3)
    allBathrooms.append(cb301A)

    cb365 = Bathroom(bathroomID="cb365", buildingID="cb", bathroomName="Men's Restroom", bathroomNumber="365", floorNumber=3)
    allBathrooms.append(cb365)

    cb367 = Bathroom(bathroomID="cb367", buildingID="cb", bathroomName="Women's Restroom", bathroomNumber="367", floorNumber=3)
    allBathrooms.append(cb367)

    cb367C = Bathroom(bathroomID="cb367C", buildingID="cb", bathroomName="Restroom Vestibule", bathroomNumber="367C", floorNumber=3)
    allBathrooms.append(cb367C)

    cb367E = Bathroom(bathroomID="cb367E", buildingID="cb", bathroomName="Women's Lounge", bathroomNumber="367E", floorNumber=3)
    allBathrooms.append(cb367E)

    cb402 = Bathroom(bathroomID="cb402", buildingID="cb", bathroomName="Restroom Vestibule", bathroomNumber="402", floorNumber=4)
    allBathrooms.append(cb402)

    cb402A = Bathroom(bathroomID="cb402A", buildingID="cb", bathroomName="Men's Restroom", bathroomNumber="402A", floorNumber=4)
    allBathrooms.append(cb402A)

    cb465 = Bathroom(bathroomID="cb465", buildingID="cb", bathroomName="Restroom Vestibule", bathroomNumber="465", floorNumber=4)
    allBathrooms.append(cb465)

    cb465B = Bathroom(bathroomID="cb465B", buildingID="cb", bathroomName="Women's Restroom", bathroomNumber="465B", floorNumber=4)
    allBathrooms.append(cb465B)

    cb465E = Bathroom(bathroomID="cb465E", buildingID="cb", bathroomName="Women's Lounge", bathroomNumber="465E", floorNumber=4)
    allBathrooms.append(cb465E)

    cb540 = Bathroom(bathroomID="cb540", buildingID="cb", bathroomName="Men's Restroom", bathroomNumber="540", floorNumber=5)
    allBathrooms.append(cb540)

    # EB BUILDING
    ebB115 = Bathroom(bathroomID="ebB115", buildingID="eb", bathroomName="Women's Restroom", bathroomNumber="B115", floorNumber=0)
    allBathrooms.append(ebB115)

    ebB123 = Bathroom(bathroomID="ebB123", buildingID="eb", bathroomName="Men's Restroom", bathroomNumber="B123", floorNumber=0)
    allBathrooms.append(ebB123)

    eb109 = Bathroom(bathroomID="eb109", buildingID="eb", bathroomName="Men's Restroom", bathroomNumber="109", floorNumber=1)
    allBathrooms.append(eb109)

    eb111 = Bathroom(bathroomID="eb111", buildingID="eb", bathroomName="Women's Restroom", bathroomNumber="111", floorNumber=1)
    allBathrooms.append(eb111)

    eb212 = Bathroom(bathroomID="eb212", buildingID="eb", bathroomName="Single Use Restroom", bathroomNumber="212", floorNumber=2)
    allBathrooms.append(eb212)

    eb215 = Bathroom(bathroomID="eb215", buildingID="eb", bathroomName="Men's Restroom", bathroomNumber="215", floorNumber=2)
    allBathrooms.append(eb215)

    eb217 = Bathroom(bathroomID="eb217", buildingID="eb", bathroomName="Women's Restroom", bathroomNumber="217", floorNumber=2)
    allBathrooms.append(eb217)

    eb311 = Bathroom(bathroomID="eb311", buildingID="eb", bathroomName="Men's Restroom", bathroomNumber="311", floorNumber=3)
    allBathrooms.append(eb311)

    eb313 = Bathroom(bathroomID="eb313", buildingID="eb", bathroomName="Women's Restroom", bathroomNumber="313", floorNumber=3)
    allBathrooms.append(eb313)

    eb347 = Bathroom(bathroomID="eb347", buildingID="eb", bathroomName="Single Use Restroom", bathroomNumber="347", floorNumber=3)
    allBathrooms.append(eb347)

    eb415 = Bathroom(bathroomID="eb415", buildingID="eb", bathroomName="Men's Restroom", bathroomNumber="415", floorNumber=4)
    allBathrooms.append(eb415)

    eb417 = Bathroom(bathroomID="eb417", buildingID="eb", bathroomName="Women's Restroom", bathroomNumber="417", floorNumber=4)
    allBathrooms.append(eb417)

    #CTB BUILDING
    ctb62 = Bathroom(bathroomID="ctb62", buildingID="ctb", bathroomName="Single Use Restroom", bathroomNumber="62", floorNumber=0)
    allBathrooms.append(ctb62)

    ctb64 = Bathroom(bathroomID="ctb64", buildingID="ctb", bathroomName="Single Use Restroom", bathroomNumber="64", floorNumber=0)
    allBathrooms.append(ctb64)

    ctb122 = Bathroom(bathroomID="ctb122", buildingID="ctb", bathroomName="Women's Restroom", bathroomNumber="122", floorNumber=1)
    allBathrooms.append(ctb122)

    ctb124 = Bathroom(bathroomID="ctb124", buildingID="ctb", bathroomName="Men's Restroom", bathroomNumber="124", floorNumber=1)
    allBathrooms.append(ctb124)

    ctb222 = Bathroom(bathroomID="ctb222", buildingID="ctb", bathroomName="Women's Restroom", bathroomNumber="222", floorNumber=2)
    allBathrooms.append(ctb222)

    ctb224 = Bathroom(bathroomID="ctb224", buildingID="ctb", bathroomName="Men's Restroom", bathroomNumber="224", floorNumber=2)
    allBathrooms.append(ctb224)

    ctb322 = Bathroom(bathroomID="ctb322", buildingID="ctb", bathroomName="Women's Restroom", bathroomNumber="322", floorNumber=3)
    allBathrooms.append(ctb322)

    ctb324 = Bathroom(bathroomID="ctb324", buildingID="ctb", bathroomName="Men's Restroom", bathroomNumber="324", floorNumber=3)
    allBathrooms.append(ctb324)

    ctb422 = Bathroom(bathroomID="ctb422", buildingID="ctb", bathroomName="Women's Restroom", bathroomNumber="422", floorNumber=4)
    allBathrooms.append(ctb422)

    ctb424 = Bathroom(bathroomID="ctb424", buildingID="ctb", bathroomName="Men's Restroom", bathroomNumber="424", floorNumber=4)
    allBathrooms.append(ctb424)

    #PPCH BUILDING
    ppch106 = Bathroom(bathroomID="ppch106", buildingID="ppch", bathroomName="Restroom", bathroomNumber="106", floorNumber=1)
    allBathrooms.append(ppch106)

    ppch182 = Bathroom(bathroomID="ppch182", buildingID="ppch", bathroomName="General Restroom", bathroomNumber="182", floorNumber=1)
    allBathrooms.append(ppch182)

    ppch232 = Bathroom(bathroomID="ppch232", buildingID="ppch", bathroomName="Restroom", bathroomNumber="232", floorNumber=2)
    allBathrooms.append(ppch232)

    #ROTC BUILDING
    rotc271 = Bathroom(bathroomID="rotc271", buildingID="rotc", bathroomName="Men's Restroom", bathroomNumber="271", floorNumber=2)
    allBathrooms.append(rotc271)

    rotc322 = Bathroom(bathroomID="rotc322", buildingID="rotc", bathroomName="Men's Restroom", bathroomNumber="322", floorNumber=3)
    allBathrooms.append(rotc322)

    rotc370 = Bathroom(bathroomID="rotc370", buildingID="rotc", bathroomName="Women's Restroom", bathroomNumber="370", floorNumber=3)
    allBathrooms.append(rotc370)

    #CMB BUILDING
    cmb110 = Bathroom(bathroomID="cmb110", buildingID="cmb", bathroomName="Single Use Restroom/Employee", bathroomNumber="110", floorNumber=1)
    allBathrooms.append(cmb110)

    cmb174 = Bathroom(bathroomID="cmb174", buildingID="cmb", bathroomName="Single Use Restroom/Shower/Employee", bathroomNumber="174", floorNumber=1)
    allBathrooms.append(cmb174)

    #SNLB BUILDING
    snlb160 = Bathroom(bathroomID="snlb160", buildingID="snlb", bathroomName="Single Use Restroom", bathroomNumber="160", floorNumber=1)
    allBathrooms.append(snlb160)

    snlb260 = Bathroom(bathroomID="snlb260", buildingID="snlb", bathroomName="Women's Restroom", bathroomNumber="260", floorNumber=2)
    allBathrooms.append(snlb260)

    snlb280 = Bathroom(bathroomID="snlb280", buildingID="snlb", bathroomName="Men's Restroom", bathroomNumber="280", floorNumber=2)
    allBathrooms.append(snlb280)

    #B66 BUILDING
    b66202 = Bathroom(bathroomID="b66202", buildingID="b66", bathroomName="Men's Restroom", bathroomNumber="202", floorNumber=2)
    allBathrooms.append(b66202)

    b66205 = Bathroom(bathroomID="b66205", buildingID="b66", bathroomName="Women's Restroom", bathroomNumber="205", floorNumber=2)
    allBathrooms.append(b66205)

    #BRWB BUILDING
    brwb105 = Bathroom(bathroomID="brwb105", buildingID="brwb", bathroomName="Men's Restroom", bathroomNumber="105", floorNumber=1)
    allBathrooms.append(brwb105)

    brwb109 = Bathroom(bathroomID="brwb109", buildingID="brwb", bathroomName="Women's Restroom", bathroomNumber="109", floorNumber=1)
    allBathrooms.append(brwb109)

    brwb171 = Bathroom(bathroomID="brwb171", buildingID="brwb", bathroomName="Single Use Restroom/Employee", bathroomNumber="171", floorNumber=1)
    allBathrooms.append(brwb171)

    brwb199 = Bathroom(bathroomID="brwb199", buildingID="brwb", bathroomName="Men's Restroom/Locker Room/Shower", bathroomNumber="199", floorNumber=1)
    allBathrooms.append(brwb199)

    brwb212 = Bathroom(bathroomID="brwb212", buildingID="brwb", bathroomName="Men's Restroom", bathroomNumber="212", floorNumber=2)
    allBathrooms.append(brwb212)

    brwb216 = Bathroom(bathroomID="brwb216", buildingID="brwb", bathroomName="Women's Restroom", bathroomNumber="216", floorNumber=2)
    allBathrooms.append(brwb216)

    brwb272 = Bathroom(bathroomID="brwb272", buildingID="brwb", bathroomName="Men's Restroom/Locker Room/Shower/Employee", bathroomNumber="272", floorNumber=2)
    allBathrooms.append(brwb272)

    # HRCB BUILDING
    hrcb103 = Bathroom(bathroomID="hrcb103", buildingID="hrcb", bathroomName="Men's Restroom", bathroomNumber="103", floorNumber=1)
    allBathrooms.append(hrcb103)

    hrcb106 = Bathroom(bathroomID="hrcb106", buildingID="hrcb", bathroomName="Women's Restroom", bathroomNumber="106", floorNumber=1)
    allBathrooms.append(hrcb106)

    hrcb136 = Bathroom(bathroomID="hrcb136", buildingID="hrcb", bathroomName="Women's Restroom", bathroomNumber="136", floorNumber=1)
    allBathrooms.append(hrcb136)

    hrcb138 = Bathroom(bathroomID="hrcb138", buildingID="hrcb", bathroomName="Men's Restroom", bathroomNumber="138", floorNumber=1)
    allBathrooms.append(hrcb138)

    hrcb256 = Bathroom(bathroomID="hrcb256", buildingID="hrcb", bathroomName="Men's Restroom", bathroomNumber="256", floorNumber=2)
    allBathrooms.append(hrcb256)

    hrcb264 = Bathroom(bathroomID="hrcb264", buildingID="hrcb", bathroomName="Women's Restroom", bathroomNumber="264", floorNumber=2)
    allBathrooms.append(hrcb264)

    # MARB BUILDING
    marbB103 = Bathroom(bathroomID="marbB103", buildingID="marb", bathroomName="Women's Restroom", bathroomNumber="B103", floorNumber=0)
    allBathrooms.append(marbB103)

    marbB104 = Bathroom(bathroomID="marbB104", buildingID="marb", bathroomName="Men's Restroom", bathroomNumber="B104", floorNumber=0)
    allBathrooms.append(marbB104)

    marb106 = Bathroom(bathroomID="marb106", buildingID="marb", bathroomName="Men's Restroom", bathroomNumber="106", floorNumber=1)
    allBathrooms.append(marb106)

    marb107 = Bathroom(bathroomID="marb107", buildingID="marb", bathroomName="Women's Restroom", bathroomNumber="107", floorNumber=1)
    allBathrooms.append(marb107)

    marb204 = Bathroom(bathroomID="marb204", buildingID="marb", bathroomName="Men's Restroom", bathroomNumber="204", floorNumber=2)
    allBathrooms.append(marb204)

    marb205 = Bathroom(bathroomID="marb205", buildingID="marb", bathroomName="Women's Restroom", bathroomNumber="205", floorNumber=2)
    allBathrooms.append(marb205)

    #LSB BUILDING
    lsb1008 = Bathroom(bathroomID="lsb1008", buildingID="lsb", bathroomName="Men's Restroom/Shower", bathroomNumber="1008", floorNumber=1)
    allBathrooms.append(lsb1008)

    lsb1010 = Bathroom(bathroomID="lsb1010", buildingID="lsb", bathroomName="Women's Restroom/Shower", bathroomNumber="1010", floorNumber=1)
    allBathrooms.append(lsb1010)

    lsb2053A = Bathroom(bathroomID="lsb2053A", buildingID="lsb", bathroomName="Women's Restroom", bathroomNumber="2053A", floorNumber=2)
    allBathrooms.append(lsb2053A)

    lsb2053C = Bathroom(bathroomID="lsb2053C", buildingID="lsb", bathroomName="Men's Restroom", bathroomNumber="2053C", floorNumber=2)
    allBathrooms.append(lsb2053C)

    lsb2103A = Bathroom(bathroomID="lsb2103A", buildingID="lsb", bathroomName="Women's Restroom", bathroomNumber="2103A", floorNumber=2)
    allBathrooms.append(lsb2103A)

    lsb2103C = Bathroom(bathroomID="lsb2103C", buildingID="lsb", bathroomName="Men's Restroom", bathroomNumber="2103C", floorNumber=2)
    allBathrooms.append(lsb2103C)

    lsb3102A = Bathroom(bathroomID="lsb3102A", buildingID="lsb", bathroomName="Women's Restroom", bathroomNumber="3102A", floorNumber=3)
    allBathrooms.append(lsb3102A)

    lsb3102C = Bathroom(bathroomID="lsb3102C", buildingID="lsb", bathroomName="Men's Restroom", bathroomNumber="3102C", floorNumber=3)
    allBathrooms.append(lsb3102C)

    lsb4115A = Bathroom(bathroomID="lsb4115A", buildingID="lsb", bathroomName="Women's Restroom", bathroomNumber="4115A", floorNumber=4)
    allBathrooms.append(lsb4115A)

    lsb4115C = Bathroom(bathroomID="lsb4115C", buildingID="lsb", bathroomName="Men's Restroom", bathroomNumber="4115C", floorNumber=4)
    allBathrooms.append(lsb4115C)

    lsb5118A = Bathroom(bathroomID="lsb5118A", buildingID="lsb", bathroomName="Women's Restroom", bathroomNumber="5118A", floorNumber=5)
    allBathrooms.append(lsb5118A)

    lsb5118C = Bathroom(bathroomID="lsb5118C", buildingID="lsb", bathroomName="Men's Restroom", bathroomNumber="5118C", floorNumber=5)
    allBathrooms.append(lsb5118C)

    #ESC BUILDING
    escN183 = Bathroom(bathroomID="escN183", buildingID="esc", bathroomName="Women's Restroom", bathroomNumber="N183", floorNumber=1)
    allBathrooms.append(escN183)

    escS111 = Bathroom(bathroomID="escS111", buildingID="esc", bathroomName="Men's Restroom", bathroomNumber="S111", floorNumber=1)
    allBathrooms.append(escS111)

    escU131 = Bathroom(bathroomID="escU131", buildingID="esc", bathroomName="Men's Restroom", bathroomNumber="U131", floorNumber=1)
    allBathrooms.append(escU131)

    escU133 = Bathroom(bathroomID="escU133", buildingID="esc", bathroomName="Women's Restroom", bathroomNumber="U133", floorNumber=1)
    allBathrooms.append(escU133)

    escN287 = Bathroom(bathroomID="escN287", buildingID="esc", bathroomName="Men's Restroom", bathroomNumber="N287", floorNumber=2)
    allBathrooms.append(escN287)

    escS203 = Bathroom(bathroomID="escS203", buildingID="esc", bathroomName="Women's Restroom", bathroomNumber="S203", floorNumber=2)
    allBathrooms.append(escS203)

    escC329 = Bathroom(bathroomID="escC329", buildingID="esc", bathroomName="Women's Restroom", bathroomNumber="C329", floorNumber=3)
    allBathrooms.append(escC329)

    escC385 = Bathroom(bathroomID="escC385", buildingID="esc", bathroomName="Men's Restroom", bathroomNumber="C385", floorNumber=3)
    allBathrooms.append(escC385)

    escC402A = Bathroom(bathroomID="escC402A", buildingID="esc", bathroomName="Women's Restroom", bathroomNumber="C402A", floorNumber=4)
    allBathrooms.append(escC402A)

    escC453A = Bathroom(bathroomID="escC453A", buildingID="esc", bathroomName="Men's Restroom", bathroomNumber="C453A", floorNumber=4)
    allBathrooms.append(escC453A)

    # KMBL BUILDING
    kmbl139 = Bathroom(bathroomID="kmbl139", buildingID="kmbl", bathroomName="Restroom Vestibule", bathroomNumber="139", floorNumber=1)
    allBathrooms.append(kmbl139)

    kmbl139A = Bathroom(bathroomID="kmbl139A", buildingID="kmbl", bathroomName="Single Use Restroom/Nursing Lab", bathroomNumber="139A", floorNumber=1)
    allBathrooms.append(kmbl139A)

    kmbl139B = Bathroom(bathroomID="kmbl139B", buildingID="kmbl", bathroomName="Single Use Restroom/Nursing Lab", bathroomNumber="139B", floorNumber=1)
    allBathrooms.append(kmbl139B)

    kmbl176 = Bathroom(bathroomID="kmbl176", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="176", floorNumber=1)
    allBathrooms.append(kmbl176)

    kmbl177 = Bathroom(bathroomID="kmbl177", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="177", floorNumber=1)
    allBathrooms.append(kmbl177)

    kmbl1031A = Bathroom(bathroomID="kmbl1031A", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="1031A", floorNumber=1)
    allBathrooms.append(kmbl1031A)

    kmbl1131A = Bathroom(bathroomID="kmbl1131A", buildingID="kmbl", bathroomName="Single Use Restroom", bathroomNumber="1131A", floorNumber=1)
    allBathrooms.append(kmbl1131A)

    kmbl220 = Bathroom(bathroomID="kmbl220", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="220", floorNumber=2)
    allBathrooms.append(kmbl220)

    kmbl222 = Bathroom(bathroomID="kmbl222", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="222", floorNumber=2)
    allBathrooms.append(kmbl222)

    kmbl224 = Bathroom(bathroomID="kmbl224", buildingID="kmbl", bathroomName="Single Use Restroom", bathroomNumber="224", floorNumber=2)
    allBathrooms.append(kmbl224)

    kmbl308 = Bathroom(bathroomID="kmbl308", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="308", floorNumber=3)
    allBathrooms.append(kmbl308)

    kmbl329 = Bathroom(bathroomID="kmbl329", buildingID="kmbl", bathroomName="Restroom Vestibule", bathroomNumber="329", floorNumber=3)
    allBathrooms.append(kmbl329)

    kmbl329A = Bathroom(bathroomID="kmbl329A", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="329A", floorNumber=3)
    allBathrooms.append(kmbl329A)

    kmbl407 = Bathroom(bathroomID="kmbl407", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="407", floorNumber=4)
    allBathrooms.append(kmbl407)

    kmbl408 = Bathroom(bathroomID="kmbl408", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="408", floorNumber=4)
    allBathrooms.append(kmbl408)

    kmbl508 = Bathroom(bathroomID="kmbl508", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="508", floorNumber=5)
    allBathrooms.append(kmbl508)

    kmbl531 = Bathroom(bathroomID="kmbl531", buildingID="kmbl", bathroomName="Restroom Vestibule", bathroomNumber="531", floorNumber=5)
    allBathrooms.append(kmbl531)

    kmbl531A = Bathroom(bathroomID="kmbl531A", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="531A", floorNumber=5)
    allBathrooms.append(kmbl531A)

    kmbl608 = Bathroom(bathroomID="kmbl608", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="608", floorNumber=6)
    allBathrooms.append(kmbl608)

    kmbl631 = Bathroom(bathroomID="kmbl631", buildingID="kmbl", bathroomName="Restroom Vestibule", bathroomNumber="631", floorNumber=6)
    allBathrooms.append(kmbl631)

    kmbl631A = Bathroom(bathroomID="kmbl631A", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="631A", floorNumber=6)
    allBathrooms.append(kmbl631A)

    kmbl708 = Bathroom(bathroomID="kmbl708", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="708", floorNumber=7)
    allBathrooms.append(kmbl708)

    kmbl731 = Bathroom(bathroomID="kmbl731", buildingID="kmbl", bathroomName="Restroom Vestibule", bathroomNumber="731", floorNumber=7)
    allBathrooms.append(kmbl731)

    kmbl731A = Bathroom(bathroomID="kmbl731A", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="731A", floorNumber=7)
    allBathrooms.append(kmbl731A)

    kmbl808 = Bathroom(bathroomID="kmbl808", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="808", floorNumber=8)
    allBathrooms.append(kmbl808)

    kmbl831 = Bathroom(bathroomID="kmbl831", buildingID="kmbl", bathroomName="Restroom Vestibule", bathroomNumber="831", floorNumber=8)
    allBathrooms.append(kmbl831)

    kmbl831A = Bathroom(bathroomID="kmbl831A", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="831A", floorNumber=8)
    allBathrooms.append(kmbl831A)

    kmbl908 = Bathroom(bathroomID="kmbl908", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="908", floorNumber=9)
    allBathrooms.append(kmbl908)

    kmbl935 = Bathroom(bathroomID="kmbl935", buildingID="kmbl", bathroomName="Restroom Vestibule", bathroomNumber="935", floorNumber=9)
    allBathrooms.append(kmbl935)

    kmbl935A = Bathroom(bathroomID="kmbl935A", buildingID="kmbl", bathroomName="Men's Restroom", bathroomNumber="935A", floorNumber=9)
    allBathrooms.append(kmbl935A)

    kmbl1008 = Bathroom(bathroomID="kmbl1008", buildingID="kmbl", bathroomName="Women's Restroom", bathroomNumber="1008", floorNumber=10)
    allBathrooms.append(kmbl1008)

    kmbl1031 = Bathroom(bathroomID="kmbl1031", buildingID="kmbl", bathroomName="Restroom Vestibule", bathroomNumber="1031", floorNumber=10)
    allBathrooms.append(kmbl1031)

    kmbl1121 = Bathroom(bathroomID="kmbl1121", buildingID="kmbl", bathroomName="Single Use Restroom", bathroomNumber="1121", floorNumber=11)
    allBathrooms.append(kmbl1121)

    kmbl1131 = Bathroom(bathroomID="kmbl1131", buildingID="kmbl", bathroomName="Restroom Vestibule", bathroomNumber="1131", floorNumber=11)
    allBathrooms.append(kmbl1131)

    kmbl1208 = Bathroom(bathroomID="kmbl1208", buildingID="kmbl", bathroomName="Single Use Restroom/Research", bathroomNumber="1208", floorNumber=12)
    allBathrooms.append(kmbl1208)

    # MSRB BUILDING
    msrb107 = Bathroom(bathroomID="msrb107", buildingID="msrb", bathroomName="Women’s Restroom", bathroomNumber="107", floorNumber=1)
    allBathrooms.append(msrb107)

    msrb147 = Bathroom(bathroomID="msrb147", buildingID="msrb", bathroomName="Men’s Restroom", bathroomNumber="147", floorNumber=1)
    allBathrooms.append(msrb147)

    msrb311 = Bathroom(bathroomID="msrb311", buildingID="msrb", bathroomName="Women’s Restroom", bathroomNumber="311", floorNumber=3)
    allBathrooms.append(msrb311)

    msrb341 = Bathroom(bathroomID="msrb341", buildingID="msrb", bathroomName="Men’s Restroom", bathroomNumber="341", floorNumber=3)
    allBathrooms.append(msrb341)

    # HGB BUILDING
    hgb164 = Bathroom(bathroomID="hgb164", buildingID="hgb", bathroomName="Restroom Vestibule", bathroomNumber="164", floorNumber=1)
    allBathrooms.append(hgb164)

    hgb164A = Bathroom(bathroomID="hgb164A", buildingID="hgb", bathroomName="Women’s Restroom", bathroomNumber="164A", floorNumber=1)
    allBathrooms.append(hgb164A)

    hgb168 = Bathroom(bathroomID="hgb168", buildingID="hgb", bathroomName="Restroom Vestibule", bathroomNumber="168", floorNumber=1)
    allBathrooms.append(hgb168)

    hgb168A = Bathroom(bathroomID="hgb168A", buildingID="hgb", bathroomName="Men’s Vestibule", bathroomNumber="168A", floorNumber=1)
    allBathrooms.append(hgb168A)

    hgb250 = Bathroom(bathroomID="hgb250", buildingID="hgb", bathroomName="Women’s Vestibule", bathroomNumber="250", floorNumber=2)
    allBathrooms.append(hgb250)

    hgb256 = Bathroom(bathroomID="hgb256", buildingID="hgb", bathroomName="Men’s Vestibule", bathroomNumber="256", floorNumber=2)
    allBathrooms.append(hgb256)

    # JSB BUILDING
    jsb105 = Bathroom(bathroomID="jsb105", buildingID="jsb", bathroomName="Men’s Restroom", bathroomNumber="105", floorNumber=1)
    allBathrooms.append(jsb105)

    jsb155 = Bathroom(bathroomID="jsb155", buildingID="jsb", bathroomName="Women’s Restroom", bathroomNumber="155", floorNumber=1)
    allBathrooms.append(jsb155)

    jsb247C = Bathroom(bathroomID="jsb247C", buildingID="jsb", bathroomName="Restroom Vestibule", bathroomNumber="247C", floorNumber=2)
    allBathrooms.append(jsb247C)

    jsb247D = Bathroom(bathroomID="jsb247D", buildingID="jsb", bathroomName="Women’s Restroom", bathroomNumber="247D", floorNumber=2)
    allBathrooms.append(jsb247D)

    jsb347D = Bathroom(bathroomID="jsb347D", buildingID="jsb", bathroomName="Restroom Vestibule", bathroomNumber="347D", floorNumber=3)
    allBathrooms.append(jsb347D)

    jsb347E = Bathroom(bathroomID="jsb347EC", buildingID="jsb", bathroomName="Men’s Restroom", bathroomNumber="347E", floorNumber=3)
    allBathrooms.append(jsb347E)

    jsb350 = Bathroom(bathroomID="jsb350", buildingID="jsb", bathroomName="Women’s Restroom", bathroomNumber="350", floorNumber=3)
    allBathrooms.append(jsb350)

    #BNSN BUILDING
    bnsnC012 = Bathroom(bathroomID="bnsnC012", buildingID="bnsn", bathroomName="Single Use Restroom", bathroomNumber="C012", floorNumber=0)
    allBathrooms.append(bnsnC012)

    bnsnC014 = Bathroom(bathroomID="bnsnC014", buildingID="bnsn", bathroomName="Single Use Restroom", bathroomNumber="C014", floorNumber=0)
    allBathrooms.append(bnsnC014)

    bnsnW013 = Bathroom(bathroomID="bnsnW013", buildingID="bnsn", bathroomName="Men’s Restroom", bathroomNumber="W013", floorNumber=0)
    allBathrooms.append(bnsnW013)

    bnsnW014 = Bathroom(bathroomID="bnsnW014", buildingID="bnsn", bathroomName="Women’s Restroom", bathroomNumber="W014", floorNumber=0)
    allBathrooms.append(bnsnW014)

    bnsnC119 = Bathroom(bathroomID="bnsnC119", buildingID="bnsn", bathroomName="Men’s Restroom", bathroomNumber="C119", floorNumber=1)
    allBathrooms.append(bnsnC119)

    bnsnC123 = Bathroom(bathroomID="bnsnC123", buildingID="bnsn", bathroomName="Women’s Restroom", bathroomNumber="C123", floorNumber=1)
    allBathrooms.append(bnsnC123)

    bnsnC125 = Bathroom(bathroomID="bnsnC125", buildingID="bnsn", bathroomName="Single Use Restroom", bathroomNumber="C125", floorNumber=1)
    allBathrooms.append(bnsnC125)

    bnsnW132 = Bathroom(bathroomID="bnsnW132", buildingID="bnsn", bathroomName="Women’s Restroom", bathroomNumber="W132", floorNumber=1)
    allBathrooms.append(bnsnW132)

    bnsnW139 = Bathroom(bathroomID="bnsnW139", buildingID="bnsn", bathroomName="Men Restroom", bathroomNumber="W139", floorNumber=1)
    allBathrooms.append(bnsnW139)

    bnsnC219 = Bathroom(bathroomID="bnsnC219", buildingID="bnsn", bathroomName="Women’s Restroom", bathroomNumber="C219", floorNumber=2)
    allBathrooms.append(bnsnC219)

    bnsnC225 = Bathroom(bathroomID="bnsnC225", buildingID="bnsn", bathroomName="Men’s Restroom", bathroomNumber="C225", floorNumber=2)
    allBathrooms.append(bnsnC225)

    bnsnC319 = Bathroom(bathroomID="bnsnC319", buildingID="bnsn", bathroomName="Men’s Restroom", bathroomNumber="C319", floorNumber=3)
    allBathrooms.append(bnsnC319)

    bnsnC325 = Bathroom(bathroomID="bnsnC325", buildingID="bnsn", bathroomName="Women’s Restroom", bathroomNumber="C325", floorNumber=3)
    allBathrooms.append(bnsnC325)

    bnsnC419 = Bathroom(bathroomID="bnsnC419", buildingID="bnsn", bathroomName="Women’s Restroom", bathroomNumber="C419", floorNumber=4)
    allBathrooms.append(bnsnC419)

    bnsnC425 = Bathroom(bathroomID="bnsnC425", buildingID="bnsn", bathroomName="Men’s Restroom", bathroomNumber="C425", floorNumber=4)
    allBathrooms.append(bnsnC425)



    # NICB BUILDING
    nicb101 = Bathroom(bathroomID="nicb101", buildingID="nicb", bathroomName="Mothers Room", bathroomNumber="101", floorNumber=1)
    allBathrooms.append(nicb101)

    nicb102 = Bathroom(bathroomID="nicb102", buildingID="nicb", bathroomName="Single Use  Restroom", bathroomNumber="102", floorNumber=1)
    allBathrooms.append(nicb102)

    nicb103 = Bathroom(bathroomID="nicb103", buildingID="nicb", bathroomName="Mens’Single Use Restroom", bathroomNumber="106", floorNumber=1)
    allBathrooms.append(nicb103)

    nicb241 = Bathroom(bathroomID="nicb241", buildingID="nicb", bathroomName="Single Use Restroom/Employee", bathroomNumber="241", floorNumber=2)
    allBathrooms.append(nicb241)

    # BRMB BUILDING
    brmb105 = Bathroom(bathroomID="brmb105", buildingID="brmb", bathroomName="Men’s Restroom", bathroomNumber="105", floorNumber=1)
    allBathrooms.append(brmb105)

    brmb155 = Bathroom(bathroomID="brmb155", buildingID="brmb", bathroomName="Women’s Restroom", bathroomNumber="155", floorNumber=1)
    allBathrooms.append(brmb155)

    brmb247C = Bathroom(bathroomID="brmb247C", buildingID="brmb", bathroomName="Restroom Vestibule", bathroomNumber="247C", floorNumber=2)
    allBathrooms.append(brmb247C)

    brmb247D = Bathroom(bathroomID="brmb247D", buildingID="brmb", bathroomName="Women’s Restroom", bathroomNumber="247D", floorNumber=2)
    allBathrooms.append(brmb247D)

    brmb347D = Bathroom(bathroomID="brmb347D", buildingID="brmb", bathroomName="Restroom Vestibule", bathroomNumber="347D", floorNumber=3)
    allBathrooms.append(brmb347D)

    brmb347E = Bathroom(bathroomID="brmb347E", buildingID="brmb", bathroomName="Men’s Restroom", bathroomNumber="347E", floorNumber=3)
    allBathrooms.append(brmb347E)

    brmb350 = Bathroom(bathroomID="brmb350", buildingID="brmb", bathroomName="Women’s Restroom", bathroomNumber="350", floorNumber=3)
    allBathrooms.append(brmb350)

    # FPH BUILDING
    fph110 = Bathroom(bathroomID="fph110", buildingID="fph", bathroomName="Single Use Restroom", bathroomNumber="110", floorNumber=1)
    allBathrooms.append(fph110)

    fph210 = Bathroom(bathroomID="fph210", buildingID="fph", bathroomName="Single Use Restroom", bathroomNumber="210", floorNumber=2)
    allBathrooms.append(fph210)

    #MCKB BUILDING
    mckb117 = Bathroom(bathroomID="mckb117", buildingID="mckb", bathroomName="Men’s Restroom", bathroomNumber="117", floorNumber=1)
    allBathrooms.append(mckb117)

    mckb163 = Bathroom(bathroomID="mckb163", buildingID="mckb", bathroomName="Restroom Vestibule", bathroomNumber="163", floorNumber=1)
    allBathrooms.append(mckb163)

    mckb163A = Bathroom(bathroomID="mckb163A", buildingID="mckb", bathroomName="Women’s Restroom", bathroomNumber="163A", floorNumber=1)
    allBathrooms.append(mckb163A)

    mckb213 = Bathroom(bathroomID="mckb213", buildingID="mckb", bathroomName="Restroom Vestibule" , bathroomNumber="213", floorNumber=2)
    allBathrooms.append(mckb213)

    mckb213A = Bathroom(bathroomID="mckb213A", buildingID="mckb", bathroomName="Restroom Vestibule", bathroomNumber="213A", floorNumber=2)
    allBathrooms.append(mckb213A)

    mckb229 = Bathroom(bathroomID="mckb229", buildingID="mckb", bathroomName="Women’s Restroom", bathroomNumber="229", floorNumber=2)
    allBathrooms.append(mckb229)

    mckb229A = Bathroom(bathroomID="mckb229A", buildingID="mckb", bathroomName="Women’s Restroom", bathroomNumber="229A", floorNumber=2)
    allBathrooms.append(mckb229A)

    mckb315 = Bathroom(bathroomID="mckb315", buildingID="mckb", bathroomName="Restroom Vestibule" , bathroomNumber="315", floorNumber=3)
    allBathrooms.append(mckb315)

    mckb315A = Bathroom(bathroomID="mckb315A", buildingID="mckb", bathroomName="Restroom Vestibule", bathroomNumber="315A", floorNumber=3)
    allBathrooms.append(mckb315A)

    mckb335 = Bathroom(bathroomID="mckb335", buildingID="mckb", bathroomName="Women’s Restroom", bathroomNumber="335", floorNumber=3)
    allBathrooms.append(mckb335)

    mckb335A = Bathroom(bathroomID="mckb335A", buildingID="mckb", bathroomName="Women’s Restroom", bathroomNumber="335A", floorNumber=3)
    allBathrooms.append(mckb335A)

    return allBathrooms

def insertBuildings():
    allBuildings = populateAllBuildings()

    import sqlite3
    for building in allBuildings:
        data_tuple = (building.buildingID, building.fullBuildingName, building.buildingLocationLat, building.buildingLocationLong)
        print('Attempting to insert', building.buildingID, building.buildingLocationLat, 'into db')

        try:
            conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
            cursor = conn.cursor()
            print("\tConnected to db")

            insert = """INSERT INTO Building 
            (buildingID, fullBuildingName, buildingLocationLat, buildingLocationLong) 
            VALUES (?,?,?,?);"""

            
            cursor.execute(insert, data_tuple)

            conn.commit()
            cursor.close()
            print('\tSuccessfully added account info to db')
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table:", error)
        finally:
            if (conn):
                conn.close()
def insertBathrooms():
    allBathrooms = populateBathrooms()

    import sqlite3
    for bathroom in allBathrooms:
        data_tuple = (bathroom.bathroomID, bathroom.buildingID.upper(), bathroom.bathroomName, bathroom.bathroomNumber, bathroom.floorNumber)
        print('Attempting to insert', bathroom.bathroomID, 'into db')

        try:
            conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
            cursor = conn.cursor()
            print("\tConnected to db")

            insert = """INSERT INTO Bathroom 
            (bathroomID, buildingID, bathroomName, bathroomNumber, floorNumber) 
            VALUES (?,?,?,?,?);"""

            
            cursor.execute(insert, data_tuple)

            conn.commit()
            cursor.close()
            print('\tSuccessfully added account info to db')
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
            print(data_tuple)
        finally:
            if (conn):
                conn.close()

def insertFakeUsers(numUsers):
    import sqlite3
    users = []

    for i in range (numUsers):
        person = Person()
        user = (person.username, person.password, person.username + '@gmail.com')
        users.append(user)

    for user in users:
        print('Attempting to insert', user[0], 'into db')

        try:
            conn = sqlite3.connect('DoesItStinkBYUDataBase.db')
            cursor = conn.cursor()
            print("\tConnected to db")

            insert = """INSERT INTO User 
            (login, password, email) 
            VALUES (?,?,?);"""

            cursor.execute(insert, user)

            conn.commit()
            cursor.close()
            print('\tSuccessfully added account info to db')
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table:", error)
        finally:
            if (conn):
                conn.close()

def insertFakeRatings(numRatingsPerUser):
    import random
    users = selectAllUsers()
    bathrooms = selectAllBathrooms()
    
    for user in users: # For each user
        for i in range(numRatingsPerUser): # insert 100 ratings
            insertRating(random.choice(bathrooms).bathroomID, user.userID, random.randint(1,5))

def insertFakeReviews(numReviewsPerUser):
    import random
    users = selectAllUsers()
    bathrooms = selectAllBathrooms()
    titles = ['Wow', 'Oh my goodness', 'Nice bathroom!', 'Look at this!!!', 'OMG']
    comments = ['I would never poop here ugg', 'So clean, I can eat off the toilets', 'poop everywhere', 'mira un poco', '69 lol']
    
    for user in users: # For each user
        for i in range(numReviewsPerUser): # insert 50 reviews
            insertReview(random.choice(bathrooms).bathroomID, user.userID, random.randint(1,5), random.choice(titles), random.choice(comments))

def insertFakeLikes(numLikesPerUser):
    import random
    users = selectAllUsers()
    reviews = selectAllReviews()
    
    for user in users: # For each user
        for i in range(numLikesPerUser): # insert 1000 likes
            insertLike(random.choice(reviews).ratingID, user.userID)

def insertFakeDislikes(numDislikesPerUser):
    import random
    users = selectAllUsers()
    reviews = selectAllReviews()
    
    for user in users: # For each user
        for i in range(numDislikesPerUser): # insert 50 dislikes
            insertDislike(random.choice(reviews).ratingID, user.userID)


if __name__ == "__main__":
    deleteAllData()
    insertBuildings()
    insertBathrooms()
    insertFakeUsers(50)
    insertFakeRatings(200)
    insertFakeReviews(50)
    insertFakeLikes(300)
    insertFakeDislikes(300)
