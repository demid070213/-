points = 0
question1 = input("корень 49=")
if question1 == "7":
    print("правильно")
    points = points + 1
else :
    print("неправильно")
    points = points + 0
question2 = input("4 в 5 степени=")
if question2 == "1024":
    print("правильно")
    points = points + 1
else :
    print("неправильно")
    points = points + 0
question3 = input("24 умножить на 18=")
if question3 == "432":
    print("правильно")
    points = points + 1
else :
    print("неправильно")
    points = points + 0
question4 = input("у Пети было 20 батончиков сникерс,12 с половиной он съел.Сколько у него осталось батончиков?")
if question4 == "7,5":
    print("правильно")
    points = points + 1
else :
    print("неправильно")
    points = points + 0
question5 = input("(213,1-189,6)*78,2-693,14=")
if question5 == "1144,56":
    print("правильно")
    points = points + 1
else :
    print("неправильно")
    points = points + 0
print(question1)
print("-----------------")
print(question2)
print("-----------------")
print(question3)
print("-----------------")
print(question4)
print("-----------------")
print(question5)
print("-----------------")
print(f"вы набрали,{points},баллов")
if points == 5:
    print("это отлично")
if points == 4:
    print("это хорошо")
if points == 3:
    print("это не очень")
if points == 2:
    print("это плохо")
if points == 1:
    print("это ужасно")
if points == 0:
    print("это отвратительно")
