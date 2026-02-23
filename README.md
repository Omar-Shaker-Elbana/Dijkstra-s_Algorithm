# Dijkstra-s_Algorithm
> A clean, efficient, and production-ready implementation of Dijkstra’s Shortest Path Algorithm in Python.

---

## 📌 Overview

This project implements **Dijkstra’s Algorithm**, a fundamental graph algorithm used to compute the shortest paths from a single source node to all other nodes in a weighted graph with non-negative edge weights.

It is designed to be:
- Educational
- Efficient
- Clean and readable
- Easy to extend

---

##  What is Dijkstra’s Algorithm?

Dijkstra’s Algorithm solves the **single-source shortest path problem** for weighted graphs where all edge weights are non-negative.

### How It Works

1. Initialize all node distances to infinity.
2. Set the source node distance to 0.
3. Use a priority queue (min-heap) to repeatedly:
   - Extract the node with the smallest tentative distance.
   - Update (relax) its neighbors.
4. Continue until all nodes are processed.

### ⏱ Time Complexity

- Using a binary heap:
  
  O((V + E) log V)

Where:
- V = number of vertices
- E = number of edges

---

## 🛠️ Tech Stack

- Python 3.x
- `heapq` (priority queue)
- Dictionary-based adjacency list representation

---

## 📂 Project Structure

```bash
.
├── dijkstra.py
├── main.py
└── README.md
└── graph.py
└── testing.py
└── example.jpg
```
---

## ▶️ How to Run

```bash
git clone https://github.com/Omar-Shaker-Elbana/Dijkstra-s_Algorithm/
cd Dijkstra-s_Algorithm
python main.py
```

---

## 🧪 Example Usage

```python
from dijkstra import dijkstra

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3},
    'D': {}
}

distances = dijkstra(graph, 'A')
print(distances)
```

### Output

```
{'A': 0, 'B': 1, 'C': 3, 'D': 6}
```

---

## 🧩 Features

- ✅ Efficient priority queue implementation
- ✅ Clean adjacency list structure
- ✅ Supports directed and undirected graphs
- ✅ Easy to extend for path reconstruction

---

## 📈 Future Improvements

- Add shortest path reconstruction
- Add graph visualization
- Add performance benchmarking
- Add unit tests (pytest)
- Support large-scale random graph testing

---

## 🎯 Why This Project?

This implementation was built to:

- Strengthen understanding of graph theory
- Practice algorithm optimization
- Improve clean code structuring
- Serve as a reusable reference implementation

---

## 📚 References

- *Introduction to Algorithms (CLRS)*
- MIT OpenCourseWare
- GeeksForGeeks

---

## 👨‍💻 Author

Omar Shaker 
🔗 **GitHub:** [Omar-Shaker-Elbana](https://github.com/Omar-Shaker-Elbana)
Computer Science Enthusiast | Algorithm Explorer

If you found this helpful, consider ⭐ starring the repository!
