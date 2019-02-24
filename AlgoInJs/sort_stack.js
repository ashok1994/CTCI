const Stack = require('./stack');

class SortStack {
  constructor() {
    this.stack = new Stack();
    this.tempStack = new Stack();
  }

  push(data) {
    if (this.stack.isEmpty()) {
      this.stack.push(data);
      return;
    }
    if (this.stack.peek() >= data) {
      this.stack.push(data);
    } else {
      while (!this.stack.isEmpty()) {
        var tempItem = this.stack.pop();
        if (tempItem < data) {
          this.tempStack.push(tempItem);
        } else {
          break;
        }
      }
      this.stack.push(data);
      while (!this.tempStack.isEmpty()) {
        this.stack.push(this.tempStack.pop());
      }
    }
  }

  pop() {
    return this.stack.pop();
  }

  peek() {
    return this.stack.peek();
  }

  isEmpty() {
    return this.stack.isEmpty();
  }
}

var s = new SortStack();
s.push(0);
s.push(5);
s.push(1);
s.push(2);
console.log(s.peek());
