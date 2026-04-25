from boto3 import resource
from aws_lambda_powertools.logging import Logger
from boto3.dynamodb.conditions import Attr

from src.application.ports.output import RepositoryOutputPort


class DynamoDBOutputAdapter(RepositoryOutputPort):
    table = None
    logger: Logger

    def __init__(self, table_name: str):
        dynamodb = resource("dynamodb")
        self.table = dynamodb.Table(table_name)
        self.logger = Logger(service="DynamoDBOutputAdapter")

    def create(self, attributes: dict) -> bool:
        response = self.table.put_item(Item=attributes)
        return response["ResponseMetadata"]["HTTPStatusCode"] == 200

    def find_all(self, term: str | None = None) -> list[dict]:
        response = self.table.scan() if term is None else self.table.scan(
            FilterExpression=Attr("title").contains(term) | Attr("content").contains(term) | Attr("category").contains(
                term) | Attr("tags").contains(term)
        )
        return response["Items"] if "Items" in response else []
    
    def find_by_id(self, id: str) -> dict | None:
        response = self.table.get_item(Key={"id": id})
        return response["Item"] if "Item" in response else None

    def update(self, id: str, attributes: dict) -> bool:
        update_expression = "SET "
        expression_attributes = []
        expression_attribute_values = {}
        for key, value in attributes.items():
            expression_attributes.append(f"{key} = :{key}")
            expression_attribute_values[f":{key}"] = value
        update_expression += ", ".join(expression_attributes)
        response = self.table.update_item(
            Key={"id": id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
        )
        return response["ResponseMetadata"]["HTTPStatusCode"] == 200
    
    def delete(self, id: str) -> None:
        self.table.delete_item(Key={"id": id})
