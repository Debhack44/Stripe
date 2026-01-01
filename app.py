import requests

cookies = {
    '_gcl_au': '1.1.131447095.1767250600',
    '_ga': 'GA1.1.1822436907.1767250600',
    '_fbp': 'fb.2.1767250601584.882654966909328794',
    'cookiehub': 'eyJhbnN3ZXJlZCI6dHJ1ZSwicmV2aXNpb24iOjEsImRudCI6ZmFsc2UsImFsbG93U2FsZSI6dHJ1ZSwiaW1wbGljdCI6ZmFsc2UsInJlZ2lvbiI6IiIsInRva2VuIjoiIiwidGltZXN0YW1wIjoiMjAyNi0wMS0wMVQwNjo1Njo0Mi45NjBaIiwiYWxsQWxsb3dlZCI6dHJ1ZSwiY2F0ZWdvcmllcyI6W10sInZlbmRvcnMiOltdLCJzZXJ2aWNlcyI6W119',
    '__stripe_mid': 'ddf5678d-b019-4b93-999b-ccfcf6636b34a51bad',
    '__stripe_sid': '1ec4e639-7d88-4345-bcb8-3ee068c41e6d1f2a18',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2026-01-01%2006%3A27%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fget-support%2F%3F',
    'sbjs_first_add': 'fd%3D2026-01-01%2006%3A27%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fget-support%2F%3F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F',
    '_ga_JY5DRMF51J': 'GS2.1.s1767250600$o1$g1$t1767250817$j26$l0$h0',
}

