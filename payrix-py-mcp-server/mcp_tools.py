# Common supported search operators for all tools
SUPPORTED_SEARCH_OPERATORS = (
    "| Operator   | Usage Example                | Description                  |\n"
    "|-----------|------------------------------|------------------------------|\n"
    "| equals    | status[equals]=2             | Equality (null/0/empty OK)   |\n"
    "| exact     | dba[exact]=Acme Inc          | Exact match                  |\n"
    "| greater   | created[greater]=20240601    | Greater than (date/number)   |\n"
    "| less      | created[less]=20250801       | Less than (date/number)      |\n"
    "| in        | status[in]=1,2,3             | In list (comma, no spaces)   |\n"
    "| like      | dba[like]=Test%25            | Partial string (wildcard %25)|\n"
    "| notlike   | dba[notlike]=%25Test%25      | Not like (wildcard %25)      |\n"
    "| diff      | status[diff]=0               | Not equal                    |\n"
    "| notin     | status[notin]=1,2            | Not in list                  |"
)
from mcp_instance import mcp
from mcp.server.fastmcp import Context
from mcp_common import get_http_client

import logging

 # Helper for GET requests with error handling and custom headers
async def _do_get(client, url, query_params=None, headers=None):
    if query_params is None:
        query_params = {}
    if headers is None:
        headers = {}
    try:
        response = await client.get(url, params=query_params, headers=headers)
        response.raise_for_status()
        return str(response.text)
    except Exception as e:
        if hasattr(e, 'response') and hasattr(e.response, 'status_code'):
            return f"API Error: {e.response.status_code} - {getattr(e.response, 'text', str(e))}"
        return f"Error: {str(e)}"


@mcp.tool(description="Show/Query/Get/Fetch/Retrieve a Merchant, an organization that processes credit card payments, each associated with an Entity.")
async def getMerchants(ctx: Context, search: str = '', totals: str = '', page_number_: int = 0, page_limit_: int = 0) -> str:
    """
    Show/Query/Get/Fetch/Retrieve a Merchant, an organization that processes credit card payments, each associated with an Entity.

    Parameters:
        ctx (Context): The MCP context.
        request_token (str): Optional request token.
        search (str): Search filter string. Use key[operator]=value format. Supported operators: equals, not, less, greater, like, in, etc.
            Example: 'created[less]=2025-08-01' or 'name[like]=Acme'. Multiple conditions can be separated by & operator.
            Examples:
                - 'created[less]=2025-08-01'
                - 'name[like]=Acme'
                - 'status[equals]=active'
                - 'created[greater]=2024-01-01&status[equals]=active'
        totals (str): If 'true', include total count in response.
        page_number_ (int): Page number for pagination.
        page_limit_ (int): Page size for pagination.

    Returns:
        str: JSON string of merchant data or error message.
        ## merchantsResponse properties (property | type):
        #  id | string, created | string (YYYY-MM-DD HH:MM:SS.SSSS), modified | string (YYYY-MM-DD HH:MM:SS.SSSS), creator | string, modifier | string, lastActivity | string (YYYY-MM-DD HH:MM:SS), totalApprovedSales | integer (int64), entity | string, dba | string (0-50 chars), new | integer (0 or 1), incrementalAuthSupported | integer (0 or 1), seasonal | integer (0 or 1), advancedBilling | integer (0 or 1), established | integer (YYYYMMDD), annualCCSales | integer (int64), annualCCSaleVolume | integer (int64), annualACHSaleVolume | integer (int64), amexVolume | integer (int64), avgTicket | integer (int64), amex | string (1-15 chars), discover | string (1-15 chars), mcc | string, visaMvv | string, visaDisclosure | integer (0 or 1), disclosureIP | string, disclosureDate | integer (YYYYMMDD), environment | string (e.g., supermarket, moto, cardPresent, etc.), status | integer (0-6), autoBoarded | integer (0 or 1), statusReason | string, accountClosureReasonCode | string, accountClosureReasonDate | integer (YYYYMMDD), riskLevel | string (restricted, prohibited, high, medium, low), creditRatio | integer (int32), creditTimeliness | integer (int32), chargebackRatio | integer (int32), ndxDays | integer (int32), ndxPercentage | integer (int32), boarded | integer (int32), saqType | string (SAQ-A, SAQ-A-EP, SAQ-B, SAQ-B-IP, SAQ-C-VT, SAQ-C, SAQ-P2PE-HW, SAQ-D), saqDate | integer (YYYYMMDD), qsa | string, letterStatus | integer (0 or 1), letterDate | integer (YYYYMMDD), tcAttestation | integer (0 or 1), tmxSessionId | string, chargebackNotificationEmail | string, locationType | string (77, 78, 79, 80, 81), percentKeyed | integer (int32), totalVolume | integer (int64), percentEcomm | integer (int32), percentBusiness | integer (int32), applePayActive | integer (0 or 1), applePayStatus | string, googlePayActive | integer (0 or 1), naics | string (see NAICS codes), naicsDescription | string, expressBatchCloseMethod | string (TimeInitiated, MerchantInitiated), expressBatchCloseTime | string, passTokenEnabled | integer (0 or 1), inactive | integer (0 or 1), frozen | integer (0 or 1)
    """
    async with await get_http_client() as client:
        url = "/merchants"
        query_params = {}
        headers = {}
        if page_number_ is not None:
            query_params['page[number]'] = page_number_
        if page_limit_ is not None:
            query_params['page[limit]'] = page_limit_
        if search:
            if isinstance(search, str):
                headers['search'] = search
                logging.info(f"[DEBUG] Merchants search header: {headers['search']}")
        if totals:
            headers['totals'] = str(totals).lower()
        raw = await _do_get(client, url, query_params, headers)
        try:
            import json
            resp = json.loads(raw)
            if isinstance(resp, dict) and 'data' in resp and not resp['data']:
                return "No merchants found for the given criteria."
        except Exception:
            pass
        return raw


