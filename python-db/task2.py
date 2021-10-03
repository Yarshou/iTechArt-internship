from sqlalchemy import create_engine, select, update, delete, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import literal
from models import *


class SQLManager:

    def __init__(self, dbname, user, password, host='localhost'):
        self.engine = create_engine(f'postgresql://{user}:{password}@{host}/{dbname}')
        Session = sessionmaker(bind=self.engine)
        Session.configure(bind=self.engine)
        self.session = Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def insert_data(self):
        self.session.add_all([
            Shop(name='Auchan', address=None, staff_amount=250),
            Shop(name='IKEA', address='Street Žirnių g. 56, Vilnius, Lithuania.', staff_amount=500)
        ])
        self.session.commit()
        self.session.add_all([
            Department(sphere='Furniture', staff_amount=250, shop_id=1),
            Department(sphere='Furniture', staff_amount=300, shop_id=2),
            Department(sphere='Dishes', staff_amount=200, shop_id=2)
        ])
        self.session.commit()
        self.session.add_all([
            Item(name='Table', description='Cheap wooden table', price=300, department_id=1),
            Item(name='Table', description=None, price=750, department_id=2),
            Item(name='Bed', description='Amazing wooden bed', price=1200, department_id=2),
            Item(name='Cup', description=None, price=10, department_id=3),
            Item(name='Plate', description='Glass plate', price=20, department_id=3)
        ])
        self.session.commit()

    def select_data(self, num: float):
        if num == 3.1:
            result = self.session.execute(select(Item).where(Item.description != None))
            for i in result.scalars():
                print(i.name)
        if num == 3.2:
            result = self.session.query(Department.sphere).distinct().filter(Department.staff_amount > 200)
            for i in result:
                print(i[0])
        if num == 3.3:
            result = self.session.query(Shop.address).filter(Shop.name.ilike('i%'))
            for i in result:
                print(i[0])
        if num == 3.4:
            result = self.session.query(Item.name).distinct().join(Department).where(Department.sphere == 'Furniture')
            for i in result:
                print(i[0])
        if num == 3.5:
            result = self.session.query(Shop.name).distinct().join(Department).join(Item).where(
                Item.description != None
            )
            for i in result:
                print(i[0])
        if num == 3.6:
            result = self.session.execute(
                select([Item.name, Item.description, Item.price, Department.sphere.label('department_sphere'),
                        Department.staff_amount.label('department_staff_amount'), Shop.name.label('shop_name'),
                        Shop.address.label('shop_address'), Shop.staff_amount.label('shop_staff_amount'),
                        ]).join(Department, Department.id == Item.department_id).
                    join(Shop, Department.shop_id == Shop.id)
            )
            for i in result:
                print(i)
        if num == 3.7:
            result = self.session.execute(select(Item).limit(4).offset(3))
            for i in result.scalars():
                print(i.id)
        if num == 3.8:
            result = self.session.execute(
                select([Item.name, Department.sphere]).join(Department, Department.id == Item.department_id))
            for i in result.scalars():
                print(i)
        if num == 3.9:
            result = self.session.execute(
                select([Item.name, Department.sphere]).join(Department, Department.id == Item.department_id,
                                                            isouter=True))
            for i in result.scalars():
                print(i)
        if num == 3.10:
            result = self.session.execute(
                select([Item.name, Department.sphere]).join(Item, Department.id == Item.department_id,
                                                            isouter=True))
            for i in result.scalars():
                print(i)
        if num == 3.11:
            result = self.session.execute(
                select([Item.name, Department.sphere]).join(Department, Department.id == Item.department_id,
                                                            isouter=True).union(
                    select([Item.name, Department.sphere]).join(Item, Department.id == Item.department_id,
                                                                isouter=True)))
            for i in result.scalars():
                print(i)
        if num == 3.12:
            result = self.session.query(Item, Department).join(Department, literal(True)).all()
            for i in result:
                print(i)

    def update_data(self):
        result = self.session.query(Shop.address).filter(Shop.name.ilike('i%'))
        self.session.query(Item).filter(
            Item.name.ilike('b%') | Item.name.ilike('%e')).update({'price': Item.price + 100})

    def delete_data(self, num: float):
        if num == 5.1:
            self.session.execute(delete(Item).where((Item.price > 500) & (Item.description == None)))
            self.session.commit()
        if num == 5.2:
            self.session.execute(delete(Item).where(
                any(Item.id == val for val in self.session.execute(select(Item.id).join(
                    Department, Department.id == Item.department_id).join(
                    Shop, Shop.id == Department.shop_id).where(Shop.address == None)).scalars())))
            self.session.commit()
        if num == 5.3:
            self.session.execute(delete(Item).where(Item.id in self.session.execute(select(Department.id).where(
                or_(Department.staff_amount < 225, Department.staff_amount > 275))).scalars()))
        if num == 5.4:
            self.session.query(Item).delete()
            self.session.commit()
            self.session.query(Department).delete()
            self.session.commit()
            self.session.query(Shop).delete()
            self.session.commit()

    def drop_tables(self):
        Base.metadata.drop_all(bind=self.engine)


instance = SQLManager('', '', '')
instance.create_tables()
instance.insert_data()
instance.select_data(3.5)
instance.update_data()
# instance.delete_data(5.1)
instance.drop_tables()
