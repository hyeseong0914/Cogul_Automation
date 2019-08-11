import pandas, xlrd, re, os, datetime, json
from cogul_theme import theme
from cogul_watch import watch

excelFile = pandas.read_excel("190808/input1_1.xlsx")
result_list = []

types = excelFile['바이너리 타입'].values
paths = excelFile['경로'].values
upload_file1 = excelFile['업로드 파일명1'].values
upload_file2 = excelFile['업로드 파일명2'].values
add_language = excelFile['언어 추가'].values
application_name = excelFile['어플리케이션명'].values
description = excelFile['설명'].values
tags = excelFile['태그'].values
ringTone = excelFile['Ring Tone'].values
alarmTone = excelFile['Alarm Tone'].values
notificationSound = excelFile['Notification Sound'].values
touchSound = excelFile['Touch Sound'].values
navigationBarKeySound = excelFile['Navigation Bar Key Sound'].values
daialingKeypadTone = excelFile['Dialing Keypad Tone'].values
keyboardSound = excelFile['Keyboard Sound'].values
backspaceButton = excelFile['Backspace Button'].values
category1 = excelFile['카테고리#1'].values
category2 = excelFile['카테고리#2'].values
watchIcon = excelFile['워치 아이콘'].values
watchPreview = excelFile['워치 미리보기'].values
sellerIcon = excelFile['판매자 아이콘'].values
sellerURL = excelFile['판매자 URL'].values
sellerName = excelFile['판매자명'].values
supportLanguage = excelFile['지원언어'].values
youtubeURL = excelFile['Youtube URL'].values
customerSupportEmail = excelFile['고객지원 이메일'].values
resultsNotificationEmail = excelFile['결과 통보'].values
multipleThings = excelFile['어플리케이션명, 설명, 태그'].values
excludedTerminals = excelFile['출시제외 단말'].values
standardPrice = excelFile['표준가격'].values
priceByCountry = excelFile['국가:price'].values
excludedCountry = excelFile['출시제외 국가'].values
sellingStartDate = excelFile['판매 시작일'].values
authenticationFiles = excelFile['인증 파일'].values
authenticationNotes = excelFile['인증 메모'].values

# print(len(excludedTerminals))
# for i in excludedTerminals:
#     if type(i) != float:
#         print(i, type(i))

# print(len(authenticationFiles))
# for i in authenticationFiles:
#     if str(i) != "nan":
#         print(i, type(i))

