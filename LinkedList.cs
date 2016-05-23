using System;
using System.Text;

public class Node<T>
{
    public Node(T data)
    {
        this.data = data;
    }

    public T Data
    {
        get { return this.data; }
        set { this.data = value; }
    }

    public Node<T> Next
    {
        get { return this.next; }
        set { this.next = value; }        
    }

    public override string ToString()
    {
        return this.data.ToString();
    }

    private T data;
    private Node<T> next;
}

public class LinkedList<T> // where T : class
{
    public int Size
    {
        get { return this.size; }
    }

    public void AddFirst(T element)
    {
        Node<T> node = new Node<T>(element);
        node.Next = this.head;
        this.head = node;
        this.size++;

        if (this.tail == null)
            this.tail = this.head;
    }

    public void AddLast(T element)
    {
        Node<T> node = new Node<T>(element);
        if (this.tail == null) {
            this.head = this.tail = node;
            this.size++;
        }
        else {
            this.tail.Next = node;
            this.tail = this.tail.Next;
            this.size++;
        }
    }

    public void Add(int index, T element)
    {
        if (index == 0) {
            this.AddFirst(element);
        }
        else if (index >= size) {
            this.AddLast(element);
        }
        else {
            Node<T> currentNode = this.head;

            for (int i = 1; i < index; i++)
                currentNode = currentNode.Next;

            Node<T> temp = currentNode.Next;
            currentNode.Next = new Node<T>(element);
            (currentNode.Next).Next = temp;
            this.size++;
        }
    }

    public void Add(T element)
    {
        this.Add(this.size, element);
    }

    public T RemoveFirst()
    {
        if (this.size == 0) {
            return default(T); // null
        }
        else {
            Node<T> temp = this.head;
            this.head = this.head.Next;
            this.size--;
            if (this.head == null)
                this.tail = null;
            return temp.Data;
        }
    }

    public T RemoveLast()
    {
        if (this.size == 0) {
            return default(T);
        }
        else if (this.size == 1) {
            Node<T> temp = this.head;
            this.head = this.tail = null;
            this.size = 0;
            return temp.Data;
        }
        else {
            Node<T> currentNode = this.head;

            for (int i = 0; i < this.size - 2; i++)
                currentNode = currentNode.Next;

            Node<T> temp = this.tail;
            this.tail = currentNode;
            this.tail.Next = null;
            this.size--;
            return temp.Data;
        }
    }

    public T Remove(int index)
    {
        if (index == 0) {
            return this.RemoveFirst();
        }
        else if (index >= size) {
            return this.RemoveLast();
        }
        else {
            Node<T> currentNode = this.head;

            for (int i = 1; i < index; i++)
                currentNode = currentNode.Next;

            Node<T> temp = currentNode.Next;
            currentNode.Next = (currentNode.Next).Next;
            this.size--;
            return temp.Data;
        }
    }

    // TODO Implement
    public T Remove(T element)
    {
        return default(T);
    }

    public override string ToString()
    {
        StringBuilder sb = new StringBuilder();
        Node<T> currentNode = this.head;
        while (currentNode != null) {
            sb.Append(currentNode + " ");
            currentNode = currentNode.Next;
        }
        return sb.ToString();
    }

    private Node<T> head, tail;
    private int size;
}

public class Test
{
    public static void Main(string[] args)
    {
        LinkedList<int> ints = new LinkedList<int>();
        ints.Add(1);
        ints.Add(2);
        ints.Add(3);
        ints.Add(1, 4);
        ints.AddFirst(5);
        ints.AddLast(6);
        Console.WriteLine(ints);
        Console.WriteLine("Current size: {0}", ints.Size);

        ints.RemoveFirst();
        Console.WriteLine(ints);
        Console.WriteLine("Current size: {0}", ints.Size);
        ints.RemoveLast();
        Console.WriteLine(ints);
        Console.WriteLine("Current size: {0}", ints.Size);
        Console.WriteLine("Removed: {0}", ints.Remove(1));
        Console.WriteLine(ints);
        Console.WriteLine("Current size: {0}", ints.Size);
    }
}