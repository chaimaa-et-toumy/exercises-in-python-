from Classes_Inheritance import Doctor

from Classes_Inheritance import Doctor

class FamilyDoctor(Doctor):

    def what_specialization(self):
        print("i work with families")

    def paid_by_who(self):
        print("i get paid by the people")


d1 = FamilyDoctor()
d1.studied()
d1.Works_where()
d1.paid_by_who()
d1.what_specialization()
