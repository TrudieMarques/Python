# office = ["stapler", "files", "monitor", "pens"]

# print(office)

# print(office[0].title())
# print(office[1].title())
# print(office[2].title())
# print(office[3].title())

# print(office[-1])

# message = f"We only use black {office[-1]} in our office"
# print(message)

# office[0] = "hole punch"
# print(office)

# office.append("stapler")
# print(office)

# office.insert(1, "ruler")
# print(office)

# del office[3]
# print(office)

# # popped_office = office.pop()
# # print(office)
# # print(popped_office)
# least_useful = office.pop()
# print(f"The least useful office tool is a {least_useful}")

# popped_item = office.pop(1)
# # print(office)
# # print(popped_item)
# print(f"I need one more {popped_item} for my desk")

# print(office)

# # office.remove("files")
# # print(office)

# paper = "files"
# office.remove(paper)
# print(office)
# print(f"\n{paper.title()} are no longer needed in an office.")

# print(office)

# office.append("scissors")
# office.append("mouse")

# print(office)

# office.sort()
# print(office)

# office.sort(reverse=True)
# print(office)

office2 = ['hole punch', 'pens', 'scissors', 'mouse']
print("Here is the original list:")
print(office2)
print("\nHere is the sorted list:")
print(sorted(office2))
print("\nHere is the orignal list agian:")
print(office2)

office2.reverse()
print(office2)

print(len(office2))
