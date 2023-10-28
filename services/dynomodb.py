import boto3
from models.user_info import UserInfo
from logger import get_logger

dynamodb = boto3.resource('dynamodb')


class User:
    def __init__(self):
        self.table = dynamodb.Table('writetrack-data')

    def put_info(self, info_item: UserInfo):
        get_logger(self.__class__.__name__).info(f"put_info({dict(info_item)})")
        self.table.put_item(Item=dict(info_item))

    def get_all_info(self):

        get_logger(self.__class__.__name__).info("get_all_info()")

        # Use the scan operation to retrieve all items
        response = self.table.scan()

        # Extract the items from the response
        items = response.get('Items', [])

        # Continue scanning if the response is paginated
        while 'LastEvaluatedKey' in response:
            response = self.table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response.get('Items', []))

        return items
