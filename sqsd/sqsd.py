import requests
import logging
import datetime
import boto3

default_url="http://localhost:5000/employees"
default_url2="http://localhost:5001/employees"
queue_name="nomecodedacambiare"
default_headers={'User-Agent': 'aws-sqsd',
                 'X-Aws-Sqsd-Queue': queue_name,
                 'Content-Type': 'application/json'}
logging.basicConfig(format='%(asctime)s %(process)d:%(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
queue_url = 'https://sqs.eu-central-1.amazonaws.com/650675451866/ap04024_sqs_analytics'

class Sender():

    def send(self, datas, msgID, url = default_url2, headers = default_headers):
        self.addMsgHeaders(headers, msgID)
        r=requests.post(url, json=datas, headers=headers)
        logging.debug("Post sent\n Json: %s\n headers:%s ", datas, headers)
        return r.status_code

    def addMsgHeaders(self, headers, msgID):
        headers.update({'X-Aws-Sqsd-Msgid': str(msgID),
                        'X-Aws-Sqsd-First-Received-At': datetime.datetime.utcnow().isoformat(),
                        'X-Aws-Sqsd-Receive-Count': str(0)})

    def processMessage(self):
        # Create SQS client
        sqs = boto3.client('sqs')

        # Receive message from SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )
        print('Received')

        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        # Send message
        status = self.send(message,1)
        print('Forwarded. Return code: %s' % str(status))

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print('Received, forwarded and deleted message: %s' % message)

class TestSender():
    def generateData(self, index=1):
        return {"index": index , "message": "lorem Ipsum"}

    def testSenderMultiple(self, index=2):
        sender = Sender()
        for i in range(index):
            message = sender.processMessage()
            logging.debug("Response Status Code: "+ str(status))

app = TestSender()

if __name__ == "__main__":
    from sys import argv

    logging.info("Started")
    if len(argv) == 2:
        app.testSenderMultiple(index=int(argv[1]))
    else:
        app.testSenderMultiple()
    logging.info("Closed")
