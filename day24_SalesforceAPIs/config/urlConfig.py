version = '57.0'
request_headers = {
    'Sforce-Auto-Assign': True,
    'Content-Encoding': 'gzip',
    'If-Unmodified-Since': '',
    'If-Modified-Since': '',
    'If-None-Match': '',
    'If-Match': '',
    'Sforce-Duplicate-Rule-Header': 'allowSave=true, includeRecordDetails=true, runAsCurrentUser=true',
    'Sforce-Limit-Info': 'api-usage=10018/100000',
    'Sforce-Query-Options': 'batchSize=1000'
    # There is no guarantee that requested batch size is actual size when getting response. The size of records is
    # returned making sure the maximum performance.
}
# Visit this for valid date formats in Salesforce
# https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_valid_date_formats.htm
