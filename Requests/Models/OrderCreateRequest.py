from Requests.Models.Base.Request import Request


class OrdersCreateRequest(Request):
    id: int = 0,
    petId: int = 0,
    quantity: int = 0,
    shipDate: str = "",
    status: str = "",
    complete: bool = True

    def __init__(self, id: int, petId: int, quantity: int, shipDate: str, status: str, complete: bool):
        self.id = id
        self.petId = petId
        self.quantity = quantity
        self.shipDate = shipDate
        self.status = status
        self.complete = complete