headers = {
    'authority': 'www.suffolkmind.org.uk',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': '_gcl_au=1.1.131447095.1767250600; _ga=GA1.1.1822436907.1767250600; _fbp=fb.2.1767250601584.882654966909328794; cookiehub=eyJhbnN3ZXJlZCI6dHJ1ZSwicmV2aXNpb24iOjEsImRudCI6ZmFsc2UsImFsbG93U2FsZSI6dHJ1ZSwiaW1wbGljdCI6ZmFsc2UsInJlZ2lvbiI6IiIsInRva2VuIjoiIiwidGltZXN0YW1wIjoiMjAyNi0wMS0wMVQwNjo1Njo0Mi45NjBaIiwiYWxsQWxsb3dlZCI6dHJ1ZSwiY2F0ZWdvcmllcyI6W10sInZlbmRvcnMiOltdLCJzZXJ2aWNlcyI6W119; __stripe_mid=ddf5678d-b019-4b93-999b-ccfcf6636b34a51bad; __stripe_sid=1ec4e639-7d88-4345-bcb8-3ee068c41e6d1f2a18; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-01%2006%3A27%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fget-support%2F%3F; sbjs_first_add=fd%3D2026-01-01%2006%3A27%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fget-support%2F%3F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F; _ga_JY5DRMF51J=GS2.1.s1767250600$o1$g1$t1767250817$j26$l0$h0',
    'origin': 'https://www.suffolkmind.org.uk',
    'referer': 'https://www.suffolkmind.org.uk/donate/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

json_data = {
    'user_id': 0,
    'donationtype': '2',
    'donationamount': 3,
    'paymentmethod': 1,
    'donationmessage': 'Soja vaii',
    'inmemoryof': None,
    'donationamountgiftaid': None,
    'giftaid': False,
    'forename': 'Debjit',
    'surname': 'Kyro',
    'email': 'devopdjd@gmail.com',
    'title': 'Fr',
    'telephone': '6291258255',
    'address1': 'Street 107',
    'address2': 'Laura road',
    'town': 'New york ',
    'county': 'New york ',
    'country': 'United states',
    'postcode': '10080',
    'marketing_optin_email': False,
    'marketing_optin_post': False,
    'marketing_optin_telephone': False,
    'marketing_optin_sms': False,
    'marketing_optin_privacy': True,
    'marketing_optin_newsletter': False,
    'user_age_range': None,
    'user_gender': None,
    'tribute_id': None,
    'giving_id': None,
    'newsletters_subscribe_array': [],
    'grecaptcha': '0cAFcWeA5tc_G28Uo55vgedea_tNvyC9nGOr8SEHsuFsvSwz2rrBG0MMrUB4VFANeAG2qa3XQylJIXOuo_de4koewKzfetOP0cWh5rUBmip0qTrodT1nPXkuqYWx2RsaRH68dag2jRRfMGifojErosk3hB6qv8vkhsWqrPn5JCYjVKUyES6t05es-2lnfG2hYjTYIOHSEwpdnIqPGP525AP1FMilYe1j4g3D5Fgq6gkEewmdWcM2LvJdqJGeH1-1_Ig9-oC43yGXEOSeXrzZj2xrrCrfOVGzYep7W-pFZje3JgqIEYseeOHUgjdRgMdGbWqYOSci9eDalB_LAta4Q6eIm75QM1xbZ9cRRnPGP5RJDq4E9tYIwDnP-l8LmaaOm2rfpnJZcbNJkiiAiADu47HAZvyUvSMNGTSiPOdSY75tkXDyE3AEN_PxeLeUevGZt-qo5GiR4yOh7vaxVas4hTRsDn_jmxDikSp8xITu9LZZdrSmXvbNoKNFLWjau9EzIEgoMJOUOJgY6nJuNDZtDW1lEbExi51Uqe6MH3haZfBgZLwPv3pEGEmkNRJLUfrxIz7OBUn_sMgKz6CsOkh-ctn-nMsRi7fuBuauLVmB6G0gx5ytvVJFky0ozU66y2phePjfZLoLZFr08swvflyQd0E12iRvSRwTNIbd8kmfl_dZfcJfNIpK5v-BWKBiNDsXsSO3knMqFhQqT1yS0rLJBtD1svQwfopEfWqd8SqtM2saJmm-QahjhSil5RARt3n5pioM8xk8FAyMUePHBWC5K7rJdPtFjtMjybOAfQkgNytDO1CcJdikCysNSrcwWxk3PNpht2GYsbb1_VdJCI2CcBxUnJhEoYQGnKBmcaFLpbzlW3HfWmb1v_fl72iOMP5ZW7G3cyYFP9WZAahtfz2EkzG1PI0etnsO6FJjEYhpT0qy1sz5oHy1ITNRKXWBDnWhEXznwjv1MtBA2j6UN1FPIFd0Wi4glytLg0lMHe7WAHHb9kXi3Pz7Aaaz7Z5nKutYZw3IOyehZO5g7UQAncise75UJFMemROV-o_UQzc-3naXl0C7rln42zCX5Itg9Ze5HVdImVIc_wKxMnQe-T9qycNuNQNiOozHfbcUXcfrYFkBBWDNJWJyiyHAt0t8cTxxw62Nby8l2a0kRfhHVA4yHjfRYeN1OaGa23M4TVl4SidNuLIDExcVJJmte_WkMXDWIvGqNMWtRhTJlWRMBqg5Y2AjhDKgXVS95o6E1xm4KNXS4nyWURhB70ZGGKk02Nh1ILFw8g-1ZXFP7yeciv6hOuSWnsZpgh68cQCjdjPKZ8QQ_4oMJIC2kCQI37AsdIAMU8n2_jXo9tGsYHqVq6iBMPrbyRQLOD7Pt4bkU-iWOtulLcM68cyzMtVqW5GlWKr7szs92TjmG1MBTOC-6FmmXqLwxtPw5E9NvzI_qDFrDanv07FYFAPrAQvf8xvFHrWJOH03A3jy9opR9ljJzoSEcThHnzvO4hGZFwcs9O9bj4hs4QcVdKSPB69RCHdTw0_huQDPKhW9nl271I3N9X3iNBsAoCSibTMPLnSZvQplvFuOBhJHu4kNNYv0wVIt9ubUYU8yC2X554A47I-VrwPCjUKnd2V04y8VrJaiPqCZwjX0dRZMiV_fUrmPvufQ-fV-WR6q-hN74OLi8z6qQgPg62ZWxHcVlBFQKJ8w',
    'ip_address': '81.78.156.159',
    'donation_error': False,
    'customdonationamount': '3',
}

response = requests.post(
    'https://www.suffolkmind.org.uk/wp-json/donation/v1/save/',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"user_id":0,"donationtype":"2","donationamount":3,"paymentmethod":1,"donationmessage":"Soja vaii","inmemoryof":null,"donationamountgiftaid":null,"giftaid":false,"forename":"Debjit","surname":"Kyro","email":"devopdjd@gmail.com","title":"Fr","telephone":"6291258255","address1":"Street 107","address2":"Laura road","town":"New york ","county":"New york ","country":"United states","postcode":"10080","marketing_optin_email":false,"marketing_optin_post":false,"marketing_optin_telephone":false,"marketing_optin_sms":false,"marketing_optin_privacy":true,"marketing_optin_newsletter":false,"user_age_range":null,"user_gender":null,"tribute_id":null,"giving_id":null,"newsletters_subscribe_array":[],"grecaptcha":"0cAFcWeA5tc_G28Uo55vgedea_tNvyC9nGOr8SEHsuFsvSwz2rrBG0MMrUB4VFANeAG2qa3XQylJIXOuo_de4koewKzfetOP0cWh5rUBmip0qTrodT1nPXkuqYWx2RsaRH68dag2jRRfMGifojErosk3hB6qv8vkhsWqrPn5JCYjVKUyES6t05es-2lnfG2hYjTYIOHSEwpdnIqPGP525AP1FMilYe1j4g3D5Fgq6gkEewmdWcM2LvJdqJGeH1-1_Ig9-oC43yGXEOSeXrzZj2xrrCrfOVGzYep7W-pFZje3JgqIEYseeOHUgjdRgMdGbWqYOSci9eDalB_LAta4Q6eIm75QM1xbZ9cRRnPGP5RJDq4E9tYIwDnP-l8LmaaOm2rfpnJZcbNJkiiAiADu47HAZvyUvSMNGTSiPOdSY75tkXDyE3AEN_PxeLeUevGZt-qo5GiR4yOh7vaxVas4hTRsDn_jmxDikSp8xITu9LZZdrSmXvbNoKNFLWjau9EzIEgoMJOUOJgY6nJuNDZtDW1lEbExi51Uqe6MH3haZfBgZLwPv3pEGEmkNRJLUfrxIz7OBUn_sMgKz6CsOkh-ctn-nMsRi7fuBuauLVmB6G0gx5ytvVJFky0ozU66y2phePjfZLoLZFr08swvflyQd0E12iRvSRwTNIbd8kmfl_dZfcJfNIpK5v-BWKBiNDsXsSO3knMqFhQqT1yS0rLJBtD1svQwfopEfWqd8SqtM2saJmm-QahjhSil5RARt3n5pioM8xk8FAyMUePHBWC5K7rJdPtFjtMjybOAfQkgNytDO1CcJdikCysNSrcwWxk3PNpht2GYsbb1_VdJCI2CcBxUnJhEoYQGnKBmcaFLpbzlW3HfWmb1v_fl72iOMP5ZW7G3cyYFP9WZAahtfz2EkzG1PI0etnsO6FJjEYhpT0qy1sz5oHy1ITNRKXWBDnWhEXznwjv1MtBA2j6UN1FPIFd0Wi4glytLg0lMHe7WAHHb9kXi3Pz7Aaaz7Z5nKutYZw3IOyehZO5g7UQAncise75UJFMemROV-o_UQzc-3naXl0C7rln42zCX5Itg9Ze5HVdImVIc_wKxMnQe-T9qycNuNQNiOozHfbcUXcfrYFkBBWDNJWJyiyHAt0t8cTxxw62Nby8l2a0kRfhHVA4yHjfRYeN1OaGa23M4TVl4SidNuLIDExcVJJmte_WkMXDWIvGqNMWtRhTJlWRMBqg5Y2AjhDKgXVS95o6E1xm4KNXS4nyWURhB70ZGGKk02Nh1ILFw8g-1ZXFP7yeciv6hOuSWnsZpgh68cQCjdjPKZ8QQ_4oMJIC2kCQI37AsdIAMU8n2_jXo9tGsYHqVq6iBMPrbyRQLOD7Pt4bkU-iWOtulLcM68cyzMtVqW5GlWKr7szs92TjmG1MBTOC-6FmmXqLwxtPw5E9NvzI_qDFrDanv07FYFAPrAQvf8xvFHrWJOH03A3jy9opR9ljJzoSEcThHnzvO4hGZFwcs9O9bj4hs4QcVdKSPB69RCHdTw0_huQDPKhW9nl271I3N9X3iNBsAoCSibTMPLnSZvQplvFuOBhJHu4kNNYv0wVIt9ubUYU8yC2X554A47I-VrwPCjUKnd2V04y8VrJaiPqCZwjX0dRZMiV_fUrmPvufQ-fV-WR6q-hN74OLi8z6qQgPg62ZWxHcVlBFQKJ8w","ip_address":"81.78.156.159","donation_error":false,"customdonationamount":"3"}'
#response = requests.post('https://www.suffolkmind.org.uk/wp-json/donation/v1/save/', cookies=cookies, headers=headers, data=data)

print(response.json[id])

import requests

cookies = {
    '_gcl_au': '1.1.131447095.1767250600',
    '_ga': 'GA1.1.1822436907.1767250600',
    '_fbp': 'fb.2.1767250601584.882654966909328794',
    'cookiehub': 'eyJhbnN3ZXJlZCI6dHJ1ZSwicmV2aXNpb24iOjEsImRudCI6ZmFsc2UsImFsbG93U2FsZSI6dHJ1ZSwiaW1wbGljdCI6ZmFsc2UsInJlZ2lvbiI6IiIsInRva2VuIjoiIiwidGltZXN0YW1wIjoiMjAyNi0wMS0wMVQwNjo1Njo0Mi45NjBaIiwiYWxsQWxsb3dlZCI6dHJ1ZSwiY2F0ZWdvcmllcyI6W10sInZlbmRvcnMiOltdLCJzZXJ2aWNlcyI6W119',
    '__stripe_mid': 'ddf5678d-b019-4b93-999b-ccfcf6636b34a51bad',
    '__stripe_sid': '1ec4e639-7d88-4345-bcb8-3ee068c41e6d1f2a18',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2026-01-01%2006%3A27%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fget-support%2F%3F',
    'sbjs_first_add': 'fd%3D2026-01-01%2006%3A27%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fget-support%2F%3F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F',
    '_ga_JY5DRMF51J': 'GS2.1.s1767250600$o1$g1$t1767250819$j24$l0$h0',
}

headers = {
    'authority': 'www.suffolkmind.org.uk',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': '_gcl_au=1.1.131447095.1767250600; _ga=GA1.1.1822436907.1767250600; _fbp=fb.2.1767250601584.882654966909328794; cookiehub=eyJhbnN3ZXJlZCI6dHJ1ZSwicmV2aXNpb24iOjEsImRudCI6ZmFsc2UsImFsbG93U2FsZSI6dHJ1ZSwiaW1wbGljdCI6ZmFsc2UsInJlZ2lvbiI6IiIsInRva2VuIjoiIiwidGltZXN0YW1wIjoiMjAyNi0wMS0wMVQwNjo1Njo0Mi45NjBaIiwiYWxsQWxsb3dlZCI6dHJ1ZSwiY2F0ZWdvcmllcyI6W10sInZlbmRvcnMiOltdLCJzZXJ2aWNlcyI6W119; __stripe_mid=ddf5678d-b019-4b93-999b-ccfcf6636b34a51bad; __stripe_sid=1ec4e639-7d88-4345-bcb8-3ee068c41e6d1f2a18; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-01%2006%3A27%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fget-support%2F%3F; sbjs_first_add=fd%3D2026-01-01%2006%3A27%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fget-support%2F%3F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.suffolkmind.org.uk%2Fdonate%2F; _ga_JY5DRMF51J=GS2.1.s1767250600$o1$g1$t1767250819$j24$l0$h0',
    'origin': 'https://www.suffolkmind.org.uk',
    'referer': 'https://www.suffolkmind.org.uk/donate/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

json_data = {
    'amount': 3,
    'donation_id': 35749,
    'description': 'Suffolk Mind Donation',
    'email': 'devopdjd@gmail.com',
    'forename': 'Debjit',
    'surname': 'Kyro',
}

response = requests.post(
    'https://www.suffolkmind.org.uk/wp-json/donation/v1/setup_stripe/',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"amount":3,"donation_id":35749,"description":"Suffolk Mind Donation","email":"devopdjd@gmail.com","forename":"Debjit","surname":"Kyro"}'
#response = requests.post(
#    'https://www.suffolkmind.org.uk/wp-json/donation/v1/setup_stripe/',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)

yummy = [id]
print(yummy)

import requests

headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

data = 'payment_method_data[type]=card&payment_method_data[card][number]=4585815016532612&payment_method_data[card][cvc]=069&payment_method_data[card][exp_month]=11&payment_method_data[card][exp_year]=26&payment_method_data[guid]=471b2b89-ace0-45d9-8292-e0171d588fbafcb8bf&payment_method_data[muid]=ddf5678d-b019-4b93-999b-ccfcf6636b34a51bad&payment_method_data[sid]=1ec4e639-7d88-4345-bcb8-3ee068c41e6d1f2a18&payment_method_data[payment_user_agent]=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+split-card-element&payment_method_data[referrer]=https%3A%2F%2Fwww.suffolkmind.org.uk&payment_method_data[time_on_page]=184356&payment_method_data[client_attribution_metadata][client_session_id]=e559e6dc-74cc-410c-9ae8-a3f36c50e11f&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=split-card-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2017&expected_payment_method_type=card&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzY3MjUwODY1LCJjZGF0YSI6IktzVng0UFF3TTR0K2ZIais5cjduRnZyNmJhSlJQYlVabnIva2x2eHg5WjZUWXNmajZ0bXpuOEsvb2M3T0NhSkQxZElFeHB0dms4anpXM01telQxK01YLzBiV2Y0bGxCQWdOb2VpVzlXd0FjRFlqbHhpeEg2SkpTOUJ4MWc3S3BadVJ6cVBsZGNZTEw5Ni8yZ3UvbWErd3ZmWjkxdHVMRU9iSXZNYTJ3TzN1OHJJSDYwZ2ovRTdQUE1MbHkzdnNsQ3NncFJCSTNRTDB2bHMxeHQiLCJwYXNza2V5IjoiWGlSMS9EcVVveitjZ2U3clBKK2x2WXl1NGRHNGN6NUthZExtSk5jeG9mdWlXSDBxdHdxNjhwRE4ydnE3NlJickhrWmc3UDZzWE9HbXl2bDhiQzM3TzZFWVgveVRSaUV1Z0FDNEpjbEF0VE1GL2V4MVdpWTdjSjdOamV0dzdSWml5Y29kSDNwYVZsaTl1MFhpMTdDWklJL1B3N1AveFV0dnRudVhxTnpVc0libUlReFc3Y3Y4VVFySEFEWUhJT0RHNDJiSEYrbGo3YVhJNVB6NDRFM2RwQVZES1dxZXA2akY2WVNOVE1tS3ViSHp4RXB0QWNLY0xXRjIvclJWVE91Qm9rWlZzcmt5U2xkU25wVXhTN2VlVnhNK0lwTzFvTUJST1E3U1dKb3dOTENLRkxBeTg2RzVweTFSbVJTWmFGdnhlNFM2YUM4N0JkYmhnTi9FUGRiVDM2dGlsL3dkcWZZSnhjb3hTWXNNL1VGTFhRcWY2WmpWSnl0QXhJbUs3TWt2Q1l0ZGdDdUNtK01TaHQwOXhkbGo0a3U1WjFybzMxVm0xdWdoR3lGRitpU2FwRFY4MUJRemgyYUlWYmtlZVZnL2Q2M1JncVZNK1FNM3paMklIUzhHcWVVV0dLMHh3NXVDbUVkbVp4ZGFKaFY5OUZ1aWd0NHZodVZHMDJ1dHIvekFFMVpCNmdJQ292SE91VXlrcHNRTlNZMDM3d21laThqY2x1U2p5endjU0oxWDllOGg5Q0dtZHNiTVU2TmlGWTlMdmFOU0hrOVoydXdMYlpDMVo5d0tWbkJCV042a2d3cGp5dkh6bEhLZENkZS9jaFQ2OFhxU1FxU1JGSEdBZUJLYVlNbklzazRLS3ZXMFEydjRDdG1WWDFHOGEzU0JsR3pneFhMWDZtU1grQ2NIdXF1QnZvU0xQMjczdTlxb0ZyWi8zeTFaMEVGRnp2NGNETDV2N2VyQkcvQS9sa2VVOUN6TUxMc1dYV1JTOGlnRDhscVl3VytMNkhsdTl0MVdHMlhiV3l4TFloQlpkTUs5MjNFbk9SWDJpNS9UV2hCcjVrNTNyZlh2OEg0anlLcS9rUFRlaDVUS1NPc2h4MkVQMU9iR2l6L2J0YXNyeVlOYnFHUnR1ODIyY0lSdG1YTlRWQUh5NG9tSHV5RE9lRmpUZ0hRbG5pbTcvVyt6cWl1cUIySXpRNkx6RVl4SHcrMFdJcm5pZkx6VHBLZGxDKzRkdGJOc0RVY0VXbzUxWG1NTTJ5YzJOdG5pekVpUlhkNGh5OU1CbDV2bmZqUk9LT3ROTG9MOEFhSUVWVmR3R0J0RUZWMFhPd2RLaUpZVTd1VTVHVmZhaDE3NXdOL2JsQXFqN3VjRUdyTlJpKytIQ000ODJZSmdlamtSNmovL1VQWm5RaTVPUFpCVFV3MlY2MzFEZVE2L1E1dUh1dnMyTkpxVkRWZnpKOE5aTXdHejF5MkxqOXZYRWJNdVJOTUhCY3dDalVMM3l0NE5kekxvL2xKWitiOUV1eno3VUFpbTNWQVNzemdkeURqbGpPdEFsUnI4TDBrRzZJaVVxdlVTWmc4K3RpOFhuWU96cEQrZ2YraUp6dWhqMXRtZk04a3dON2EwdzBHcUpCakpJOWdyNktmYUxWT2t2WSt1OWs3MDdiRTQvMTVmT0RacFpYTVVRM3g3U3dnUTFNaWNDOERRK21IZlp4WWVzdzI1dnlPeHpjLytVZnZLSkl2MHJOcExUckxMWlo1R1YrRFpCSU92MVhHKzZXanNsdytGYmhqa2IwTlkvS2JBYzhnVGRxU210aWNWU0lDYmttUW9VMXRERDRpTUY0M1p3UWdkc2Y4TVpPbm94Z1BYSlIxZktBaG1ZNkJyekxsN3FieXl0Y3JNZDY0cUd2QU9meGM5NmFzSU56QkVpV0h2OWRld2dqbjBPUVVFN2gzSFFrUnJJb0pwWnZGR3BNS2lHWE5WUEtMTWFaZCtHeDlvc0t2bGUrTjJUNGJnVmF6UE44UmRzTUgvL2NKMDVudUFnbFZRRnhCZklZS0RXS1lBQ2dtMTFEalBRaTJEWFBmREpHdVp5dHVsbjQrTXM1NWFvRWhQNFdURHBNei9zZHRDSHkvUkZFZ1RIZzV2c1hQVGZ2SU8zMkpFN08zNVlQazlQRGxJODNKTTNmYzVSS2thTDd3L3M4MiszV1VvYWRzMWRKMkUwUG9ZSWFodVh5ZGc2Mkd4ZVRyK2FPK3Q2clVCYzhtZGhQR2F1YlQ5S1pvaUs1VU1jRGovQTRZdkhnTVUvbUdFK2o4cEVWYS9jOUNMUXNYQkNSTXJScEc5U0MwWWxFWkN0RTVIak9oNFlKUWZPckdtYnEvLzlOUHpiQ2hiU1JSd0xUMkhBQ3I3TTlnT0Y0NW9TU3FQbFNLdHVRSkNuMElnMGcwQ3Y1WDU5YVUwUDM3N0NhbWlIZWpEd0FTM0gydlozUUZCZ1pncXJMUzZZejhlZlZuaEFyNU1pbDFZbElYc1g5cnFINjdKQktRQ1p1UnhVN2JQcWdsQXU1UXNYSTVsWmxHSnowM0VIMzNxNjA4UnlNdlN1Z2JKVDREYkZoS3QzczZ4alk0L1Y4Qmt6RHNUZWc9PSIsImtyIjoiMmNhNTFiZTgiLCJzaGFyZF9pZCI6MjU5MTg5MzU5fQ.RqCTbq1Mf6vXSRmylxf_oL2nQ4LdB8DMdcbiL50MPTo&use_stripe_sdk=true&key=pk_live_O45qBcmyO7GC7KkMKzPtpRsl&client_attribution_metadata[client_session_id]=e559e6dc-74cc-410c-9ae8-a3f36c50e11f&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=split-card-element&client_attribution_metadata[merchant_integration_version]=2017&client_secret=pi_3SkfrsBI46WJQGRa0L6E2dB6_secret_B4Wfm4YESnOsHfm9KyUeU3Fef'

response = requests.post(
    'https://api.stripe.com/v1/payment_intents/pi_3SkfrsBI46WJQGRa0L6E2dB6/confirm',
    headers=headers,
    data=data,
)

print(yummy[id])