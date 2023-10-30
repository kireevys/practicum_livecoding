import requests
from pydantic import BaseModel

from integrations.customer import Fine, get_customers_who_need_fines


class GibddRequestStruct(BaseModel):
    ...


class GibddRequest(BaseModel):
    token: str
    method: str
    data: GibddRequestStruct


class GibddDetailResponse(BaseModel):
    ...


class GibddResponse(BaseModel):
    method: str
    result: GibddDetailResponse


class FineId(BaseModel):
    fine_id: str


@cron("* * * * *")
def fine_saver_task():
    customers = get_customers_who_need_fines()
    client = GibddClient()
    for c in customers:
        for fine in client.get_fines(c.number):
            db.save(fine)


class GibddClient:
    def _request(self, request: GibddRequest) -> GibddResponse:
        result = requests.get(
            "gibdd.ru/api/v1", json={"method": request.method, "params": request.data}
        )
        return GibddResponse(method=request.method, result=result)

    def get_fines(self, sts_number: str) -> list[Fine]:
        result = self._request(
            GibddRequest(
                method="get_penalty_by_number",
                token=self._get_token(),
                data=self._build_request(sts_number, "get_penalty_by_number"),
            ),
        )
        fines = self._to_fine(result)
        return fines

    def _get_token(self) -> str:
        pass

    def _build_request(self, sts_number: str, method: str) -> GibddRequestStruct:
        pass

    def _to_fine(self, result) -> list[Fine]:
        pass
