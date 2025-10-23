from collections import deque
from typing import Any, Callable, Dict
def gen_bin_tree(height,root,left_branch: Callable[[Any], Any] = lambda x: x // 2,right_branch: Callable[[Any], Any] = lambda x: x * 2) -> Dict[str, int]:
    if height == 0:  #если высота 0 возвращаем пустое дерево
        return {}
    if height < 0:
        return "Высота дерева должна быть неотрицательна"
    tree_dict = {} #Создаем пустой словарь для дерева
    queue = deque() #будем обрабатывать узлы по порядку
    queue.append(('root', root, 1)) #корень (путь, значение, текущий уровень)
    while queue:
        path, current_value, level = queue.popleft() # Берем первый узел из начала очереди
        tree_dict[path] = current_value # Записываем узел в словарь
        if level < height:
            left_value = left_branch(current_value)  # Левый потомок
            right_value = right_branch(current_value)  # Правый потомок
            queue.append((f"{path}.left", left_value, level + 1)) #добавляем в очередь
            queue.append((f"{path}.right", right_value, level + 1))
    return tree_dict

