print("--------Student report card management system--------")
reportcards={"s1":{"name":"haritha",
                    "dept":"cse",
                    "marks":{"maths":94,"english":86,"python":92}},
             "s2":{"name":"kiran",
                    "dept":"ai",
                    "marks":{"maths":93,"english":76,"python":82}},
             "s3":{"name":"chandu",
                    "dept":"ece",
                    "marks":{"maths":84,"english":66,"python":96}},
             "s4":{"name":"joshvik",
                    "dept":"IT",
                    "marks":{"maths":74,"english":56,"python":93}},
             "s5":{"name":"gaayi",
                    "dept":"eee",
                    "marks":{"maths":91,"english":88,"python":90}}
             }
total1=reportcards["s1"]["marks"]["maths"]+reportcards["s1"]["marks"]["english"]+reportcards["s1"]["marks"]["python"]
print("total marks of student1:",total1)
print("percentage of student1:",total1/3)
total2=reportcards["s2"]["marks"]["maths"]+reportcards["s2"]["marks"]["english"]+reportcards["s2"]["marks"]["python"]
print("total marks of student2:",total2)
print("percentage of student1:",total2/3)
total3=reportcards["s3"]["marks"]["maths"]+reportcards["s3"]["marks"]["english"]+reportcards["s3"]["marks"]["python"]
print("total marks of student3:",total3)
print("percentage of student3:",total3/3)
total4=reportcards["s4"]["marks"]["maths"]+reportcards["s4"]["marks"]["english"]+reportcards["s4"]["marks"]["python"]
print("total marks of student4:",total4)
print("percentage of student4:",total4/3)
total5=reportcards["s5"]["marks"]["maths"]+reportcards["s5"]["marks"]["english"]+reportcards["s5"]["marks"]["python"]
print("total marks of student5:",total5)
print("percentage of student5:",total5/3)
print("---student Details----")
print(reportcards)
reportcards.update({"s1":{"name":"jaanu"}})
print(reportcards)



