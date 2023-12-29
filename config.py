# 输入自己的token
token = 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkEFPAyEUhP_LO-_hQVmW7bGmRhONSWMPngzLvk03WaAB1qhN_7tsMdqT3mAy8w3MCbye0-HeDR7Wbp6mCuZIodxP0I2fN74nWMPt3cPrI1QQ527zI0ouG62QqOdM1YI3Sg5MtCL7cnLnp8W02b9sd1mxyewXdL8Ea0RkytQSOyMuZ8KhlSX4n03BuQJ6P46BnkebO1iDLTIu68VzQTwdKejk_8Q0uc0E0umXslICleArlSnxIyay5adlGUvBHLRL12vlZ1z3V_BGIY7eZZGVLZ2234TzFwAAAP__.K8MdvFsXzP3i5V8dRUO-4hMXhV8XCV32rF6ORRzDu95aNWctdWZQa0-rb6yiP7iGSaQ5l4bvHnAWYrkfHfGm3fV8PcKx0tTkR5IA_sGDt6Y9NGZi3ohvtdl0OlrY-yT3XbcnliBic5wXdHkmQ_0oN6iVJu6SKYiwWgwK4fNwupE'


# 项目id，必填
show_id = '6559fb4957a50200013819c7'
# 指定场次id，不指定则默认从第一场开始遍历

session_id = '6559fb7957a5020001381e3e'

# 指定座位
seat_id = '656d8ed29c2ae5000134a859'
seat_price = 380
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 1
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
deliver_method = ''
