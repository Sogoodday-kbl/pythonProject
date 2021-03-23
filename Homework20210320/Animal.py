'''
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】

创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】

调用 name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】。

2、使用yaml 来管理猫猫，狗狗的属性
'''''
import yaml


class Animal:

    def __init__(self,name,color,age,sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def run(self):
        print ("我在跑")
        return

    def barked(self):
        print ("我在叫")
        return


class cat(Animal):

    hair="短毛"

    def CatchMouse(self):
        print ("捉到了老鼠")
        return

    def barked(self):
        print("喵喵叫")


class dog(Animal):

    hair = "长毛"

    def HouseKeeping(self):
        print("狗看家")
        return

    def barked(self):
        print("汪汪叫")


if __name__ == '__main__':

    with open('../Homework20210320/file.yaml',encoding='utf-8') as f :
        datas=yaml.safe_load(f)
        Dogdata=datas['dogdata']
        Catdata=datas['catdata']


    cat1=cat(name=Catdata['name'],color=Catdata['color'],age=Catdata['age'],sex=Catdata['sex'])
    print(cat1.name)
    print(cat1.color)
    print(cat1.age)
    print(cat1.sex)
    print(cat1.hair)
    print(cat1.CatchMouse())

    dog1=dog(name=Dogdata['name'],color=Dogdata['color'],age=Dogdata['age'],sex=Dogdata['sex'])
    print(dog1.name)
    print(dog1.color)
    print(dog1.age)
    print(dog1.sex)
    print(dog1.hair)
    print(dog1.HouseKeeping())
