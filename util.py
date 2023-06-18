import numpy as np
def eliminar_repetidos(arr1, arr2):
    arr_copy = arr2.copy()
    for element in arr1:
        arr_copy.remove(element)

arr1 = np.array([1,2,3])
arr2 = np.array([1,2])
print(eliminar_repetidos(arr1, arr2))