@mcp.tool(description="Show/Query/Get/Fetch/Retrieve a Merchant by Id, which is an organization that processes credit card payments and each is associated with an Entity.")
async def getMerchantsId(id: str, ctx: Context, search: str = '') -> str:
    """
    Show/Query/Get/Fetch/Retrieve a Merchant, an organization that processes credit card payments, each associated with an Entity.

    Parameters:
        ctx (Context): The MCP context.
        request_token (str): Optional request token.
        search (str): Search filter string. Use key[operator]=value format. Supported operators: equals, not, less, greater, like, in, etc.
            Example: 'created[less]=2025-08-01' or 'name[like]=Acme'. Multiple conditions can be separated by & operator.
            Examples:
                - 'created[less]=2025-08-01'
                - 'name[like]=Acme'
                - 'status[equals]=active'
                - 'created[greater]=2024-01-01&status[equals]=active'
    Returns:
        str: JSON string of merchant data or error message.
        ## merchantsResponse properties (property | type):
        #  id | string, created | string (YYYY-MM-DD HH:MM:SS.SSSS), modified | string (YYYY-MM-DD HH:MM:SS.SSSS), creator | string, modifier | string, lastActivity | string (YYYY-MM-DD HH:MM:SS), totalApprovedSales | integer (int64), entity | string, dba | string (0-50 chars), new | integer (0 or 1), incrementalAuthSupported | integer (0 or 1), seasonal | integer (0 or 1), advancedBilling | integer (0 or 1), established | integer (YYYYMMDD), annualCCSales | integer (int64), annualCCSaleVolume | integer (int64), annualACHSaleVolume | integer (int64), amexVolume | integer (int64), avgTicket | integer (int64), amex | string (1-15 chars), discover | string (1-15 chars), mcc | string, visaMvv | string, visaDisclosure | integer (0 or 1), disclosureIP | string, disclosureDate | integer (YYYYMMDD), environment | string (e.g., supermarket, moto, cardPresent, etc.), status | integer (0-6), autoBoarded | integer (0 or 1), statusReason | string, accountClosureReasonCode | string, accountClosureReasonDate | integer (YYYYMMDD), riskLevel | string (restricted, prohibited, high, medium, low), creditRatio | integer (int32), creditTimeliness | integer (int32), chargebackRatio | integer (int32), ndxDays | integer (int32), ndxPercentage | integer (int32), boarded | integer (int32), saqType | string (SAQ-A, SAQ-A-EP, SAQ-B, SAQ-B-IP, SAQ-C-VT, SAQ-C, SAQ-P2PE-HW, SAQ-D), saqDate | integer (YYYYMMDD), qsa | string, letterStatus | integer (0 or 1), letterDate | integer (YYYYMMDD), tcAttestation | integer (0 or 1), tmxSessionId | string, chargebackNotificationEmail | string, locationType | string (77, 78, 79, 80, 81), percentKeyed | integer (int32), totalVolume | integer (int64), percentEcomm | integer (int32), percentBusiness | integer (int32), applePayActive | integer (0 or 1), applePayStatus | string, googlePayActive | integer (0 or 1), naics | string (see NAICS codes), naicsDescription | string, expressBatchCloseMethod | string (TimeInitiated, MerchantInitiated), expressBatchCloseTime | string, passTokenEnabled | integer (0 or 1), inactive | integer (0 or 1), frozen | integer (0 or 1)
    """
    async with await get_http_client() as client:
        url = "/merchants/{id}"
        if id is not None:
            url = url.replace('{id}', str(id))
        headers = {}
        if search:
            headers['search'] = search
        return await _do_get(client, url, headers=headers)


