from sqlalchemy.orm import relationship, declared_attr

from app.database import Base
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Float, Text, Boolean


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

    products = relationship('Product', back_populates='category')

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)

    products = relationship('Product', back_populates='brand')

class BaseTablesForProduct(Base):
    __abstract__ = True
    back_populates: str = None
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, unique=True, nullable=False)
    count = Column(Integer, default=0, nullable=False)

    @declared_attr
    def products(cls):
        return relationship('Product', back_populates=f"{cls.back_populates}")

class Manufacturer(BaseTablesForProduct):
    __tablename__ = 'manufacturers'
    back_populates = 'manufacturer'

class SteelType(BaseTablesForProduct):
    __tablename__ = 'steel_types'
    back_populates = 'steel_type'

class HandleMaterial(BaseTablesForProduct):
    __tablename__ = 'handle_materials'
    back_populates = 'handle_material'

class GuardAndPommel(BaseTablesForProduct):
    __tablename__ = 'guards_and_pommels'
    back_populates = 'guard_and_pommel'

class ProductImage(Base):
    __tablename__ = "product_images"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    img_url = Column(String, nullable=False)
    product = relationship("Product", back_populates="images")

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    in_stock = Column(Integer, default=0, nullable=False)  # Поле для хранения доступного количества товара

    product = relationship("Product", back_populates="inventory", foreign_keys=[product_id])


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'), nullable=False)
    brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)
    steel_type_id = Column(Integer, ForeignKey('steel_types.id'), nullable=False)
    handle_material_id = Column(Integer, ForeignKey('handle_materials.id'), nullable=False)
    guard_and_pommel_id = Column(Integer, ForeignKey('guards_and_pommels.id'), nullable=False)

    price = Column(DECIMAL(precision=10, scale=2), nullable=False)
    total_length = Column(Float, nullable=False)
    blade_length = Column(Float, nullable=False)
    blade_width = Column(Float, nullable=False)
    gilding_blade = Column(Boolean, nullable=False, default=False)
    gilding_drawling = Column(Boolean, nullable=False, default=False)
    rating = Column(Float, default=0, nullable=False)
    model_number = Column(String, nullable=False)
    series = Column(String, nullable=False)
    main_img_url = Column(String, nullable=False)

    category = relationship('Category', back_populates='products')
    manufacturer = relationship('Manufacturer', back_populates='products')
    brand = relationship('Brand', back_populates='products')
    steel_type = relationship('SteelType', back_populates='products')
    handle_material = relationship('HandleMaterial', back_populates='products')
    guard_and_pommel = relationship('GuardAndPommel', back_populates='products')
    images = relationship("ProductImage", back_populates="product")
    inventory = relationship("Inventory", uselist=False, back_populates="product", foreign_keys=[Inventory.product_id])

