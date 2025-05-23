# Sample programs for Python Set and Frozenset methods

# 1. frozenset()
print("1. frozenset()")
fset = frozenset([1, 2, 3, 4])
print("frozenset:", fset)
# fset.add(5) → will raise error because it's immutable

# 2. set.add()
print("\n2. set.add()")
s = {1, 2}
s.add(3)
print("After add:", s)

# 3. set.clear()
print("\n3. set.clear()")
s2 = {1, 2, 3}
s2.clear()
print("After clear:", s2)

# 4. set.copy()
print("\n4. set.copy()")
s3 = {1, 2, 3}
s_copy = s3.copy()
print("Copy of set:", s_copy)

# 5. set.difference()
print("\n5. set.difference()")
a = {1, 2, 3}
b = {2, 4}
print("Difference:", a.difference(b))

# 6. set.difference_update()
print("\n6. set.difference_update()")
a2 = {1, 2, 3}
a2.difference_update(b)
print("After difference_update:", a2)

# 7. set.discard()
print("\n7. set.discard()")
s4 = {1, 2, 3}
s4.discard(2)
s4.discard(10)  # No error
print("After discard:", s4)

# 8. set.intersection()
print("\n8. set.intersection()")
a3 = {1, 2, 3}
b3 = {2, 3, 4}
print("Intersection:", a3.intersection(b3))

# 9. set.intersection_update()
print("\n9. set.intersection_update()")
a4 = {1, 2, 3}
a4.intersection_update(b3)
print("After intersection_update:", a4)

# 10. set.isdisjoint()
print("\n10. set.isdisjoint()")
a5 = {1, 2}
b5 = {3, 4}
print("Is disjoint:", a5.isdisjoint(b5))

# 11. set.issubset()
print("\n11. set.issubset()")
a6 = {1, 2}
b6 = {1, 2, 3}
print("Is subset:", a6.issubset(b6))

# 12. set.issuperset()
print("\n12. set.issuperset()")
a7 = {1, 2, 3}
b7 = {2, 3}
print("Is superset:", a7.issuperset(b7))

# 13. set.pop()
print("\n13. set.pop()")
s5 = {1, 2, 3}
print("Pop element:", s5.pop())
print("After pop:", s5)

# 14. set.remove()
print("\n14. set.remove()")
s6 = {1, 2, 3}
s6.remove(2)
print("After remove:", s6)

# 15. set.symmetric_difference()
print("\n15. set.symmetric_difference()")
a8 = {1, 2, 3}
b8 = {3, 4, 5}
print("Symmetric difference:", a8.symmetric_difference(b8))

# 16. set.symmetric_difference_update()
print("\n16. set.symmetric_difference_update()")
a9 = {1, 2, 3}
a9.symmetric_difference_update(b8)
print("After symmetric_difference_update:", a9)

# 17. set.union()
print("\n17. set.union()")
a10 = {1, 2}
b10 = {2, 3}
print("Union:", a10.union(b10))

# 18. set.update()
print("\n18. set.update()")
a11 = {1, 2}
a11.update(b10)
print("After update:", a11)
