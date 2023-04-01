# Timber Problem Dynamic Programming Solution
### By Eric McKevitt

---

## Recurrence Relation:

$$
T(i, j) = \max ( l_i + \min [ T(i+2, j), T(i+1, j - 1) ], l_j + \min (T(i+1, j - 1), T(i, j-2)))
$$