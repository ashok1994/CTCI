// from StacksAndQueues.Exceptions import EmptyStackError

class StackNode {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
  }

  push(data) {
    var node = new StackNode(data);
    node.next = this.top;
    this.top = node;
  }

  pop() {
    if (this.top === null) {
      throw new Error('Empty stack');
    } else {
      var data = this.top.data;
      this.top = this.top.next;
      return data;
    }
  }

  peek() {
    if (this.top === null) {
      throw new Error('Empty stack');
    } else {
      return this.top.data;
    }
  }

  isEmpty() {
    return this.top === null;
  }
}

module.exports = Stack;
