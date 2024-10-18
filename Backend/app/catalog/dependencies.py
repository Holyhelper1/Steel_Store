from typing import Optional, List

from fastapi import Query

from app.catalog.shemas import SCatalogFilters


def get_catalog_filters(
    manufacturer_ids: Optional[List[int]] = Query(None, description="IDs производителей"),
    steel_type_ids: Optional[List[int]] = Query(None, description="IDs типов стали"),
    handle_material_ids: Optional[List[int]] = Query(None, description="IDs материалов рукояти"),
    guard_and_pommel_ids: Optional[List[int]] = Query(None, description="IDs гарды и навершия"),
    gilding_blade: Optional[bool] = Query(None, description="Фильтр по позолоте лезвия"),
    gilding_drawling: Optional[bool] = Query(None, description="Фильтр по позолоте рисунка"),
    total_length_min: Optional[float] = Query(None, ge=0, description="Минимальная длина изделия"),
    total_length_max: Optional[float] = Query(None, ge=0, description="Максимальная длина изделия"),
    blade_length_min: Optional[float] = Query(None, ge=0, description="Минимальная длина лезвия"),
    blade_length_max: Optional[float] = Query(None, ge=0, description="Максимальная длина лезвия"),
    blade_width_min: Optional[float] = Query(None, ge=0, description="Минимальная ширина лезвия"),
    blade_width_max: Optional[float] = Query(None, ge=0, description="Максимальная ширина лезвия"),
    price_min: Optional[float] = Query(None, ge=0, description="Минимальная цена"),
    price_max: Optional[float] = Query(None, ge=0, description="Максимальная цена"),
    rating: Optional[float] = Query(None, ge=0, lt=5, description="Минимальный рейтинг"),
) -> SCatalogFilters:
    return SCatalogFilters(
        manufacturer_ids=manufacturer_ids,
        steel_type_ids=steel_type_ids,
        handle_material_ids=handle_material_ids,
        guard_and_pommel_ids=guard_and_pommel_ids,
        gilding_blade=gilding_blade,
        gilding_drawling=gilding_drawling,
        total_length_min=total_length_min,
        total_length_max=total_length_max,
        blade_length_min=blade_length_min,
        blade_length_max=blade_length_max,
        blade_width_min=blade_width_min,
        blade_width_max=blade_width_max,
        price_min=price_min,
        price_max=price_max,
        rating=rating,
    )