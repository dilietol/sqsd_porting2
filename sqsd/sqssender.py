import boto3

queue_url = 'https://sqs.eu-central-1.amazonaws.com/650675451866/ap04024_sqs_analytics'

class SqsSender():
    # Create SQS client
    sqs = boto3.client('sqs')

    def send(self, message):

        response = self.sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageAttributes={
                'Title': {
                    'DataType': 'String',
                    'StringValue': 'The Whistler'
                },
                'Author': {
                    'DataType': 'String',
                    'StringValue': 'John Grisham'
                },
                'WeeksOn': {
                    'DataType': 'Number',
                    'StringValue': '6'
                }
            },
            MessageBody=(
                str(message)
            )
        )

        #print(response['MessageId'])
        #print(response)
        return response['ResponseMetadata']['HTTPStatusCode']