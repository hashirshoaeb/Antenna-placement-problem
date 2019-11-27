# Antenna-placement-problem

In 5 antenna problem we have to place 5 antennas (a, b, c, d, e) on a 6x6 grid in such a way that maximum area is covered by their signals. To find the best solution we use Genetic Algorithm, upon a population of twenty random individuals/chromosomes.

## Chromosome:

The chromosome has 5 values, each representing the position of antenna (a,b,c,d,e) consecutively, on the grid. For example, the below chromosome shows the positions of a,b,c,d,e as shown. x is horizontal, and y is vertical. Area covered by each antenna is represented by 1. Similarly uncovered area is represented by 0.

```python
#             [x, y]
chromosome = [[5, 4], [2, 2], [3, 4], [4, 1], [1, 1]]

#     x= 1, 2, 3, 4, 5, 6
area = [[1, 1, 1, 1, 1, 0], # y = 1
        [1, 1, 1, 1, 0, 0], #     2
        [0, 1, 1, 0, 1, 0], #     3
        [0, 1, 1, 1, 1, 1], #     4
        [0, 0, 1, 0, 1, 0], #     5
        [0, 0, 0, 0, 0, 0]] #     6
```

Each antenna cover 5 blocks.

```python
antenna = [[0, 1, 0],  #  [N, N-1]
           [1, 1, 1],  #  [N-1, N] , [N, N], [N+1, N]
           [0, 1, 0]]  #  [N, N+1]
```

## Fitness evaluation:
Each antenna covers 5 blocks on a grid. One its own, and four neighbours, up, down, left and right. So fitness value is the total area covered by all 5 antennas. Example is shown above. 5 antennas cover 19 blocks, so fitness value is 19.

# Example

```python
from chromosome import chromosome
chromosome1 = chromosome()
print(chromosome1.chrom)
print(chromosome1.area)
print(chromosome1.fitnessValue)
```

```bash
[[4, 3], [6, 2], [2, 5], [5, 5], [2, 2]]
[[0 1 0 0 0 1]
 [1 1 1 1 1 1]
 [0 1 1 1 1 1]
 [0 1 0 1 1 0]
 [1 1 1 1 1 1]
 [0 1 0 0 1 0]]
24
```

```python
chromosome1.mutate()
print(chromosome1.chrom)
print(chromosome1.fitnessValue)
```
```bash
[[4, 3], [6, 2], [6, 2], [5, 5], [2, 2]]
19
```