from enum import Enum

from fastapi import Query, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from app.config import settings

class SSortOptions(str, Enum):
    popularity = "popularity"
    price_asc = "price_asc"
    price_desc = "price_desc"

class SMainFilters(BaseModel):
    id: int
    name: str
    count: Optional[int] = None

class SMinMax(BaseModel):
    min: float
    max: float

class SManufacturer(SMainFilters):
    pass

class SSteelType(SMainFilters):
    pass

class SHandleMaterial(SMainFilters):
    pass

class SGuardAndPommel(SMainFilters):
    pass

class SCategory(BaseModel):
    id_category: int
    category_name: str
    description: Optional[str] = None

class SCategories(BaseModel):
    categories: List[SCategory]

class SCatalogFilters(BaseModel):
    manufacturer_ids: Optional[List[int]] = Query(None, description="IDs производителей")
    steel_type_ids: Optional[List[int]] = Query(None, description="IDs типов стали")
    handle_material_ids: Optional[List[int]] = Query(None, description="IDs материалов рукояти")
    guard_and_pommel_ids: Optional[List[int]] = Query(None, description="IDs гарды и навершия")
    gilding_blade: Optional[bool] = Query(None, description="Фильтр по позолоте лезвия")
    gilding_drawling: Optional[bool] = Query(None, description="Фильтр по позолоте рисунка")
    total_length_min: Optional[float] = Query(None, ge=0, description="Минимальная длина изделия")
    total_length_max: Optional[float] = Query(None, ge=0, description="Максимальная длина изделия")
    blade_length_min: Optional[float] = Query(None, ge=0, description="Минимальная длина лезвия")
    blade_length_max: Optional[float] = Query(None, ge=0, description="Максимальная длина лезвия")
    blade_width_min: Optional[float] = Query(None, ge=0, description="Минимальная ширина лезвия")
    blade_width_max: Optional[float] = Query(None, ge=0, description="Максимальная ширина лезвия")
    price_min: Optional[float] = Query(None, ge=0, description="Минимальная цена")
    price_max: Optional[float] = Query(None, ge=0, description="Максимальная цена")
    rating: Optional[float] = Query(None, ge=0, lt=5, description="Минимальный рейтинг")


class SCatalogSorting(BaseModel):
    sort_by: Optional[SSortOptions] = Query(None,
                                           description="Поле для сортировки (например, 'popularity', 'price_asc', 'price_desc')")

class SCatalogPagination(BaseModel):
    limit: int = Query(settings.LIMIT_DEFAULT, ge=1, description="Лимит на количество товаров")
    offset: int = Query(settings.OFFSET_DEFAULT, ge=0, description="Смещение для пагинации")

class CatalogRequestFilters(BaseModel):
    manufacturers: List[SManufacturer]
    steel_types: List[SSteelType]
    handle_materials: List[SHandleMaterial]
    guards_and_pommels: List[SGuardAndPommel]
    gilding_blade: Optional[bool] = False
    gilding_drawling: Optional[bool] = False
    total_length: SMinMax
    blade_length: SMinMax
    blade_width: SMinMax
    price: SMinMax

class SCatalogProductSchema(BaseModel):
    id: int
    name: str
    steel_type: str
    handle_material: str
    price: float
    rating: float
    img_url: str

class SCatalogProducts(BaseModel):
    total_pages: int
    current_page: int
    results: List[SCatalogProductSchema]
    limit: int
    offset: int

class SProductResponse(BaseModel):
    product_id: int
    name: str
    description: str
    brand: str
    price: float
    total_length: float
    blade_length: float
    blade_width: float
    rating: float
    product_model_number: str
    series: str
    images: List[str]
    in_stock: int


class SCatalogResponse(BaseModel):
    filters: CatalogRequestFilters
    sorting: SCatalogSorting
    current_filters: SCatalogFilters
    category_id: int
    catalog: Optional[SCatalogProducts] = None