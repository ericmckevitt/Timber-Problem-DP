# Timber Problem Dynamic Programming Solution
### By Eric McKevitt

---

## Recurrence Relation:

$$
T(i, j) = \max \biggl( l_i + \min \Bigr[ T(i+2, j), T(i+1, j - 1) \Bigr], l_j + \min \Bigl[ T(i+1, j - 1), T(i, j-2)\Bigl] \biggl)
$$
$$
\text{Base Cases: }
\begin{cases}
    T(i, j) = l_i \hspace{1.84cm} j = i \\
    T(i, j) = \max (l_i, l_j) \hspace{0.5cm} j = i + 1
\end{cases}
$$