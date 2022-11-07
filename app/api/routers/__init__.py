from fastapi import APIRouter
from fastapi.routing import APIRoute

from . import catalogue

router_v1 = APIRouter()

router_v1.include_router(catalogue.router, prefix="/catalogue")


def __use_route_names_as_operation_ids(router: APIRouter):
    # use just the method name for the operation id which makes the openapi docs nicer
    route_names = set()
    for route in router.routes:
        if isinstance(route, APIRoute):
            if route.name in route_names:
                raise ValueError(f"Duplicate route name: {route.name}")
            route_names.add(route.name)
            route.operation_id = route.name


__use_route_names_as_operation_ids(router_v1)
