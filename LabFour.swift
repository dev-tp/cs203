import Glibc

func recursiveFibonacci(n: Int) -> Int {
    if n <= 1 {
        return n
    } else {
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)
    }
}

func dynamicFibonacci(n: Int) -> Int {
    var f0 = 0, f1 = 1, f2 = 1
    if n <= 0 {
        return 0
    } else if n == 1 || n == 2 {
        return 1
    }

    for _ in 3...n {
        f0 = f1
        f1 = f2
        f2 = f0 + f1
    }
    return f2
}

func getTime(n: Int) {
    var startTime = UInt32(time(nil))
    recursiveFibonacci(n)
    var endTime = UInt32(time(nil))
    print("Execution time for recursive fib(\(n)): \(endTime - startTime) sec.")

    startTime = UInt32(time(nil))
    let answer = dynamicFibonacci(n)
    endTime = UInt32(time(nil))
    print("Execution time for dynamic fib(\(n)): \(endTime - startTime) sec.")

    print("fib(\(n)): \(answer)", terminator: "\n\n")
}

var nums = [Int]()
var seconds = UInt32(time(nil))
srand(seconds)
// srandom(UInt32(NSDate().timeIntervalSince1970))
for i in 1...10 {
    nums.append(random() % 21)
}

var tree: [Int:Int] = [:]

print(nums)
for i in nums {
    tree[i] = 0
}

for i in nums {
    tree[i]! += 1 // tree[i] = tree[i]! + 1
}
print(tree)

var key = 0, highestValue = 0
for (k, v) in tree {
    if v > highestValue {
        highestValue = v
        key = k
    }
}

print("\(key) repeats \(highestValue)")

print("\n-------------------------------------\n")

for i in [10, 20, 40] {
    getTime(i)
}