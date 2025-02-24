import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        yield arr, key, i, j


array = [random.randint(1, 100) for _ in range(20)]

fig, ax = plt.subplots()
ax.set_title("Insertion Sort Visualization")

bars = ax.bar(range(len(array)), array, color='skyblue')


def update(arr_data):
    arr, key, i, j = arr_data

    for bar, val in zip(bars, arr):
        bar.set_height(val)
        bar.set_color('skyblue')

    bars[i].set_color('green')

    if j >= 0:
        bars[j].set_color('blue')

    return bars


anim = animation.FuncAnimation(
    fig, update, frames=insertion_sort(array), interval=200, repeat=False
)

plt.show()
