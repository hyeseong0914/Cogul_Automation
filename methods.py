import os


def determineSeconds(path):
    seconds = 0
    fileSize = os.path.getsize(path)
    fileSize = (fileSize / (1024.0 * 1024.0))
    if fileSize < 1:
        seconds = 10
    elif fileSize < 5:
        seconds = 20
    elif fileSize < 10:
        seconds = 30
    elif fileSize < 15:
        seconds = 35
    elif fileSize < 20:
        seconds = 50
    elif fileSize < 25:
        seconds = 60
    else:
        seconds = 70
    return seconds

#언어추가
def chooseLanguage(countryName):
    languages_dict = {}
    languages_dict["Arabic"] = "_cd0"
    languages_dict["Bulgarian"] = "_cd1"
    languages_dict["Croatian"] = "_cd2"
    languages_dict["Czech"] = "_cd3"
    languages_dict["Danish"] = "_cd4"
    languages_dict["Dutch"] = "_cd5"
    languages_dict["English"] = "_cd6"
    languages_dict["Estonian"] = "_cd7"
    languages_dict["Finnish"] = "_cd8"
    languages_dict["French"] = "_cd9"
    languages_dict["Gaelic"] = "_cd10"
    languages_dict["German"] = "_cd11"
    languages_dict["Greek"] = "_cd12"
    languages_dict["Hebrew"] = "_cd13"
    languages_dict["Hungarian"] = "_cd14"
    languages_dict["Indonesian"] = "_cd15"
    languages_dict["Italian"] = "_cd16"
    languages_dict["Japanese"] = "_cd17"
    languages_dict["Kazakh"] = "_cd18"
    languages_dict["Korean"] = "_cd19"
    languages_dict["Latvian"] = "_cd20"
    languages_dict["Lithuanian"] = "_cd21"
    languages_dict["Norwegian"] = "_cd22"
    languages_dict["Persian"] = "_cd23"
    languages_dict["Polish"] = "_cd24"
    languages_dict["Portuguese"] = "_cd25"
    languages_dict["Romanian"] = "_cd26"
    languages_dict["Russian"] = "_cd27"
    languages_dict["Serbian"] = "_cd28"
    languages_dict["Simplified Chinese"] = "_cd29"
    languages_dict["Slovakian"] = "_cd30"
    languages_dict["Spanish"] = "_cd31"
    languages_dict["Swedish"] = "_cd32"
    languages_dict["Thai"] = "_cd33"
    languages_dict["Traditional Chinese"] = "_cd34"
    languages_dict["Turkish"] = "_cd35"
    languages_dict["Ukrainian"] = "_cd36"
    languages_dict["Vietnamese"] = "_cd37"
    return languages_dict[countryName]

