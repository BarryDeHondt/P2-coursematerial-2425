# sort_by_age(people) orders the Persons by increasing age.
# sort_by_decreasing_age(people) orders the Persons by decreasing age.
# sort_by_name(people) orders the Persons by name, alphabetically.
# sort_by_name_then_age(people) orders the Persons by name, and in case of equal names, by increasing age
# sort_by_name_then_decreasing_age(people) orders the Persons by name, and in case of equal names, by decreasing age


sort_by_age = lambda people : sorted(people, key=lambda person: person.age)