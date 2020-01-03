
courses=['Computer','Java','Php','Python']
courses.append('c++')
courses_str='-'.join(courses)
print(courses_str)

courses=['Computer','Java','Php','Python']
courses.insert(0,'c++')
print(courses)

num_1=100
num_2=200
result=[num_1+num_2,num_1-num_2,num_1/num_2,num_1*num_2]
print(result)

courses=['Computer','Java','Php','Python']
print(courses[0:2])

tuple_1=['Computer','Java','Php','Python']
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)

cs_courses=['Computer','Java','Php','Python']
art_courses=['History','Maths']
print(cs_courses.union(art_courses))
