import asyncio
from typing import Optional

from fastapi import APIRouter, Path, Depends
from app.catalog.shemas import SCatalogFilters, SCategories, SCatalogSorting, SCatalogPagination, SCatalogResponse, SProductResponse
from app.catalog.dependencies import get_catalog_filters
from app.catalog.dao import CatalogDAO
from fastapi_cache.decorator import cache

from app.exceptions import ProductNotFoundException

router = APIRouter(
    tags=['Каталог'],
)


@router.get('/categories/', response_model=SCategories)
@cache(expire=60*60)
async def get_all_categories():
    categories = await CatalogDAO.get_categories()
    response = {
        'categories': [
            {'id_category': row.id,
                'category_name': row.name,
                'description': row.description
            } for row in categories
        ]
    }
    return response

@router.get('/categories/{category_id}/catalog/', response_model=SCatalogResponse)
async def get_catalog_by_category(
    category_id: Optional[int] = Path(..., ge=0),
    filters: SCatalogFilters = Depends(get_catalog_filters),
    sorting: SCatalogSorting = Depends(),
    pagination: SCatalogPagination = Depends()):

    catalog, get_filters = await asyncio.gather(
        CatalogDAO.get_catalog(category_id, pagination, filters, sorting),
        CatalogDAO.get_filters_data(category_id)
    )

    response = {
        'filters': get_filters,
        'sorting': sorting,
        'current_filters': filters,
        'category_id': category_id,
        'catalog': catalog
    }
    return response

@cache(expire=60*10)
@router.get('/categories/{category_id}/catalog/{product_id}/', response_model=SProductResponse)
async def get_product(category_id: int = Path(..., ge=0, description="Параметр обязательный, но не используется в запросе"),
                      product_id: int = Path(..., ge=0)):
    product = await CatalogDAO.get_product(product_id)
    if product is not None:
        response = {
            'product_id': product.id,
            'name': product.name,
            'description': product.description,
            'brand': product.brand.name,
            'price': product.price,
            'total_length': product.total_length,
            'blade_length': product.blade_length,
            'blade_width': product.blade_width,
            'rating': product.rating,
            'product_model_number': product.model_number,
            'series': product.series,
            'images': [product.main_img_url] + [obj_image.img_url for obj_image in product.images],
            'in_stock': product.inventory.in_stock,
        }
        return response
    raise ProductNotFoundException