for i in range(len(types)):
    excludedTerminal_list = excludedTerminals[i]
    add_language_list = add_language[i]
    tag_list = tags[i]
    resultsNotificationEmail_list = resultsNotificationEmail[i]
    multipleThings_list = multipleThings[i]
    supportLanguage_list = supportLanguage[i]
    priceByCountry_list = priceByCountry[i]
    excludedCountry_list = excludedCountry[i]
    watchPreview_list = watchPreview[i]
    category1_list = category1[i]
    category2_list = category2[i]

    if type(excludedTerminals[i]) != float:
        excludedTerminal_list = excludedTerminals[i].split("##")

    if type(add_language[i]) != float:
        if "##" in add_language[i]:
            add_language_list = add_language[i].split('##')

    if type(tags[i]) != float:
        if "##" in tags[i]:
            tag_list = tags[i].split("##")

    if type(resultsNotificationEmail[i]) != float:
        if "##" in resultsNotificationEmail[i]:
            resultsNotificationEmail_list = resultsNotificationEmail[i].split("##")

    if type(multipleThings[i]) != float:
        if "##" in multipleThings[i]:
            multipleThings_list = multipleThings[i].split("##")

    if type(supportLanguage[i]) != float:
        if "##" in supportLanguage[i]:
            supportLanguage_list = supportLanguage[i].split("##")

    if type(priceByCountry[i]) != float:
        if "##" in priceByCountry[i]:
            priceByCountry_list = priceByCountry[i].split("##")

    if str(excludedCountry[i]) != "nan":
        if "##" in excludedCountry[i]:
            excludedCountry_list = excludedCountry[i].split("##")

    if str(watchPreview[i]) != "nan":
        if "##" in watchPreview[i]:
            watchPreview_list = watchPreview[i].split("##")

    if type(category1[i]) != float:
        if "##" in category1[i]:
            category1_list = category1[i].split("##")

    if type(category2[i]) != float:
        if "##" in category2[i]:
            category2_list = category2[i].split("##")


    if types[i].lower() == 'theme':
        theme(types[i], paths[i], upload_file1[i], upload_file2[i], add_language_list, application_name[i], description[i], tag_list, ringTone[i], alarmTone[i],
              notificationSound[i], touchSound[i], navigationBarKeySound[i], daialingKeypadTone[i], keyboardSound[i], backspaceButton[i], category1[i], category2[i], sellerIcon[i],
              sellerURL[i], sellerName[i], supportLanguage_list, youtubeURL[i], customerSupportEmail[i], resultsNotificationEmail_list, multipleThings_list,
              excludedTerminal_list, standardPrice[i], priceByCountry_list, excludedCountry_list, sellingStartDate[i], authenticationFiles[i], authenticationNotes[i])
    elif types[i].lower() == 'icon':
        theme(types[i], paths[i], upload_file1[i], upload_file2[i] ,add_language_list, application_name[i], description[i], tag_list, ringTone[i], alarmTone[i],
              notificationSound[i], touchSound[i], navigationBarKeySound[i], daialingKeypadTone[i], keyboardSound[i], backspaceButton[i], category1[i], category2[i], sellerIcon[i],
              sellerURL[i], sellerName[i], supportLanguage_list, youtubeURL[i], customerSupportEmail[i], resultsNotificationEmail_list, multipleThings_list,
              excludedTerminal_list, standardPrice[i], priceByCountry_list, excludedCountry_list, sellingStartDate[i], authenticationFiles[i], authenticationNotes[i])
    elif types[i].lower() == 'wallpaper':
        theme(types[i], paths[i], upload_file1[i], upload_file2[i], add_language_list, application_name[i], description[i], tag_list, ringTone[i], alarmTone[i],
              notificationSound[i], touchSound[i], navigationBarKeySound[i], daialingKeypadTone[i], keyboardSound[i], backspaceButton[i], category1[i], category2[i], sellerIcon[i],
              sellerURL[i], sellerName[i], supportLanguage_list, youtubeURL[i], customerSupportEmail[i], resultsNotificationEmail_list, multipleThings_list,
              excludedTerminal_list, standardPrice[i], priceByCountry_list, excludedCountry_list, sellingStartDate[i], authenticationFiles[i], authenticationNotes[i])
    elif types[i].lower() == 'livewallpaper':
        theme(types[i], paths[i], upload_file1[i], upload_file2[i], add_language_list, application_name[i], description[i], tag_list, ringTone[i], alarmTone[i],
              notificationSound[i], touchSound[i], navigationBarKeySound[i], daialingKeypadTone[i], keyboardSound[i], backspaceButton[i], category1[i], category2[i], sellerIcon[i],
              sellerURL[i], sellerName[i], supportLanguage_list, youtubeURL[i], customerSupportEmail[i], resultsNotificationEmail_list, multipleThings_list,
              excludedTerminal_list, standardPrice[i], priceByCountry_list, excludedCountry_list, sellingStartDate[i], authenticationFiles[i], authenticationNotes[i])
    elif types[i].lower() == 'watch':
        watch(paths[i], upload_file1[i], add_language_list, application_name[i], description[i], tag_list, category1_list, category2_list, watchIcon[i], watchPreview_list, supportLanguage_list,
              customerSupportEmail[i], resultsNotificationEmail_list, multipleThings_list, excludedTerminal_list, standardPrice[i], priceByCountry_list, excludedCountry_list,
              sellingStartDate[i], authenticationFiles[i], authenticationNotes[i])

