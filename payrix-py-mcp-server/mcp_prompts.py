# Prompts for Payrix tools
GET_MERCHANTS_PROMPT = (
    "Please provide the criteria to list merchants from the Payrix API. "
    "You can specify conditions such as 'top 4', 'created after 2024-01-01', 'name like Acme', etc. "
    "For multiple conditions, use '&' as the separator, e.g., 'status[equals]=active&created[greater]=2024-01-01'."
)
GET_MERCHANTS_ID_PROMPT = "Please provide the merchant ID to retrieve details for a specific merchant."
GET_TXNS_PROMPT = (
    "Please provide the criteria to list transactions from the Payrix API. "
    "You can specify conditions such as 'top 4', 'created after 2024-01-01', 'amount greater than 100', etc. "
    "For multiple conditions, use '&' as the separator, e.g., 'merchant[equals]=000000000000007&created[greater]=2025-07-29'. "
    "Show me all transactions related to a merchant MMM in last XX days."
)
GET_TXNS_ID_PROMPT = "Please provide the transaction ID to retrieve details for a specific transaction."