#지원언어
def chooseCountry(countryName):
    country_dict = {}
    country_dict["Algeria"] = "DZA"
    country_dict["Argentina"] = "ARG"
    country_dict["Australia"] = "AUS"
    country_dict["Austria"] = "AUT"
    country_dict["Bahrain"] = "BHR"
    country_dict["Belarus"] = "BLR"
    country_dict["Belgium"] = "BEL"
    country_dict["Brazil"] = "BRA"
    country_dict["Bulgaria"] = "BGR"
    country_dict["Canada"] = "CAN"
    country_dict["Chile"] = "CHL"
    country_dict["China"] = "CHN"
    country_dict["Colombia"] = "COL"
    country_dict["Croatia"] = "HRV"
    country_dict["Czech"] = "CZE"
    country_dict["Denmark"] = "DNK"
    country_dict["Egypt"] = "EGY"
    country_dict["Estonia"] = "EST"
    country_dict["English"] = "ENG"
    country_dict["Finland"] = "FIN"
    country_dict["France"] = "FRA"
    country_dict["German"] = "DEU"
    country_dict["Hong Kong"] = "HKG"
    country_dict["Hungary"] = "HUN"
    country_dict["India"] = "IND"
    country_dict["Indonesia"] = "IDN"
    country_dict["Iran"] = "IRN"
    country_dict["Iraq"] = "IRQ"
    country_dict["Ireland"] = "IRL"
    country_dict["Israel"] = "ISR"
    country_dict["Italy"] = "ITA"
    country_dict["Japan"] = "JPN"
    country_dict["Jordan"] = "JOR"
    country_dict["Kazakhstan"] = "KAZ"
    country_dict["Kenya"] = "KEN"
    country_dict["Korea"] = "KOR"
    country_dict["Korean"] = "KOR"
    country_dict["Kuwait"] = "KWT"
    country_dict["Latvia"] = "LVA"
    country_dict["Lebanon"] = "LBN"
    country_dict["Libya"] = "LBY"
    country_dict["Lithuania"] = "LTU"
    country_dict["Luxembourg"] = "LUX"
    country_dict["Malaysia"] = "MYS"
    country_dict["Mexico"] = "MEX"
    country_dict["Morocco"] = "MAR"
    country_dict["Netherlands"] = "NLD"
    country_dict["New Zealand"] = "NZL"
    country_dict["Nigeria"] = "NGA"
    country_dict["Norway"] = "NOR"
    country_dict["Oman"] = "OMN"
    country_dict["Peru"] = "PER"
    country_dict["Philippines"] = "PHL"
    country_dict["Poland"] = "POL"
    country_dict["Portugal"] = "PRT"
    country_dict["Qatar"] = "QAT"
    country_dict["Romania"] = "ROU"
    country_dict["Russia"] = "RUS"
    country_dict["Saudi Arabia"] = "SAU"
    country_dict["Serbia"] = "SRB"
    country_dict["Simplified Chinese"] = "ZHO"
    country_dict["Singapore"] = "SGP"
    country_dict["Slovakia"] = "SVK"
    country_dict["South Africa"] = "ZAF"
    country_dict["Spain"] = "ESP"
    country_dict["Spanish"] = "SPA"
    country_dict["Spanish_Latin"] = "LAT"
    country_dict["Sweden"] = "SWE"
    country_dict["Switzerland"] = "CHE"
    country_dict["Taiwan"] = "TWN"
    country_dict["Thailand"] = "THA"
    country_dict["Tunisia"] = "TUN"
    country_dict["Turkey"] = "TUR"
    country_dict["USA"] = "USA"
    country_dict["Ukraine"] = "UKR"
    country_dict["United Arab Emirates"] = "ARE"
    country_dict["United Kingdom"] = "GBR"
    country_dict["Vietnam"] = "VNM"
    country_dict["Yemen"] = "YEM"
    return country_dict[countryName]

def call_category1(category1):
    category_dict = {}
    category_dict['Pink'] = '0'
    category_dict['Red'] = '1'
    category_dict['Orange'] = '2'
    category_dict['Brown'] = '3'
    category_dict['Yellow'] = '4'
    category_dict['Green'] = '5'
    category_dict['Blue'] = '6'
    category_dict['Purple'] = '7'
    category_dict['Black'] = '8'
    category_dict['Grey'] = '9'
    category_dict['White'] = '10'
    category_dict['Gold'] = '11'
    return category_dict[category1]

def call_category2(category2):
    category_dict = {}
    category_dict['Cute'] = '0'
    category_dict['Simple'] = '1'
    category_dict['Colorful'] = '2'
    category_dict['Pastel'] = '3'
    category_dict['Modern'] = '4'
    category_dict['Sentimental'] = '5'
    category_dict['Illustrations'] = '6'
    category_dict['Patterns'] = '7'
    category_dict['Nature'] = '8'
    category_dict['Travel'] = '9'
    category_dict['Entertainment'] = '10'
    category_dict['Technology'] = '11'
    category_dict['Seasonal'] = '12'
    category_dict['Sports'] = '13'
    category_dict['Art'] = '14'
    category_dict['Other'] = '15'
    return category_dict[category2]

def call_subCategory(subCategory1):
    firstSubCategory_dict = {}
    firstSubCategory_dict['Digital'] = '0'
    firstSubCategory_dict['Analog'] = '1'
    firstSubCategory_dict['Collaborations'] = '2'
    firstSubCategory_dict['Sports/Health'] = '3'
    firstSubCategory_dict['Art'] = '4'
    firstSubCategory_dict['Interactive'] = '5'
    firstSubCategory_dict['Informative'] = '6'
    firstSubCategory_dict['Others'] = '7'
    return firstSubCategory_dict[subCategory1]

def call_mainCategory(mainCategory2):
    secondMainCategory_dict = {}
    secondMainCategory_dict['Watch faces'] = '0'
    secondMainCategory_dict['Health/Fitness'] = '1'
    secondMainCategory_dict['Gear Games'] = '2'
    secondMainCategory_dict['Finance'] = '3'
    secondMainCategory_dict['Lifestyle'] = '4'
    secondMainCategory_dict['Social Networking'] = '5'
    secondMainCategory_dict['Entertainment'] = '6'
    secondMainCategory_dict['Utilities'] = '7'
    return secondMainCategory_dict[mainCategory2]
















