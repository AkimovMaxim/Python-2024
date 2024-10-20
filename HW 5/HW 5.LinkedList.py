Реализуйте класс связного списка `LinkedList`. 
(Вам потребуется реализовать вспомогательный класс `Node`,
содержащий в себе ссылки на соседей, и свое значение. Тогда
сам список содержит в себе лишь ссылку на первую вершину,
и вспомогательные данные вроде текущей длины). Список 
должен поддерживать обращение по индексам, красиво печататься,
выдавать длину через `len()` и иметь работающие методы
`.pop()`, `.append()`. Также список должен поддерживать
итерацию по нему. *Можете также добавить `.insert()` и 
`.pop()` по индексу.
#Класс: узел
class Node:
    #Узел имеет два параметра: значение и ссылка на следующий узел
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    #Вывод узла
    def __repr__(self):
        return f"Node({self.value})"

#Класс: односвязный список
class LinkedList:
    def __init__(self):
        self.head = None  
        self.length = 0   

    #Вывод длины списка
    def __len__(self):
        return self.length

    #Итерация по списку
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next_node
            
    #Обращение по индексу
    def __getitem__(self, index):
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next_node
        return current.value

    #Вывод списка
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current.value))
            current = current.next_node
        return " -> ".join(nodes)

    #Добавляет элемент в конец списка
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self.length += 1

    #Удаляет элемент и возвращает его значение
    def pop(self, index=None):
        if self.length == 0:
            raise IndexError("List is empty")
        
        if index is None:
            index = self.length - 1

        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        
        if index == 0:
            value = self.head.value
            self.head = self.head.next_node
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next_node
            value = prev.next_node.value
            prev.next_node = prev.next_node.next_node
        
        self.length -= 1
        return value

    #Вставка по индексу
    def insert(self, index, value):
        if not 0 <= index <= self.length:
            raise IndexError("Index out of range")

        new_node = Node(value)

        if index == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next_node
            new_node.next_node = prev.next_node
            prev.next_node = new_node

        self.length += 1

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll)  # 1 -> 2 -> 3

print(len(ll))  # 3

print(ll[1])  # 2

ll.insert(1, 5)
print(ll)  # 1 -> 5 -> 2 -> 3

ll.pop(1)
print(ll)  # 1 -> 2 -> 3

for item in ll:
    print(item)  # 1, 2, 3 
