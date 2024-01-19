# 输入自己的token
token = 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkEFvwjAMhf-Lzz3EbtIWjqBNIIEmoXHYCYXUiEptgtJ0giH--1IF0E7j6Kf3-fn5Ck4P4bi0BwdTO7RtBkPPPs1X2Dc_c1czTOF9sdqtIYN-2M-eYkFFqSvBXBNWSlJZFQeUExl9kdy4djTNtl9vm6h0wWzH1fUIKj3hOkcyRkgSQiCjRIUJfGXL4ZYBn0-N58-m48fhkfw4sdfB_UtTDDGedbjDWApV5AoJlZSx4KUP3KWCaW_H3hy1DX-fFNPvpKScMINv9n3jbBTTB61-HHb7BQAA__8.SpUNK_uarPZkuhaqH5Yr3E1q9HOD5vpdBbg5Yh69VdZhYtEbWwVnJSCEr8YpiljTgNYfHzF1m_gpc--0BqDAa33PMOZkpD0A8PS-IiLac46AxDGw5aLuh_3989JVmHipVxFB8w-Cmq2oM0xPYQz8x0fN-ZVjbnnqSy5aoFgOMSs'

# 项目id，必填  showId
show_id = '65a4de4260a4790001cecd87'
# 指定场次id，不指定则默认从第一场开始遍历 bizShowSessionId
session_id = '65a4de50d6b3880001ab7484'

# 指定座位 seatPlanId
seat_id = '65a4e262455ed9000161d19b'
seat_price = 480
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 1
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
deliver_method = ''
