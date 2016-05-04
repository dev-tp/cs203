import Glibc

func bubbleSort<T: Comparable>(inout list: [T]) {
    for i in 0..<list.count - 1 {
        for j in 0..<list.count - i - 1 {
            if list[j] > list[j + 1] { // list[j].compareTo(list[j + 1]) > 0
                swap(&list[j], &list[j + 1])
            }
        }
    }
}

func insertionSort<T: Comparable>(inout list: [T]) {
    for i in 1..<list.count {
        var j: Int = i
        while j > 0 && list[j - 1] > list[j] {
            swap(&list[j], &list[j - 1])
            j -= 1
        }
    }
}

// Bottom-up mergesort
func mergeSort<T: Comparable>(inout list: [T]) {
    var sideList: [T] = list // E[] sideList = (E[]) new Comparable[list.size()];
    var i: Int = 1 // int i = 1;
    while i < list.count { // while(i < list.length())
        var j: Int = 0
        while j < list.count {
            mergeSort(&list, j, min(i + j, list.count), min(j + 2 * i, list.count), &sideList)
            j = j + 2 * i
        }
        list = sideList // System.arraycopy(sideList, 0, list, 0, list.length);
        i *= 2
    }
}

private func mergeSort<T: Comparable>(inout list: [T], _ leftIndex: Int,
    _ rightIndex: Int, _ tip: Int, inout _ sideList: [T]) {

    var i = leftIndex, j = rightIndex, k = leftIndex
    while k < tip {
        if i < rightIndex && (j >= tip || list[i] <= list[j]) {
            sideList[k] = list[i]
            i += 1
        } else {
            sideList[k] = list[j]
            j += 1
        }
        k += 1
    }
}

func heapSort<T: Comparable>(inout list: [T]) {
    var n: Int = list.count
    var k: Int = n / 2
    while k >= 1 {
        sync(&list, k, n) 
        k -= 1
    }
    while n > 1 {
        let temp = list[0]
        n -= 1
        list[0] = list[n]
        list[n] = temp
        sync(&list, 1, n)
    }
}

private func sync<T: Comparable>(inout list: [T], var _ k: Int, _ n: Int) {
    while 2 * k <= n {
        var j: Int = 2 * k
        if j < n && lessThan(list, j, j + 1) { j += 1 }
        if !lessThan(list, k, j) { break }

        let temp = list[k - 1]
        list[k - 1] = list[j - 1]
        list[j - 1] = temp
        k = j
    }
}

private func lessThan<T: Comparable>(list: [T], _ i: Int, _ j: Int) -> Bool {
    return list[i - 1] < list[j - 1]
}

func shuffle<T>(inout list: [T]) {
    srand(UInt32(time(nil)))
    for i in 0..<list.count {
        let r: Int = random() % list.count
        if r != i {
            swap(&list[i], &list[r])
        }
    }
}

func quickSort<T: Comparable>(inout list: [T]) {
    quickSort(&list, 0, list.count - 1)
}

private func quickSort<T: Comparable>(inout list: [T], _ leftIndex: Int, _ rightIndex: Int) {
    var i = leftIndex, j = rightIndex
    let pivot: T = list[(leftIndex + rightIndex) / 2]
    while i <= j {
        while list[i] < pivot { i += 1 }
        while list[j] > pivot { j -= 1 }
        if i <= j {
            if i != j { swap(&list[i], &list[j]) }
            i += 1
            j -= 1
        }

        if leftIndex < j {
            quickSort(&list, leftIndex, j)
        }

        if i < rightIndex {
            quickSort(&list, i, rightIndex)
        }
    }
}


var list = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

shuffle(&list)
print(list)

quickSort(&list) // bubbleSort, insertionSort, and mergeSort all work
print(list)