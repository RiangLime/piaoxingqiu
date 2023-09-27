# 输入自己的token
token = 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkMFOwzAQRP9lzznYbuxsciwCgQSqVNEDp8pxNmqk2K4cpwKq_jtODagnuNmrmTe7cwav53h4cr2Hxs3jWMA8Ucj_M7TD553vCBp4eHzev0AB09yuf4dKqEojI-oER1mKClXPy7pMuuTc-nERrXdv99s0sdHsFnS3GCVjjKORirWmvL6J9bXKxv9kCJcC6P04BHodbMrgFWM1ypXApLkiNkcKOvo_MVVKM4F0_KGoWiJDiYiCp0s_pkg2X5qbsRTMQbt421Za4za_gBOFafAOGpmrdNp-Ay5fAAAA__8.Kg8Epc4JVUjp-s7Sb1xHQK5xrLHKfGaP-kB8AfFn9bAgmMOHEuY1e-yJRRDLB-03eXrc5o671pEWr69pDmLLT_8UPXMXRiLmkw2MVHrzxzmf77KHZu2mvyGoyzJE4a-kSpnqbWuaNwuyWywnBaYIX3H6iQg6xPh7ni3d01MgeFI'
# 项目id，必填
show_id = '64f4310635699900017da27a'  #jay
# show_id = '64c098ac265b940001647730'
# 指定场次id，不指定则默认从第一场开始遍历
session_id = '64f431244f487d0001994368'  # 644fcb7dca916100017dda3d   jay
#session_id = '64c098c1a8e5a6000135d542'
# 指定座位 980->1280->780->580
seat_ids = ['64fea364c24cd20001bf098b','64fea364c24cd20001bf098e','64fea364c24cd20001bf0988','64fea364c24cd20001bf0985']
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 2
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0,1]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
deliver_method = ''

