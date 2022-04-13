const xml2json = require("xml2json");
const axios = require("axios");
exports.getAccessToken = async () => {
    const body = `<?xml version="1.0" encoding="utf-8" ?>
                    <env:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                        xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
                      <env:Body>
                        <n1:login xmlns:n1="urn:enterprise.soap.sforce.com">
                          <n1:username>Provide User name here</n1:username>
                          <n1:password>Provide password here</n1:password>
                        </n1:login>
                      </env:Body>
                    </env:Envelope>`;
    const headers = {
        SOAPAction: "''",
        "Content-Type": "text/xml"
    };
    const url = `https://test.salesforce.com/services/Soap/c/54.0`
    const response = await axios.post(url, body, {headers});
    const data = JSON.parse(xml2json.toJson(response.data, {reversible: true}));
    let serverUrl = data['soapenv:Envelope']['soapenv:Body']['loginResponse']['result']['serverUrl']['$t'];
    serverUrl = serverUrl.split('/')[2];
    return {
        instanceUrl: serverUrl,
        sessionId: data['soapenv:Envelope']['soapenv:Body']['loginResponse']['result']['sessionId']['$t']
    };
}
