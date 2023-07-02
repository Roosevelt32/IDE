import numpy as np
# создаем четкий порядок чтоб функция работала 
np.random.seed(1)
random_array = np.random.randint(1,101, size=(1000))
# создаем список 
count = []
# создаем функцию по типу лесинки        
def score(number, step=12):
    #создаем счетчик попыток
    count = 0
    # создаем число от которого будем оттталкиваться 
    predict = 0
    while number != predict:
        # если число не совпадает , прибавляем 1 попытку 
        count+=1
        # создаем алгоритм подбора числа 
        if number > predict:
            predict+=step
        else:
            predict-=1
    return count

for number in random_array:
    count.append(score(number))

print(random_array[0:10])
# берем среднее значение
print(count[0:10])
print(np.mean(count))
