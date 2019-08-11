from selenium import webdriver
import time, os
from methods import determineSeconds, chooseLanguage, chooseCountry, call_subCategory, call_mainCategory
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)

def watch(path, upload1, languages, title, description, tags, category1, category2, watchIcon, watchPreviews, supportedLanguages, customerSupportEmail, resultsNotificationEmail, multiplethings, excludedTerminals, standardPrice, priceByCountry, excludedCountry, sellingStartDate, authenticationFile, authenticationNote):
    seconds = 0
    fileSize = 0
    path = os.path.abspath(path)
    path = path.replace("\\", "/") + "/"
    driver = webdriver.Chrome()
    url = "https://seller.samsungapps.com/login/signIn.as?returnURL=%2Fmain%2FsellerMain.as&ssl=Y&ssoCheck=fail"
    driver.get(url)

    #로그인하기
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "삼성계정으로 로그인")))
    driver.find_element_by_link_text('삼성계정으로 로그인').click()
    driver.find_element_by_id('iptLgnPlnID').send_keys('')
    driver.find_element_by_id('iptLgnPlnPD').send_keys('')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "signInButton")))
    time.sleep(3)
    driver.find_element_by_css_selector('.btn-continuew > #signInButton').click()

    ####### 신규 어플케이션 추가
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#btn_add_new_app > img")))
    driver.find_element_by_css_selector('#btn_add_new_app > img').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gear")))
    driver.find_element_by_css_selector('.gear').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".on .btn_next > span")))
    driver.find_element_by_css_selector('.on .btn_next > span').click()

    ###바이너리 추가하기
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "바이너리")))
    driver.find_element_by_link_text('바이너리').click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_tbl_01 > .inr_btn > span:nth-child(1)")))
    driver.find_element_by_css_selector('.btn_tbl_01 > .inr_btn > span:nth-child(1)').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "chk5")))
    driver.find_element_by_id('chk5').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@name='gms'])[2]")))
    driver.find_element_by_xpath("(//input[@name='gms'])[2]").click()

    # 파일 업로드
    seconds = determineSeconds(path + upload1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    driver.find_element_by_xpath("//input[@type='file']").send_keys(path + upload1)
    time.sleep(seconds)

    #저장
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_04 > span")))
    driver.find_element_by_css_selector('.btn_04 > span').click()
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label:nth-child(8)")))
    # driver.find_element_by_css_selector('label:nth-child(8)').click()
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_property_on > span")))
    # driver.find_element_by_css_selector('.btn_property_on > span').click()
    time.sleep(5)

    ###단말 제외
    if type(excludedTerminals) != float:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_tbl_02 > .inr_btn > span:nth-child(1)")))
        driver.find_element_by_css_selector('.btn_tbl_02 > .inr_btn > span:nth-child(1)').click()
        time.sleep(3)

        # 출시제외 단말이 하나만 있을경우 글자 한자한자로 For loop이 실행됨
        for i in range(len(excludedTerminals)):
            if i == 0:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".inputType01:nth-child(2) .ng-pristine")))
                driver.find_element_by_css_selector(".inputType01:nth-child(2) .ng-pristine").send_keys(excludedTerminals[i])
                time.sleep(3)
            else:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".ng-dirty:nth-child(1)")))
                driver.find_element_by_css_selector('.ng-dirty:nth-child(1)').clear()
                driver.find_element_by_css_selector('.ng-dirty:nth-child(1)').send_keys(excludedTerminals[i])
                time.sleep(3)

            # 전체 선택
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//th/label")))
            driver.find_element_by_xpath('//th/label').click()
            time.sleep(1)

        # 저장
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_10 > span")))
        driver.find_element_by_css_selector('.btn_10 > span').click()
        time.sleep(8)
        # 확인
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jQbtn_cls_alt14 > span")))
        driver.find_element_by_css_selector('.jQbtn_cls_alt14 > span').click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#binaryDeleteOkPopup > .btn_area span")))
        driver.find_element_by_css_selector('#binaryDeleteOkPopup > .btn_area span').click()
        time.sleep(1)

    ### 앱 정보
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

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".jQbtn_close_lang_add:nth-child(1) > span")))
    driver.find_element_by_css_selector('.jQbtn_close_lang_add:nth-child(1) > span').click()

    # 애플리케이션명
    driver.find_element_by_id("contentName").send_keys(title)
    # 설명
    driver.find_element_by_id("longDesc").send_keys(description)
    # 태그
    for i in range(len(tags)):
        driver.find_element_by_id("etcTag" + str(i + 1)).send_keys(tags[i])

    #아이콘 이미지 업로드
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
    driver.find_elements_by_xpath("//input[@type='file']")[2].send_keys(path + watchIcon)
    time.sleep(5)

    #스크린샷
    for i in range(len(watchPreviews)):
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))
        driver.find_elements_by_xpath("//input[@type='file']")[1].send_keys(path + watchPreviews[i])
        time.sleep(3)

    #카테고리
    #첫번째 Main 카테고리
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "special1ParentCategoryId")))
    selectMainCategory = Select(driver.find_element_by_id("special1ParentCategoryId"))
    # 0 Watch faces
    # 1 Health/Fitness
    # 2 Gear Games
    # 3 Finance
    # 4 Lifestyle
    # 5 Social Networking
    # 6 Entertainment
    # 7 Utilities

    selectMainCategory.select_by_value(call_mainCategory(category1[0]))


    #첫번째 Sub 카테고리
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "special1CategoryId")))
    selectSubCategory = Select(driver.find_element_by_id("special1CategoryId"))

    # 0 Digital
    # 1 Analog
    # 2 Collaborations
    # 3 Sports/Health
    # 4 Art
    # 5 Interactive
    # 6 Informative
    # 7 Others

    selectSubCategory.select_by_value(call_subCategory(category1[1]))

    #두번째 Main 카테고리
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "special2ParentCategoryId")))
    selectMain2Category = Select(driver.find_element_by_id("special2ParentCategoryId"))

    # 0 Watch faces
    # 1 Health/Fitness
    # 2 Gear Games
    # 3 Finance
    # 4 Lifestyle
    # 5 Social Networking
    # 6 Entertainment
    # 7 Utilities

    selectMain2Category.select_by_value(call_mainCategory(category2[0]))

    #두번째 Sub 카테고리
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "special2CategoryId")))
    selectSub2Category = Select(driver.find_element_by_id("special2CategoryId"))
    time.sleep(3)
    selectSub2Category.select_by_value(call_subCategory(category2[1]))

    #연령제한
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ageLimit")))
    ageLimit = Select(driver.find_element_by_id("ageLimit"))

    # 0 0+
    # 4 4+
    # 12 12+
    # 16 16+
    # 18 18+

    ageLimit.select_by_value("0")

    ###지원언어
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_lang_add02 > span")))
    driver.find_element_by_css_selector(".btn_lang_add02 > span").click()

    for i in supportedLanguages:
        temp = "itemAppLanguage_" + chooseCountry(i)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, temp)))
        driver.find_element_by_id(temp).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".\_addLangueSave > span")))
    driver.find_element_by_css_selector(".\_addLangueSave > span").click()

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
                # 더하기
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_nr_fld_add")))
                driver.find_element_by_css_selector(".btn_nr_fld_add").click()
                # 입력
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "notifyResult_" + str(i))))
                driver.find_element_by_id("notifyResult_" + str(i)).send_keys(resultsNotificationEmail[i])
    else:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "notifyResult_0")))
        driver.find_element_by_id("notifyResult_0").send_keys(resultsNotificationEmail)

    ### 앱 정보 저장하기
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".in_btn_01 > span")))
    driver.find_element_by_css_selector('.in_btn_01 > span').click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#saveChangeSuccessAlertDialog > .btn_area span")))
    driver.find_element_by_css_selector('#saveChangeSuccessAlertDialog > .btn_area span').click()
    time.sleep(3)

    ### 언어 선택해서 선택한 언어의 어플리케이션명, 설명, 태그
    for i in range(len(multiplethings)):
        temp_list = multiplethings[i].split("#")
        abbreviation = chooseCountry(temp_list[0])

        # 언어선택 창 클릭
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "언어 선택")))
        driver.find_element_by_link_text('언어 선택').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, temp_list[0])))
        driver.find_element_by_link_text(temp_list[0]).click()
        # 어플리케이션명
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contentName_" + abbreviation)))
        driver.find_element_by_id("contentName_" + abbreviation).send_keys(temp_list[1])
        # 설명
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "longDesc_" + abbreviation)))
        driver.find_element_by_id("longDesc_" + abbreviation).send_keys(temp_list[2])

        # 태그
        count = 0
        for j in range(3, len(temp_list)):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, abbreviation + str(count))))
            driver.find_element_by_id(abbreviation + str(count)).send_keys(temp_list[j])
            count += 1

    # 앱 언어 저장하기
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_03 > span")))
    driver.find_element_by_css_selector(".btn_03 > span").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#saveChangeSuccessAlertDialog > .btn_area span")))
    driver.find_element_by_css_selector("#saveChangeSuccessAlertDialog > .btn_area span").click()
    time.sleep(3)


    ####### 국가 & 가격
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "국가 & 가격")))
    driver.find_element_by_link_text('국가 & 가격').click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "고급")))
    driver.find_element_by_link_text('고급').click()
    # 유료
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rd32")))
    driver.find_element_by_id("rd32").click()
    time.sleep(5)

    # 표준가격
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#standardPrice")))
    driver.find_element_by_css_selector("#standardPrice").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#standardPrice")))
    driver.find_element_by_css_selector("#standardPrice").send_keys(str(standardPrice))

    # 적용
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".txt_paid span")))
    driver.find_element_by_css_selector(".txt_paid span").click()
    time.sleep(5)

    # 확인
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#jQlp_alt02 .btn_lp_alert_01:nth-child(1) > span")))
    driver.find_element_by_css_selector("#jQlp_alt02 .btn_lp_alert_01:nth-child(1) > span").click()
    time.sleep(10)

    # 특정국가 가격 수정
    if type(priceByCountry) == list:
        for i in range(len(priceByCountry)):
            temp_list = priceByCountry[i].split('#')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "sellPrice_" + chooseCountry(temp_list[0]))))
            driver.find_element_by_id("sellPrice_" + chooseCountry(temp_list[0])).clear()
            driver.find_element_by_id("sellPrice_" + chooseCountry(temp_list[0])).send_keys(temp_list[1])
    else:
        temp_list = priceByCountry.split('#')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sellPrice_" + chooseCountry(temp_list[0]))))
        driver.find_element_by_id("sellPrice_" + chooseCountry(temp_list[0])).clear()
        driver.find_element_by_id("sellPrice_" + chooseCountry(temp_list[0])).send_keys(temp_list[1])

    # 출시제외 국가
    if str(excludedCountry) != "nan":
        for i in excludedCountry:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "chk_Country_" + chooseCountry(i))))
            driver.find_element_by_id("chk_Country_" + chooseCountry(i)).click()

    # 승인된 날짜부터 판매 시작` 체크박스 해제
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p/span/input")))
    driver.find_element_by_xpath('//p/span/input').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sellingStartDate")))
    driver.find_element_by_id("sellingStartDate").send_keys(str(sellingStartDate)[:10])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "usExportLaws")))
    driver.find_element_by_id('usExportLaws').click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_03 > span")))
    driver.find_element_by_css_selector('.btn_03 > span').click()
    time.sleep(1)

    if WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#freePaidChangeCheckDialog > .btn_area span"))):
        driver.find_element_by_css_selector('#freePaidChangeCheckDialog > .btn_area span').click()
        time.sleep(3)

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
