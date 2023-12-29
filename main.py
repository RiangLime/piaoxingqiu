import threading
import time
from concurrent.futures import thread

import request
import config
import _thread

'''
目前仅支持【无需选座】的项目
'''
show_id = config.show_id
session_id = config.session_id
buy_count = config.buy_count
audience_idx = config.audience_idx
deliver_method = config.deliver_method
seat_id = config.seat_id
seat_price = config.seat_price
session_id_exclude = []  # 被排除掉的场次
price = 0

success = 0
targetSeatFail = 0


def runThread():
    global session_id, success
    global seat_plan_id
    global show_id
    global buy_count
    global audience_idx
    global deliver_method
    global seat_id
    global seat_price
    global session_id_exclude
    global price
    global targetSeatFail
    while True:
        if success == 1:
            print("抢到票啦 债见")
            break
        try:
            # 如果没有指定场次，则默认从第一场开始刷
            if not session_id:
                # 如果项目不是在售状态就一直刷，直到变成在售状态拿到场次id，如果有多场，默认拿第一场
                while True:
                    sessions = request.get_sessions(show_id)
                    if sessions:
                        for i in sessions:
                            if i["sessionStatus"] == 'ON_SALE' and i["bizShowSessionId"] not in session_id_exclude:
                                session_id = i["bizShowSessionId"]
                                print("session_id:" + session_id)
                                break
                        if session_id:
                            break
                        else:
                            print("未获取到在售状态且符合购票数量需求的session_id")
                            session_id_exclude = []  # 再给自己一次机会，万一被排除掉的场次又放票了呢
            # 获取座位余票信息，默认从最低价开始
            seat_plans = request.get_seat_plans(show_id, session_id)
            seat_count = request.get_seat_count(show_id, session_id)

            print("余票信息")
            print(seat_count)

            seat_plan_id = ''
            for i in seat_count:
                # 如果指定座位还没卖完 就抢指定座位
                if targetSeatFail == 0:
                    # 只抢指定座位
                    if i["seatPlanId"] == seat_id:
                        if i["canBuyCount"] >= buy_count:
                            seat_plan_id = i["seatPlanId"]
                            for j in seat_plans:
                                if j["seatPlanId"] == seat_plan_id:
                                    price = j["originalPrice"]  # 门票单价
                                    break
                            break
                        else:
                            targetSeatFail = 1
                            print("您要的座位卖完啦...将为您购买其余座位\n")
                else:
                    if i["canBuyCount"] >= buy_count:
                        seat_plan_id = i["seatPlanId"]
                        for j in seat_plans:
                            if j["seatPlanId"] == seat_plan_id:
                                price = j["originalPrice"]  # 门票单价
                                break
                        break


            # 如果没有拿到seat_plan_id，说明该场次所有座位的余票都不满足购票数量需求，就重新开始刷下一场次
            if not seat_plan_id:
                print("该场次" + session_id + "没有符合条件的座位，将为你继续搜寻其他在售场次")
                # session_id_exclude.append(session_id)  # 排除掉这个场次
                # session_id = ''
                continue


            if not deliver_method:
                deliver_method = request.get_deliver_method(show_id, session_id, seat_plan_id, price, buy_count)
            print("deliver_method:" + deliver_method)

            if deliver_method == "VENUE_E":
                request.create_order(show_id, session_id, seat_plan_id, price, buy_count, deliver_method, 0, None,
                                     None, None, None, None, [])
            else:
                # 获取观演人信息
                audiences = request.get_audiences()
                if len(audience_idx) == 0:
                    audience_idx = range(buy_count)
                audience_ids = [audiences[i]["id"] for i in audience_idx]

                if deliver_method == "EXPRESS":
                    # 获取默认收货地址
                    address = request.get_address()
                    address_id = address["addressId"]  # 地址id
                    location_city_id = address["locationId"]  # 460102
                    receiver = address["username"]  # 收件人
                    cellphone = address["cellphone"]  # 电话
                    detail_address = address["detailAddress"]  # 详细地址

                    # 获取快递费用
                    express_fee = request.get_express_fee(show_id, session_id, seat_plan_id, price, buy_count,
                                                          location_city_id)

                    # 下单
                    request.create_order(show_id, session_id, seat_plan_id, price, buy_count, deliver_method,
                                         express_fee["priceItemVal"], receiver,
                                         cellphone, address_id, detail_address, location_city_id, audience_ids)
                elif deliver_method == "VENUE" or deliver_method == "E_TICKET" or deliver_method == "ID_CARD":
                    request.create_order(show_id, session_id, seat_plan_id, price, buy_count, deliver_method, 0, None,
                                         None, None, None, None, audience_ids)
                else:
                    print("不支持的deliver_method:" + deliver_method)
            success = 1
            break
        except Exception as e:
            print(e)
            # session_id_exclude.append(session_id)  # 排除掉这个场次
            # session_id = ''
exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        runThread()


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print
        "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


# 创建两个线程
# 创建新线程
thread1 = myThread(11, "Thread-11", 1)
thread2 = myThread(12, "Thread-12", 2)
thread3 = myThread(13, "Thread-13", 3)
thread4 = myThread(14, "Thread-14", 4)
thread5 = myThread(15, "Thread-15", 5)
thread6 = myThread(16, "Thread-16", 6)
thread7 = myThread(17, "Thread-17", 7)
thread8 = myThread(18, "Thread-18", 8)
thread9 = myThread(19, "Thread-19", 9)
thread0 = myThread(10, "Thread-10", 10)


# 开启线程
thread1.start()
thread2.start()
thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()
# thread9.start()
# thread0.start()
