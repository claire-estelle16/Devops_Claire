from fastapi import APIRouter
from schemas.indexSchema import Item
from config.db import con
from models.indexModel import items

itemRoute = APIRouter()


@itemRoute.get("/items")
async def read_items():
    data = con.execute(items.select()).fetchall()
    resultat = [dict(row._mapping) for row in data]
    return {"success": True, "data": resultat}


@itemRoute.get("/items/{id}")
async def read_only_item(id: int):
    resultat = con.execute(items.select().where(items.c.id == id)).fetchone()
    if resultat:
        return {"success": True, "data": dict(resultat._mapping)}
    else:
        return {"success": False, "message": "Item pas trouvé"}


@itemRoute.post("/items")
async def store_item(item: Item):
    resultat = con.execute(
        items.insert().values(
            name=item.name,
            price=item.price,
            in_stock=item.in_stock,
        )
    )
    con.commit()
    if resultat.rowcount > 0:
        return {
            "success": True,
            "message": "Item enregistré avec succès",
        }
    else:
        return {
            "success": False,
            "message": "Problème lors de l'enregistrement de l'item",
        }


@itemRoute.put("/items/{id}")
async def edit_item(id: int, item: Item):
    resultat = con.execute(
        items.update()
        .values(
            name=item.name,
            price=item.price,
            in_stock=item.in_stock,
        )
        .where(items.c.id == id)
    )
    con.commit()
    if resultat.rowcount > 0:
        return {
            "success": True,
            "message": "Item mis à jour avec succès",
        }
    else:
        return {"success": False, "message": "Item pas trouvé "}


@itemRoute.delete("/items/{id}")
async def delete_item(id: int):
    resultat = con.execute(items.delete().where(items.c.id == id))
    con.commit()
    if resultat.rowcount > 0:
        return {
            "success": True,
            "message": "Item supprimé avec succès",
        }
    else:
        return {"success": False, "message": "Item pas trouvé"}
