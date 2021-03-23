import select

def start():
    select_money=select.select_money()
    print("存款为"+str(select_money)+"元")



if __name__ == '__main__':
    start()