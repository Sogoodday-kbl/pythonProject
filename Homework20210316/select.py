#from Huogewoci import money, send
from Huogewoci.Homework20210316 import send, money


def select_money():
    saved_money = money.saved_money()
    send_money = send.send_money()
    select_money=saved_money+send_money
    print("现有存款"+str(select_money)+"元")
    return select_money

if __name__ == '__main__':
    select_money()