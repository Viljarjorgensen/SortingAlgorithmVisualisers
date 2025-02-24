import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            yield arr, smallest, i, j
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
        yield arr, smallest, i, j

array = [random.randint(1, 100) for _ in range(20)]

fig, ax = plt.subplots()
ax.set_title("Selection Sort Visualization")

bars = ax.bar(range(len(array)), array, color='skyblue')

def update(arr_data):
    arr, smallest, start, current_compare = arr_data
    for bar, val in zip(bars, arr):
        bar.set_height(val)
        bar.set_color('skyblue')

    bars[smallest].set_color('green')  # Highlight the smallest element in red

    bars[current_compare].set_color('blue')   # Highlight the bar being compared in yellow

    return bars

anim = animation.FuncAnimation(
    fig, update, frames=selection_sort(array), interval=200, repeat=False
)

plt.show()
