# from fastapi import HTTPException
# from app.schemas.products import ProductsIn
# from app import models
# def add_land_product(land_info: ProductsIn ,db: Session):
#     land_info = db.query(models.Product).filter(models.Product.os_listing_id == land_info.os_listing_id).first()
#     if land_info:
#         raise HTTPException(status_code=400, detail="land info already added")
#     land_obj = models.Product(**land_info)
#     db.add(land_obj)
#     db.commit()
#     db.refresh()
#     return land_obj