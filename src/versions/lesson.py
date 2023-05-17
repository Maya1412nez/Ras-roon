from matplotlib import pyplot as plt 

X1, Y1 = 2, 4
X2, Y2 = 6, 1

class Graphik:
    def __init__(self) -> None:
        plt.title("Зависимость среднего качества от количества") 
        plt.xlabel("количество фигур") 
        plt.ylabel("коэфициент качества") 

    def add_value(self, x, y, color='-ro'):
        plt.plot(x, y, color)
    def show(self):
        plt.show()
        

def count_value(gra):
    list_of_x = [i / 10 for i in range((X1) * 10, X2 * 10)][1:]
    print(list_of_x)
    for x in list_of_x:
        y = f(x)
        print(x, y)
        gra.add_value(x, y)
    

def f(x):
    return (((x - X2) * (Y1 - Y2)) / (X1 - X2)) + Y2

def main():
    gra = Graphik()
    gra.add_value(X1, Y1, '-go')
    gra.add_value(X2, Y2, '-go')
    count_value(gra)


main()
plt.show()