@mcp.tool(description="Show/Query/Get/Fetch/Retrieve a Transaction. Transactions hold all of the information relating to a particular credit card transaction, including the merchant, token, subscription, customer and card information.")
async def getTxns(ctx: Context, search: str = '', totals: str = '', page_number_: int = 0, page_limit_: int = 0) -> str:
    """
    Show/Query/Get/Fetch/Retrieve a Transaction. Transactions hold all of the information relating to a particular credit card transaction, including the merchant, token, subscription, customer and card information.

        Parameters:
            ctx (Context): The MCP context.
            request_token (str): Optional request token.
            search (str): Search filter string. Use key[operator]=value format. Supported operators: equals, not, less, greater, like, in, etc.
                Example: 'created[less]=2025-08-01' or 'name[like]=Acme'or 'merchant[equals]=p1_mer_688b17e778a020dfcf67a59'. Multiple conditions can be separated by & operator.
                Examples:
                    - 'created[less]=2025-08-01'
                    - 'name[like]=Acme'
                    - 'status[equals]=active'
                    - 'created[greater]=2024-01-01&status[equals]=active'
                    - 'merchant[equals]=p1_mer_688b17e778a020dfcf67a59'
            totals (str): If 'true', include total count in response.
            page_number_ (int): Page number for pagination.
            page_limit_ (int): Page size for pagination.

        Returns:
            str: JSON string of transaction data or error message.
            # txnsResponse properties (property | type):
            # id | string, created | string, modified | string, creator | string, modifier | string, ipCreated | string, ipModified | string, merchant | string, token | string, payment | string, fortxn | string, fromtxn | string, batch | string, subscription | string, statement | string, type | object, expiration | string, serviceCode | string, funded | integer, returned | string, currency | object, fundingCurrency | object, currencyConversion | object, convenienceFee | integer, fee | number, platform | object, authDate | integer, authCode | string, captured | string, settled | string, settledCurrency | object, settledTotal | integer, allowPartial | object, order | string, description | string, descriptor | string, traceNumber | integer, discount | integer, shipping | integer, duty | integer, terminal | string, terminalCapability | object, entryMode | object, origin | object, mobile | object, tax | integer, surcharge | integer, total | integer, cashback | integer, authorization | string, originalApproved | integer, approved | integer, authentication | string, authenticationId | string, cvv | integer, cvvStatus | object, swiped | object, emv | object, signature | object, pin | object, pinEntryCapability | object, unattended | object, cofType | object, copyReason | object, clientIp | string, first | string, middle | string, last | string, company | string, email | string, address1 | string, address2 | string, city | string, state | string, zip | string, country | object, phone | string, mid | string, status | object, refunded | integer, reserved | object, misused | object, checkStage | object, unauthReason | object, authTokenCustomer | string, channel | string, imported | object, requestSequence | integer, processedSequence | integer, debtRepayment | object, fundingEnabled | object, fbo | string, txnsession | string, inactive | object, frozen | object, tip | integer, softPosId | string, softPosDeviceTypeIndicator | string, networkTokenIndicator | object, txnRefs | array, pinlessDebitConversion | object
    """
    async with await get_http_client() as client:
        url = "/txns"
        query_params = {}
        headers = {}
        if page_number_ is not None:
            query_params['page[number]'] = page_number_
        if page_limit_ is not None:
            query_params['page[limit]'] = page_limit_
        if search:
            if isinstance(search, str):
                headers['search'] = search
                logging.info(f"[DEBUG] Txns search header: {headers['search']}")
        if totals:
            headers['totals'] = str(totals).lower()
        raw = await _do_get(client, url, query_params, headers)
        try:
            import json
            resp = json.loads(raw)
            if isinstance(resp, dict) and 'data' in resp and not resp['data']:
                return "No transactions found for the given criteria."
        except Exception:
            pass
        return raw
        return await _do_get(client, url)

