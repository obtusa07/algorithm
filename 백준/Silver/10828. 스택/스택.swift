import Foundation

struct Stack {
    private var stack: [Int] = []
    
    public mutating func push(_ element: Int) {
        stack.append(element)
    }
    
    /// need print
    public mutating func pop() -> Int? {
        return isEmpty ? nil : stack.popLast()
    }
    
    public var size: Int {
        return stack.count
    }
    
    public var isEmpty: Bool {
        return stack.isEmpty
    }
    
    /// need print
    public var top: Int {
        return isEmpty ? -1 : stack.last!
    }
}

let count = Int(readLine()!)!
var myStack = Stack()

for _ in 0 ..< count {
    let input = readLine()!.split(separator: " ")
    
    switch input[0] {
    case "push":
        myStack.push(Int(input[1])!)
    case "pop":
        let stack = myStack.pop()
        if stack == nil {
            print("-1")
            
        } else {
            print(stack!)
        }
    case "size":
        print(myStack.size)
    case "empty":
        myStack.isEmpty ? print("1") : print("0")
    case "top":
        print(myStack.top)
    default:
        continue
    }
}