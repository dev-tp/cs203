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

    public void AddAll(params T[] elements)
    {
        foreach (var element in elements)
            this.Add(element);
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

    public void Clear()
    {
        this.head = null;
        this.tail = null;
        this.size = 0;
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

    public T Remove(T element)
    {
        if (this.head.Data.Equals(element))
            return this.RemoveFirst();

        if (this.tail.Data.Equals(element))
            return this.RemoveLast();

        Node<T> currentNode = this.head;
        while (currentNode.Next != null && !currentNode.Next.Data.Equals(element)) {
            currentNode = currentNode.Next;
            if (currentNode.Next == null)
                return default(T);
        }

        Node<T> temp = currentNode.Next;
        currentNode.Next = (currentNode.Next).Next;
        this.size--;
        return temp.Data;
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
        LinkedList<string> abc = new LinkedList<string>();
        abc.AddAll("a", "b", "c");
        abc.Add(1, "d");
        abc.AddFirst("e");
        abc.AddLast("f");
        Console.WriteLine("{0}\nCurrent size: {1}", abc, abc.Size);

        abc.RemoveFirst();
        Console.WriteLine("{0}\nCurrent size: {1}", abc, abc.Size);
        abc.RemoveLast();
        Console.WriteLine("{0}\nCurrent size: {1}", abc, abc.Size);
        Console.WriteLine("Removed: {0}", abc.Remove(1));
        Console.WriteLine("{0}\nCurrent size: {1}", abc, abc.Size);
        
        abc.AddAll("h", "h", "g");
        Console.WriteLine("{0}\nCurrent size: {1}", abc, abc.Size);

        Console.WriteLine("Removed: {0}", abc.Remove("h"));
        Console.WriteLine(abc.Remove("z")); // Should return null
        Console.WriteLine("{0}\nCurrent size: {1}", abc, abc.Size);
    }
}