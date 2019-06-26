import requests
import logging

default_url="http://localhost:5000/employees"
default_headers={'Content-type': 'application/json'}
logging.basicConfig(format='%(asctime)s %(process)d:%(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Sender():
    def generateData(self, index=1):
        return {"index": index , "message": "lorem Ipsum"}


    def send(self, datas, url = default_url, headers = default_headers):

        requests.post(url, json=datas, headers=headers)
        logging.debug("Post sent\n Json: %s\n headers:%s ", datas, headers)


    def sendMultiple(self, index=5):
        for i in range(index):
            self.send(self.generateData(i))


app = Sender()

if __name__ == "__main__":
    from sys import argv

    logging.info("Started")
    if len(argv) == 2:
        app.sendMultiple(index=int(argv[1]))
    else:
        app.sendMultiple()
    logging.info("Closed")
