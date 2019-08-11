from selenium import webdriver
import time, os
from methods import determineSeconds, chooseLanguage, chooseCountry, call_category1, call_category2
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def theme(theme_type, path, upload1, upload2, languages, title, description, tags, ringTone, alarmTone, notificationScound, touchSound, navigationBarKeySound, diailingKeypadTone, keyboardSound, backSpaceButton, category1, category2, sellerIcon, sellerUrl, sellerName, supportedLanguages, YoutubeURL, customerSupportEmail, resultsNotificationEmail, multiplethings, excludedTerminals, standardPrice, priceByCountry, excludedCountry, sellingStartDate, authenticationFile, authenticationNote):
    seconds = 0
    fileSize = 0
    path = os.path.abspath(path)
    path = path.replace("\\", "/") + "/"
    driver = webdriver.Chrome()
    url = "https://seller.samsungapps.com/login/signIn.as?returnURL=%2Fmain%2FsellerMain.as&ssl=Y&ssoCheck=fail"
    #url = "https://account.samsung.com/accounts/v1/GAS/signInGate?locale=ko&countryCode=KR&redirect_uri=https:%2F%2Fseller.samsungapps.com%2Flogin%2FssoLogin.as&state=ro319f7hb31i4i83i68zno132m4q4xvn&goBackURL=https:%2F%2Fseller.samsungapps.com%2Fgate%2Fgate&response_type=code&client_id=6mztkyy858";
    driver.get(url)

    #로그인하기
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "삼성계정으로 로그인")))
    #driver.find_element_by_link_text('삼성계정으로 로그인').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "로그인")))
    driver.find_element_by_link_text('로그인').click()
    driver.find_element_by_id('iptLgnPlnID').send_keys('')
    driver.find_element_by_id('iptLgnPlnPD').send_keys('')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "signInButton")))
    time.sleep(1)
    driver.find_element_by_css_selector('.btn-continuew > #signInButton').click()

    ####### 신규 어플케이션 추가
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#btn_add_new_app > img")))
    driver.find_element_by_css_selector('#btn_add_new_app > img').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".opentheme")))
    driver.find_element_by_css_selector('.opentheme').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".on .btn_next > span")))
    driver.find_element_by_css_selector('.on .btn_next > span').click()

    ######바이너리
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_tbl_01 > .inr_btn > span:nth-child(1)")))
    driver.find_element_by_css_selector('.btn_tbl_01 > .inr_btn > span:nth-child(1)').click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".check_off:nth-child(2) > .ipt_radio_01")))
    driver.find_element_by_css_selector('.check_off:nth-child(2) > .ipt_radio_01').click()

    # 업로드 파일1
    seconds = determineSeconds(path + upload1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    driver.find_element_by_xpath("//input[@type='file']").send_keys(path + upload1)
    time.sleep(seconds)

    # 저장
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_04 > span")))
    driver.find_element_by_css_selector('.btn_04 > span').click()
    time.sleep(10)

    # 업로드 파일2
    if type(upload2) != float:
        # 두 번째 바이너리 추가하기 버튼 클릭
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_tbl_01 > .inr_btn > span:nth-child(2)")))
        driver.find_element_by_css_selector('.btn_tbl_01 > .inr_btn > span:nth-child(2)').click()
        time.sleep(1)
        # 아니오
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".check_off:nth-child(2) > .ipt_radio_01")))
        driver.find_element_by_css_selector('.check_off:nth-child(2) > .ipt_radio_01').click()
        # 업로드
        seconds = determineSeconds(path + upload2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        driver.find_element_by_xpath("//input[@type='file']").send_keys(path + upload2)
        time.sleep(seconds)

        # 저장
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_04 > span")))
        driver.find_element_by_css_selector('.btn_04 > span').click()
        time.sleep(5)

        # 확인
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#binarySaveAlertDialog > .btn_area span")))
        driver.find_element_by_css_selector('#binarySaveAlertDialog > .btn_area span').click()
        time.sleep(5)



    ###단말 제외
    if type(excludedTerminals) != float:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_tbl_02 > .inr_btn > span:nth-child(1)")))
        driver.find_element_by_css_selector('.btn_tbl_02 > .inr_btn > span:nth-child(1)').click()
        time.sleep(3)

        for i in range(len(excludedTerminals)):
            if i == 0:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inputArea > .ng-pristine")))
                driver.find_element_by_css_selector('.inputArea > .ng-pristine').send_keys(excludedTerminals[i])
                time.sleep(3)
            else:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ng-dirty:nth-child(1)")))
                driver.find_element_by_css_selector('.ng-dirty:nth-child(1)').clear()
                driver.find_element_by_css_selector('.ng-dirty:nth-child(1)').send_keys(excludedTerminals[i])
                time.sleep(3)

            # 전체 선택
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//th/label")))
            driver.find_element_by_xpath('//th/label').click()
            time.sleep(1)

        #저장
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_10 > span")))
        driver.find_element_by_css_selector('.btn_10 > span').click()
        time.sleep(8)
        #확인
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#binaryDeleteOkPopup > .btn_area span")))
        driver.find_element_by_css_selector('#binaryDeleteOkPopup > .btn_area span').click()
        time.sleep(3)

    ####### 앱 정보
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "앱 정보")))
    driver.find_element_by_link_text('앱 정보').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "단순")))
    driver.find_element_by_link_text('단순').click()

    #언어선택
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_lang_add > span")))
    driver.find_element_by_css_selector('.btn_lang_add > span').click()

    # _cd0 - Arabic                    _cd19 - Korean
    # _cd1 - Bulgarian                 _cd20 - Latvian
    # _cd2 - Croatian                  _cd21 - Lithuanian
    # _cd3 - Czech                     _cd22 - Norwegian
    # _cd4 - Danish                    _cd23 - Persian
    # _cd5 - Dutch                     _cd24 - Polish
    # _cd6 - Englsih                   _cd25 - Portuguese
    # _cd7 - Estonian                  _cd26 - Romanian
    # _cd8 - Finnish                   _cd27 - Russian
    # _cd9 - French                    _cd28 - Serbian
    # _cd10 - Gaelic                   _cd29 - Simplified Chinese
    # _cd11 - German                   _cd30 - Slovakian
    # _cd12 - Greek                    _cd31 - Spanish
    # _cd13 - Hebrew                   _cd32 - Swedish
    # _cd14 - Hungarian                _cd33 - Thai
    # _cd15 - Indonesian               _cd34 - Traditional Chinese
    # _cd16 - Italian                  _cd35 - Turkish
    # _cd17 - Japanese                 _cd36 - Ukrainian
    # _cd18 - Kazakh                   _cd37 - Vietnamese



    for i in languages:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, chooseLanguage(i))))
        driver.find_element_by_id(chooseLanguage(i)).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jQbtn_close_lang_add:nth-child(1) > span")))
    driver.find_element_by_css_selector('.jQbtn_close_lang_add:nth-child(1) > span').click()

    #애플리케이션명
    driver.find_element_by_id("contentName").send_keys(title)
    #설명
    driver.find_element_by_id("longDesc").send_keys(description)
    #태그
    for i in range(len(tags)):
        driver.find_element_by_id("etcTag" + str(i+1)).send_keys(tags[i])

    ### 미리듣기 사운드
    if theme_type == "theme":
        #Ring Tone
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
        driver.find_elements_by_xpath("//input[@type='file']")[0].send_keys(path + ringTone)
        time.sleep(5)
        #Alarm Tone
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
        driver.find_elements_by_xpath("//input[@type='file']")[1].send_keys(path + alarmTone)
        time.sleep(5)
        #Notification Sound
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
        driver.find_elements_by_xpath("//input[@type='file']")[2].send_keys(path + notificationScound)
        time.sleep(5)
        #Touch Sound
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
        driver.find_elements_by_xpath("//input[@type='file']")[3].send_keys(path + touchSound)
        time.sleep(5)
        #Navigation Bar Key Sound
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
        driver.find_elements_by_xpath("//input[@type='file']")[4].send_keys(path + navigationBarKeySound)
        time.sleep(5)
        #Daialing Keypad Tone
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
        driver.find_elements_by_xpath("//input[@type='file']")[5].send_keys(path + diailingKeypadTone)
        time.sleep(5)
        #Keyboard Sound
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
        driver.find_elements_by_xpath("//input[@type='file']")[6].send_keys(path + keyboardSound)
        time.sleep(5)
        #Backspace Button
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
        driver.find_elements_by_xpath("//input[@type='file']")[7].send_keys(path + backSpaceButton)
        time.sleep(5)

    #카테고리
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "themeGeneral2DepthCategory1")))
    selectColor = Select(driver.find_element_by_id("themeGeneral2DepthCategory1"))

    # 0 Pink
    # 1 Red
    # 2 Orange
    # 3 Brown
    # 4 Yellow
    # 5 Green
    # 6 Blue
    # 7 Purple
    # 8 Black
    # 9 Grey
    # 10 White
    # 11 Gold

    selectColor.select_by_value(call_category1(category1))

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "themeGeneral2DepthCategory2")))
    selectTopic = Select(driver.find_element_by_id("themeGeneral2DepthCategory2"))

    # 0 Cute
    # 1 Simple
    # 2 Colorful
    # 3 Pastel
    # 4 Modern
    # 5 Sentimental
    # 6 Illustrations
    # 7 Patterns
    # 8 Nature
    # 9 Travel
    # 10 Entertainment
    # 11 Technology
    # 12 Seasonal
    # 13 Sports
    # 14 Art
    # 15 Other

    selectTopic.select_by_value(call_category2(category2))


    ### 판매자 페이지 링크
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
    driver.find_elements_by_xpath("//input[@type='file']")[8].send_keys(path + sellerIcon)
    time.sleep(5)

    #판매자 URL
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sellerUrl")))
    driver.find_element_by_id("sellerUrl").send_keys(sellerUrl)
    #판매자명
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sellerName")))
    driver.find_element_by_id("sellerName").send_keys(sellerName)

    ###지원언어
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_lang_add02 > span")))
    driver.find_element_by_css_selector(".btn_lang_add02 > span").click()

    for i in supportedLanguages:
        temp = "itemAppLanguage_" + chooseCountry(i)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, temp)))
        driver.find_element_by_id(temp).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".\_addLangueSave > span")))
    driver.find_element_by_css_selector(".\_addLangueSave > span").click()

    ### YoutubeURL Animated Wallpaper랑 Theme만 추가
    if theme_type == "livewallpaper" or theme_type == "theme":
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "youTubeURLid")))
        driver.find_element_by_id("youTubeURLid").send_keys(YoutubeURL)

    ### 고객지원 이메일
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "supportedEMail")))
    driver.find_element_by_id("supportedEMail").send_keys(customerSupportEmail)

    ### 결과통보
    if type(resultsNotificationEmail) == list:
        for i in range(0, len(resultsNotificationEmail)):
            if i == 0:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "notifyResult_0")))
                driver.find_element_by_id("notifyResult_0").send_keys(resultsNotificationEmail[i])
            else:
                #더하기
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_nr_fld_add")))
                driver.find_element_by_css_selector(".btn_nr_fld_add").click()
                #입력
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "notifyResult_" + str(i))))
                driver.find_element_by_id("notifyResult_" + str(i)).send_keys(resultsNotificationEmail[i])
    else:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "notifyResult_0")))
        driver.find_element_by_id("notifyResult_0").send_keys(resultsNotificationEmail)

    ### 언어 선택해서 선택한 언어의 어플리케이션명, 설명, 태그
    for i in range(len(multiplethings)):
        temp_list = multiplethings[i].split("#")
        abbreviation = chooseCountry(temp_list[0])

        #언어선택 창 클릭
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "언어 선택")))
        driver.find_element_by_link_text('언어 선택').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, temp_list[0])))
        driver.find_element_by_link_text(temp_list[0]).click()
        #어플리케이션명
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contentName_" + abbreviation)))
        driver.find_element_by_id("contentName_" + abbreviation).send_keys(temp_list[1])
        #설명
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "longDesc_" + abbreviation)))
        driver.find_element_by_id("longDesc_" + abbreviation).send_keys(temp_list[2])

        # 태그
        count = 0
        for j in range(3, len(temp_list)):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, abbreviation+str(count))))
            driver.find_element_by_id(abbreviation+str(count)).send_keys(temp_list[j])
            count += 1

    # 앱 언어 저장하기
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_03 > span")))
    driver.find_element_by_css_selector(".btn_03 > span").click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#saveChangeSuccessAlertDialog > .btn_area span")))
    driver.find_element_by_css_selector("#saveChangeSuccessAlertDialog > .btn_area span").click()
    time.sleep(3)

    ### 앱 정보 저장하기
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".in_btn_01 > span")))
    driver.find_element_by_css_selector('.in_btn_01 > span').click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#saveChangeSuccessAlertDialog > .btn_area span")))
    driver.find_element_by_css_selector('#saveChangeSuccessAlertDialog > .btn_area span').click()
    time.sleep(3)

    ####### 국가 & 가격
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "국가 & 가격")))
    driver.find_element_by_link_text('국가 & 가격').click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "고급")))
    driver.find_element_by_link_text('고급').click()
    #유료
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rd32")))
    driver.find_element_by_id("rd32").click()
    time.sleep(5)

    #표준가격
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#standardPrice")))
    driver.find_element_by_css_selector("#standardPrice").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#standardPrice")))
    driver.find_element_by_css_selector("#standardPrice").send_keys(str(standardPrice))

    #적용
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".txt_paid span")))
    driver.find_element_by_css_selector(".txt_paid span").click()
    time.sleep(5)

    #확인
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#jQlp_alt02 .btn_lp_alert_01:nth-child(1) > span")))
    driver.find_element_by_css_selector("#jQlp_alt02 .btn_lp_alert_01:nth-child(1) > span").click()
    time.sleep(10)

    #특정국가 가격 수정
    if type(priceByCountry) == list:
        for i in range(len(priceByCountry)):
            temp_list = priceByCountry[i].split('#')
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sellPrice_" + chooseCountry(temp_list[0]))))
            driver.find_element_by_id("sellPrice_" + chooseCountry(temp_list[0])).clear()
            driver.find_element_by_id("sellPrice_" + chooseCountry(temp_list[0])).send_keys(temp_list[1])
    else:
        temp_list = priceByCountry.split('#')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sellPrice_" + chooseCountry(temp_list[0]))))
        driver.find_element_by_id("sellPrice_" + chooseCountry(temp_list[0])).clear()
        driver.find_element_by_id("sellPrice_" + chooseCountry(temp_list[0])).send_keys(temp_list[1])

    #출시제외 국가
    if str(excludedCountry) != "nan":
        for i in excludedCountry:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "chk_Country_" + chooseCountry(i))))
            driver.find_element_by_id("chk_Country_" + chooseCountry(i)).click()


    #`승인된 날짜부터 판매 시작` 체크박스 해제
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p/span/input")))
    driver.find_element_by_xpath('//p/span/input').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sellingStartDate")))
    driver.find_element_by_id("sellingStartDate").send_keys(str(sellingStartDate)[:10])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "usExportLaws")))
    driver.find_element_by_id('usExportLaws').click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_03")))
    driver.find_element_by_css_selector('.btn_03').click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".lp_notice > .btn_area span")))
    driver.find_element_by_css_selector('.lp_notice > .btn_area span').click()
    time.sleep(3)

    ###### 인증
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "인증")))
    driver.find_element_by_link_text('인증').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "appCommentData")))
    driver.find_element_by_id('appCommentData').clear()
    driver.find_element_by_id('appCommentData').send_keys(authenticationNote)

    if str(authenticationFile) != "nan":
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "certificationFileData")))
        driver.find_element_by_id('certificationFileData').send_keys(path + authenticationFile)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_03 > span")))
    driver.find_element_by_css_selector('.btn_03 > span').click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#contentCheckMsg span")))
    driver.find_element_by_css_selector('#contentCheckMsg span').click()

    driver.close()


