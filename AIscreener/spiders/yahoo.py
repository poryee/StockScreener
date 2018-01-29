# coding: utf-8
import scrapy
from scrapy.spiders import BaseSpider
from AIscreener.items import AiscreenerItem


class StockSpider(BaseSpider):

    name = 'stock'
    allowed_domains = ['sg.finance.yahoo.com']

    def start_requests(self):
        stocks = ["1A0", "1A1", "1A4", "1A5W", "1B0", "1B1", "1B5W", "1B6", "1C0", "1C1W", "1C3", "1C4W", "1C5", "1C9W", "1D0", "1D1", "1D3", "1D4", "1D5", "1D8", "1E0W", "1E1W", "1.00E+03", "1.00E+06", "1E7W", "1F0", "1F1", "1F2", "1F3", "1F4", "1F9W", "1G1", "1G3R", "1G4R", "1G5W", "1G6", "1G7W", "1G9R", "1H0R", "1H1W", "1H2", "1H3", "1H4", "3UIS", "3UJS", "40B", "40D", "40E", "40F", "40N", "40R", "40S", "40T", "40U", "40V", "40W", "41A", "41B", "41F", "41H", "41O", "41RW", "41S", "41T", "42C", "42D", "42E", "42F", "42G", "42H", "42L", "42N", "42O", "42QW", "42R", "42S", "42T", "42U", "42VW", "42W", "42Z", "43A", "43B", "43CW", "43E", "43F", "43IW", "43MW", "43P", "43Q", "500", "502", "504", "505", "508", "510", "528", "532", "533", "539", "540", "541", "543", "544", "545", "546", "554", "557", "558", "561", "564", "566", "567", "569", "570", "571", "573", "574", "575", "578", "579", "580", "581", "583", "584", "585", "586", "588", "593", "594", "595", "596", "5AB", "5AE", "5AI", "5AL", "5AM", "5AU", "5BI", "5BS", "5CF", "5CH", "5CJ", "5CN", "5CP", "5CQ", "5CR", "5CT", "5DA", "5DD", "5DL", "5DM", "5DN", "5DO", "5DP", "5DS", "5DW", "5DX", "5EB", "5EC", "5EF", "5EG", "5EK", "5EL", "5EN", "5ET", "5EV", "5EW", "5F4", "5F7", "5FA", "5FH", "5FI", "5FL", "5FW", "5FX", "5G1", "5G2", "5G3", "5G4", "5G9", "5GC", "5GD", "5GF", "5GI", "5GJ", "5GZ", "5H0", "5H7W", "5HC", "5HG", "5HH", "5HJ", "5HT", "5HV", "5I0", "5I1", "5I2W", "5I3", "5I4", "5IB", "5IC", "5IE", "5IF", "5IG", "5JK", "5JS", "5KI", "5KT", "5LE", "5LY", "5MD", "5ME", "5ML", "5MM", "5MQ", "5MS", "5MZ", "5NF", "5NG", "5NK", "5NV", "5OC", "5OI", "5OQ", "5OR", "5OS", "5OT", "5OU", "5OX", "5PC", "5PD", "5PF", "5PI", "5PL", "5PO", "5QR", "5QT", "5QY", "5RA", "5RC", "5RE", "5RF", "5RJ", "5SO", "5SR", "5SY", "5TG", "5TI", "5TJ", "5TN", "5TP", "5TR", "5TS", "5TT", "5TW", "5TY", "5UA", "5UE", "5UF", "5UJ", "5UL", "5UN", "5UO", "5UX", "5UZ", "5VC", "5VI", "5VJ", "5VNW", "5VOW", "5VP", "5VS", "5VU", "5VZW", "5WA", "5WD", "5WE", "5WF", "5WG", "5WH", "5WJ", "5WV", "600", "6SUS", "7PMS", "7QQS", "A04", "A05", "A0W", "A13", "A17U", "A26", "A27", "A30", "A31", "A33", "A34", "A35", "A50", "A52", "A55", "A68U", "A75", "A78", "A7RU", "A7S", "A9A", "A9B", "AAJ", "ACV", "ACW", "AD7", "AD8", "ADJ", "ADN", "ADP", "ADQU", "AFC", "AFUS", "AFVS", "AGS", "AIY", "AJ2", "AJBU", "AJHW", "AO9", "AOF", "AP4", "AU8U", "AUE", "AVM", "AVV", "AVX", "AW9U", "AWC", "AWE", "AWG", "AWI", "AWK", "AWM", "AWO", "AWS", "AWUW", "AWV", "AWX", "AWZ", "AXB", "AXL", "AXXZ", "AYB", "AYD", "AYL", "AYN", "AYV", "AZA", "AZG", "AZI", "AZR", "AZT", "AZW", "AZY", "AZZ", "B", "B07", "B0I", "B0Z", "B10", "B16", "B26", "B28", "B2F", "B49", "B58", "B61", "B66", "B69", "B73", "B7K", "B9S", "BABW", "BAC", "BAI", "BAZ", "BBP", "BBW", "BCD", "BCV", "BCY", "BCZ", "BDA", "BDF", "BDN", "BDR", "BDU", "BDX", "BEC", "BEH", "BEI", "BEV", "BEW", "BEYZ", "BEZ", "BFI", "BFK", "BFT", "BFU", "BGK", "BGO", "BHD", "BHK", "BHO", "BHQ", "BHU", "BIOZ", "BIP", "BIX", "BJD", "BJE", "BJFZ", "BJGS", "BJHS", "BJIS", "BJJS", "BJL", "BJV", "BJW", "BJZ", "BKA", "BKK", "BKV", "BKW", "BKX", "BKY", "BKZ", "BLA", "BLH", "BLIW", "BLJW", "BLL", "BLR", "BLS", "BLT", "BLU", "BLW", "BLZ", "BMA", "BMGU", "BMH", "BMNW", "BMT", "BN2", "BN4", "BNE", "BOL", "BOU", "BOVW", "BPF", "BQC", "BQD", "BQF", "BQI", "BQM", "BQN", "BQO", "BQP", "BR9", "BRD", "BRE", "BRHW", "BRQZ", "BRR", "BRS", "BS6", "BSHW", "BSKZ", "BSL", "BTE", "BTF", "BTG", "BTJ", "BTM", "BTNZ", "BTOU", "BTP", "BTWZ", "BTX", "BTY", "BUOU", "BUPW", "BVA", "BVP", "BVQ", "BWCU", "BWM", "BWQU", "BXE", "BXLW", "BYI", "BYJ", "BZKS", "C04", "C05", "C06", "C07", "C09", "C13", "C14", "c29", "C2PU", "C31", "C33", "C38U", "C41", "C50", "C52", "C56", "C61U", "C6L", "C70", "C71", "C76", "C86", "C8R", "C92", "C9Q", "CC3", "CDVZ", "CDWW", "CDXW", "CEDU", "CEE", "CEGW", "CFA", "CFN", "CGN", "CGOW", "CGP", "CH8", "CHBW", "CHJ", "CHSW", "CHTW", "CHUW", "CHWW", "CHXW", "CHYW", "CHZ", "CIN", "CIOW", "CIPW", "CIQW", "CIRW", "CISW", "CITW", "CIUW", "CIVW", "CIWW", "CIXW", "CJFW", "CJGW", "CJHW", "CJIW", "CJLU", "CJMW", "CJN", "CJXW", "CJYW", "CJZW", "CKAW", "CKBW", "CKLW", "CKMW", "CKNW", "CKOW", "CKRW", "CKSW", "CKTW", "CKXW", "CKYW", "CKZW", "CLAW", "CLDW", "CLHW", "CLIW", "CLJW", "CLN", "CLR", "CLVW", "CLWW", "CLYW", "CLZW", "CMAW", "CMBW", "CMCW", "CMDW", "CMEW", "CMFW", "CMKW", "CMLW", "CMMW", "CMOU", "CMPW", "CMQW", "CMRW", "CMSW", "CMTW", "CMUW", "CMVW", "CMWW", "CMXW", "CMYW", "CMZW", "CNAW", "CNBW", "CNCW", "CNDW", "CNE", "CNFW", "CNGW", "CNHW", "CNIW", "CNJW", "CNKW", "CNLW", "CNMW", "CNNU", "CNOW", "CNPW", "CNQW", "CNRW", "CNSW", "COCR", "CODR", "COGW", "COHW", "COJW", "COKW", "COMW", "CONW", "COOW", "COPW", "COTW", "COUW", "COVW", "COXW", "COYW", "COZW", "CPBW", "CPCW", "CPDW", "CPEW", "CPFW", "CPGW", "CPHW", "CPIW", "CY6U", "CZ4", "D01", "D03", "D05", "D07", "D11", "D2U", "D50", "D5IU", "D6U", "D79", "D8DU", "DK2", "DM0", "DU4", "E16", "E23", "E27", "E28", "E3B", "E5H", "E6R", "E8Z", "E90", "E9L", "EB5", "EB7", "EE6", "EG0", "EH5", "ER0", "ES3", "F03", "F10", "F12", "F13", "F17", "F1E", "F25U", "F31", "F34", "F3V", "F83", "F86", "F99", "F9D", "FP1", "FQ7", "FQ8", "G07", "G08", "G0I", "G11", "G13", "G1K", "G1M", "G1N", "G1O", "G20", "G3B", "G41", "G50", "G54", "G5X", "G92", "GG0", "GU5", "H02", "H07", "H12", "H13", "H15", "H16", "H17", "H18", "H19", "H1N", "H1O", "H1P", "H1Q", "H20", "H22", "H27", "H30", "H78", "HD6", "HD7", "HD8", "HD9", "HE0", "i06", "i07", "i11", "i15", "i26", "i49", "I5H", "I85", "I98", "I9T", "IH0", "IH1", "IH2", "IH3", "IH4", "IW5", "IX2", "J03", "J0O", "J0P", "J0Q", "J0R", "J17", "J18", "J2T", "J36", "J37", "J69U", "J85", "J91U", "JA9", "JC5", "JC6", "JC7", "JK8", "K03", "K11", "K14", "K1Q", "K22", "K29", "K2LU", "K3CD", "K3DD", "K3ED", "K3FD", "K3HD", "K3ID", "K3JD", "K3MD", "K3OD", "K3PD", "K3RD", "K3SD", "K3TD", "K6K", "K6S", "K6Y", "K71U", "K75", "KF5", "KF6", "KF7", "KF8", "KI3", "KJ5", "KJ7", "KJ9", "KT3", "KT4", "KT9", "KV4", "KV8", "L02", "L03", "L09", "L17", "L19", "L22", "L23", "L38", "L46", "L5I", "LF1", "LF2", "LG6", "LG7", "LG8", "LG9", "LJ3", "LS9", "M01", "M03", "M04", "M05", "M11", "M14", "M15", "M1GU", "M1Z", "M30", "M35", "M44U", "M62", "MC0", "ME8U", "MF6", "MR7", "MR8", "MS7", "MT1", "MU7", "MV4", "N01", "N02", "N08", "N0Z", "N14", "N2E", "N2H", "N2IU", "N32", "N33", "N4E", "N5YD", "N6DD", "N6ED", "N6FD", "N6M", "NC2", "NC9", "ND8U", "NO4", "NR7", "NS8U", "O08", "O10", "O2I", "O32", "O39", "O5RU", "O6Z", "O87", "O9A", "O9C", "O9D", "O9E", "O9P", "OL9S", "OM0S", "OM5S", "OU8", "OV8", "P01", "P11", "P15", "P19", "P2P", "P2Q", "P34", "P36", "P40U", "P52", "P58", "P5P", "P60", "P74", "P7VU", "P8A", "P8Z", "P9D", "PA3", "PH0", "PH1S", "PU6D", "Q01", "Q0F", "Q0X", "Q1P", "Q5T", "QC7", "QF6", "QG1", "QK9", "QL2", "QL3", "QR9", "QS0", "QS9", "R07", "R14", "R1LS", "R1MS", "R1NS", "R9IW", "RC5", "RE2", "RE4", "RF1U", "RF7", "RQ1", "RS1", "RW0U", "S07", "S08", "S19", "S20", "S21", "S23", "S27", "S29", "S2D", "S35", "S3N", "S41", "S44", "S45U", "S46", "S49", "S51", "S56", "S58", "S59", "S61", "S63", "S68", "S69", "S71", "S7OU", "S7P", "S85", "S91", "S9B", "SK3", "SK6U", "SK7", "SO7", "SV3U", "T03", "T09", "T12", "T13", "T14", "T15", "T18", "T19", "T24", "T39", "T41", "T43", "T4B", "T4E", "T55", "T6I", "T82U", "T8B", "T8FS", "T8GS", "T8UW", "T8V", "TQ5", "TS0U", "TY6Z", "U04", "U05", "U06", "U09", "U10", "U11", "U13", "U14", "U6C", "U77", "U96", "U9E", "UD1U", "UD2", "UQ4", "UQ7", "UV1", "V01", "V03", "W05", "X06", "Y03", "Y06", "Y35", "Y45", "Y92", "Z25", "Z59", "Z74", "Z77"]
        #stocks = ["1A0","1A1"]
        BASE_URL = "https://sg.finance.yahoo.com/quote/{}/key-statistics?p={}"
        for s in stocks:
            #print(BASE_URL.replace("{}",s+".SI"))
            yield scrapy.Request(url=BASE_URL.replace("{}",s+".SI"))


    def parse(self, response):

        item = AiscreenerItem()

        NAME_SELECTOR = 'id("quote-header-info")/div[2]/div[1]/div[1]/h1[1]//text()'
        CURRENCY_SELECTOR = '//*[@id="Col1-3-KeyStatistics-Proxy"]/section/div[1]/span//text()'

        YEAR_LOW_SELECTOR = '//*[@id="Col1-3-KeyStatistics-Proxy"]/section/div[2]/div[2]/div/div[1]/table/tbody/tr[5]/td[2]//text()'
        YEAR_HIGH_SELECTOR = '//*[@id="Col1-3-KeyStatistics-Proxy"]/section/div[2]/div[2]/div/div[1]/table/tbody/tr[4]/td[2]//text()'
        MARKETCAP_SELETOR = '//*[@id="Col1-3-KeyStatistics-Proxy"]/section/div[2]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]//text()'
        PE_SELECTOR = '//*[@id="Col1-3-KeyStatistics-Proxy"]/section/div[2]/div[1]/div[1]/div/table/tbody/tr[3]/td[2]//text()'
        BV_SELECTOR = '//*[@id="Col1-3-KeyStatistics-Proxy"]/section/div[2]/div[1]/div[3]/div[5]/table/tbody/tr[6]/td[2]//text()'
        PB_SELECTOR = '//*[@id="Col1-3-KeyStatistics-Proxy"]/section/div[2]/div[1]/div[1]/div/table/tbody/tr[7]/td[2]//text()'
        DIVIDENT_SELECTOR = '//*[@id="Col1-3-KeyStatistics-Proxy"]/section/div[2]/div[2]/div/div[3]/table/tbody/tr[4]/td[2]//text()'
        PEG_SELECTOR = '//*[@id="Col1-3-KeyStatistics-Proxy"]/section/div[2]/div[1]/div[1]/div/table/tbody/tr[5]/td[2]//text()'


        item['name']=response.xpath(NAME_SELECTOR).extract()
        item['currency'] = response.xpath(CURRENCY_SELECTOR).extract()

        item['year_low'] = response.xpath(YEAR_LOW_SELECTOR).extract()
        item['year_high'] = response.xpath(YEAR_HIGH_SELECTOR).extract()
        item['marketcap'] = response.xpath(MARKETCAP_SELETOR).extract()
        item['pe_ratio'] = response.xpath(PE_SELECTOR).extract()
        item['bookvalue'] = response.xpath(BV_SELECTOR).extract()
        item['pb_ratio'] = response.xpath(PB_SELECTOR).extract()
        item['trailingdivident'] = response.xpath(DIVIDENT_SELECTOR).extract()
        item['PEG'] = response.xpath(PEG_SELECTOR).extract()


        request=scrapy.Request(response.url.replace("/key-statistics",""),callback=self.parse_page2)
        request.meta['item']=item
        return request
        #//*[@id="quote-nav"]/ul/li[1]/a
        #next_page_url = response.xpath('/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/section/ul/li[1]/a').extract_first()
        #if next_page_url:
            #absolute_next_page_url = response.urljoin(next_page_url)
            #yield scrapy.Request(absolute_next_page_url)

    #page2 summary page to extract price info
    def parse_page2(self, response):
        item = response.meta['item']
        #xpath selector for price
        PRICE_SELECTOR = '//*[@id="quote-header-info"]/div[3]/div/span/text()'
        #summary_price = response.xpath(PRICE_SELECTOR).extract_first()
        item['price']=response.xpath(PRICE_SELECTOR).extract_first()

        return item
        #return callback function to parse
        #return {'page2': summary_price}