@mcp.tool(description="Show/Query/Get/Fetch/Retrieve a Transaction by Id. Transactions hold all of the information relating to a particular credit card transaction, including the merchant, token, subscription, customer and card information.")
async def getTxnsId(id: str, ctx: Context, search: str = '') -> str:
    """
    Show/Query/Get/Fetch/Retrieve a Transaction. Transactions hold all of the information relating to a particular credit card transaction, including the merchant, token, subscription, customer and card information.

        Parameters:
            ctx (Context): The MCP context.
            request_token (str): Optional request token.
            search (str): Search filter string. Use key[operator]=value format. Supported operators: equals, not, less, greater, like, in, etc.
                Example: 'created[less]=2025-08-01' or 'name[like]=Acme'or 'merchant[equals]=p1_mer_688b17e778a020dfcf67a59'. Multiple conditions can be separated by & operator.
                Examples:
                    - 'created[less]=2025-08-01'
                    - 'name[like]=Acme'
                    - 'status[equals]=active'
                    - 'created[greater]=2024-01-01&status[equals]=active'
                    - 'merchant[equals]=p1_mer_688b17e778a020dfcf67a59'
        Returns:
            str: JSON string of transaction data or error message.
            # txnsResponse properties (property | type):
            # id | string, created | string, modified | string, creator | string, modifier | string, ipCreated | string, ipModified | string, merchant | string, token | string, payment | string, fortxn | string, fromtxn | string, batch | string, subscription | string, statement | string, type | object, expiration | string, serviceCode | string, funded | integer, returned | string, currency | object, fundingCurrency | object, currencyConversion | object, convenienceFee | integer, fee | number, platform | object, authDate | integer, authCode | string, captured | string, settled | string, settledCurrency | object, settledTotal | integer, allowPartial | object, order | string, description | string, descriptor | string, traceNumber | integer, discount | integer, shipping | integer, duty | integer, terminal | string, terminalCapability | object, entryMode | object, origin | object, mobile | object, tax | integer, surcharge | integer, total | integer, cashback | integer, authorization | string, originalApproved | integer, approved | integer, authentication | string, authenticationId | string, cvv | integer, cvvStatus | object, swiped | object, emv | object, signature | object, pin | object, pinEntryCapability | object, unattended | object, cofType | object, copyReason | object, clientIp | string, first | string, middle | string, last | string, company | string, email | string, address1 | string, address2 | string, city | string, state | string, zip | string, country | object, phone | string, mid | string, status | object, refunded | integer, reserved | object, misused | object, checkStage | object, unauthReason | object, authTokenCustomer | string, channel | string, imported | object, requestSequence | integer, processedSequence | integer, debtRepayment | object, fundingEnabled | object, fbo | string, txnsession | string, inactive | object, frozen | object, tip | integer, softPosId | string, softPosDeviceTypeIndicator | string, networkTokenIndicator | object, txnRefs | array, pinlessDebitConversion | object
    """
    async with await get_http_client() as client:
        url = "/txns/{id}"
        if id is not None:
                    url = url.replace('{id}', str(id))
        headers = {}
        if search:
            headers['search'] = search
        return await _do_get(client, url, headers=headers)
