import asyncio

from sqlalchemy.orm import joinedload

from app.database import async_session_maker
from app.catalog.models import Product, HandleMaterial, SteelType, GuardAndPommel, Manufacturer, Category
from app.catalog.shemas import SCatalogFilters, SCatalogSorting, SCatalogPagination
from sqlalchemy import select, func, desc, asc

class CatalogDAO:

    @classmethod
    async def get_categories(cls):
        async with async_session_maker() as session:
            stmt = select(
                Category.id,
                Category.name,
                Category.description
            ).select_from(Category)

            raw_categories = await session.execute(stmt)
            categories = raw_categories.all()
            return categories if categories else []

    @classmethod
    async def get_filters_data(cls, category_id: int):
        async with async_session_maker() as session:
            stmt = select(
                func.min(Product.price).label('min_price'),
                func.max(Product.price).label('max_price'),
                func.min(Product.total_length).label('min_total_length'),
                func.max(Product.total_length).label('max_total_length'),
                func.min(Product.blade_length).label('min_blade_length'),
                func.max(Product.blade_length).label('max_blade_length'),
                func.min(Product.blade_width).label('min_blade_width'),
                func.max(Product.blade_width).label('max_blade_width'),
            ).select_from(Product).where(Product.category_id == category_id)

            main_stmt = await session.execute(stmt)
            filters_data = main_stmt.one()

            manufacturers_stmt = select(
                Manufacturer.id,
                Manufacturer.name,
                func.count(Product.id).label('count')
            ).join(Product).where(Product.category_id == category_id).group_by(Manufacturer.id)

            steel_types_stmt = select(
                SteelType.id,
                SteelType.name,
                func.count(Product.id).label('count')
            ).join(Product).where(Product.category_id == category_id).group_by(SteelType.id)

            handle_materials_stmt = select(
                HandleMaterial.id,
                HandleMaterial.name,
                func.count(Product.id).label('count')
            ).join(Product).where(Product.category_id == category_id).group_by(HandleMaterial.id)

            guards_and_pommels_stmt = select(
                GuardAndPommel.id,
                GuardAndPommel.name,
                func.count(Product.id).label('count')
            ).join(Product).where(Product.category_id == category_id).group_by(GuardAndPommel.id)

            manufacturers_stmt_result, steel_types_stmt_result, handle_materials_stmt_result, guards_and_pommels_stmt_result = await asyncio.gather(
                session.execute(manufacturers_stmt),
                session.execute(steel_types_stmt),
                session.execute(handle_materials_stmt),
                session.execute(guards_and_pommels_stmt),
            )
            manufacturers = [{'id': row.id, 'name': row.name, 'count': row.count} for row in manufacturers_stmt_result.all()]
            steel_types = [{'id': row.id, 'name': row.name, 'count': row.count} for row in steel_types_stmt_result.all()]
            handle_materials = [{'id': row.id, 'name': row.name, 'count': row.count} for row in handle_materials_stmt_result.all()]
            guards_and_pommels = [{'id': row.id, 'name': row.name, 'count': row.count} for row in guards_and_pommels_stmt_result.all()]

            filters = {
                'manufacturers': manufacturers,
                'steel_types': steel_types,
                'handle_materials': handle_materials,
                'guards_and_pommels': guards_and_pommels,
                'price': {
                    'min': filters_data[0],
                    'max': filters_data[1],
                },
                'total_length': {
                    'min': filters_data[2],
                    'max': filters_data[3],
                },
                'blade_length': {
                    'min': filters_data[4],
                    'max': filters_data[5],
                },
                'blade_width': {
                    'min': filters_data[6],
                    'max': filters_data[7],
                }
            }
            return filters

    @classmethod
    async def get_catalog(cls, category_id: int, pagination: SCatalogPagination, filters: SCatalogFilters, sorting: SCatalogSorting):
        async with async_session_maker() as session:
            session.begin()
            """
            Главный запрос
                SELECT pd.id, pd.name, st.name as steel_type, hm.name as handle_material, pd.price, pd.rating FROM Products as pd
                JOIN steel_types AS st ON st.id = pd.steel_type_id
                JOIN handel_materials AS hm ON hm.id = pd.handle_material_id
                JOIN guards_and_pommels AS gp ON gp.id = pd.guard_and_pommel_id
            """
            stmt = select(
                Product.id,
                Product.name,
                SteelType.name.label('steel_type'),
                HandleMaterial.name.label('handle_material'),
                Product.price,
                Product.rating,
                Product.main_img_url.label('img_url')
            ).select_from(Product).join(HandleMaterial, HandleMaterial.id == Product.handle_material_id
                                        ).join(SteelType, SteelType.id==Product.steel_type_id
                                               ).join(GuardAndPommel, GuardAndPommel.id==Product.guard_and_pommel_id)


            # Выбор категории
            stmt = stmt.where(Product.category_id == category_id)
            # Фильтрация
            if filters.manufacturer_ids:
                stmt = stmt.where(Product.manufacturer_id.in_(filters.manufacturer_ids))
            if filters.steel_type_ids:
                stmt = stmt.where(SteelType.id.in_(filters.steel_type_ids))
            if filters.handle_material_ids:
                stmt = stmt.where(HandleMaterial.id.in_(filters.handle_material_ids))
            if filters.guard_and_pommel_ids:
                stmt = stmt.where(GuardAndPommel.id.in_(filters.guard_and_pommel_ids))

            stmt = stmt.where(
                (Product.total_length >= filters.total_length_min) if filters.total_length_min is not None else True,
                (Product.total_length <= filters.total_length_max) if filters.total_length_max is not None else True,
                (Product.blade_length >= filters.blade_length_min) if filters.blade_length_min is not None else True,
                (Product.blade_length <= filters.blade_length_max) if filters.blade_length_max is not None else True,
                (Product.blade_width >= filters.blade_width_min) if filters.blade_width_min is not None else True,
                (Product.blade_width <= filters.blade_width_max) if filters.blade_width_max is not None else True,
                (Product.gilding_blade == True) if filters.gilding_blade is not None else True,
                (Product.gilding_drawling == True) if filters.gilding_drawling is not None else True,
                (Product.price >= filters.price_min) if filters.price_min is not None else True,
                (Product.price <= filters.price_max) if filters.price_max is not None else True,
                (Product.rating >= filters.rating) if filters.rating is not None else True
            )
            if pagination:
                stmt = stmt.limit(pagination.limit).offset(pagination.offset)

            #Сортировка
            if sorting.sort_by is not None:
                if sorting.sort_by == 'popularity':
                    stmt = stmt.order_by(desc(Product.rating))
                if sorting.sort_by == 'price_asc':
                    stmt = stmt.order_by(asc(Product.price))
                if sorting.sort_by == 'price_desc':
                    stmt = stmt.order_by(desc(Product.price))

            # Запрос к БД
            result = await session.execute(stmt)
            catalog_list = result.all()

            total_count_stmt = select(func.count(Product.id)).where(Product.category_id == category_id)
            total_count_result = await session.execute(total_count_stmt)
            total_items = total_count_result.scalar()

            # Расчет текущей страницы
            current_page = (pagination.offset // pagination.limit) + 1
            total_pages = (total_items + pagination.limit - 1) // pagination.limit  # Округление вверх

            # Возвращаемый результат
            catalog = {
                'total_pages': total_pages,
                'current_page': current_page,
                'results': [
                    {
                        'id': product.id,
                        'name': product.name,
                        'steel_type': product.steel_type,
                        'handle_material': product.handle_material,
                        'price': float(product.price),  # Преобразуем DECIMAL в float
                        'rating': product.rating,
                        'img_url': product.img_url
                    }
                    for product in catalog_list
                ],
                'limit': pagination.limit,
                'offset': pagination.offset
            }

            return catalog

    @classmethod
    async def get_product(cls, product_id: int):
        async with async_session_maker() as session:
            stmt = select(Product).options(joinedload(Product.brand), joinedload(Product.images), joinedload(Product.inventory)).where(Product.id == product_id)
            result = await session.scalars(stmt)
            return result.first()


