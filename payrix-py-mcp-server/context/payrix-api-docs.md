
# Payrix Pro API Quick Reference

## Authentication
- Use APIKEY header: `APIKEY: {API_key}`

## Pagination
- `page[number]={n}`: Page number
- `page[limit]={m}`: Results per page (max 100)

## Search Header Format
- Header: `search: {field}[{operator}]={value}`
- Example: `created[greater]=20240601`
- Multiple search headers allowed

## Supported Operators
| Operator   | Usage Example                | Description                  |
|-----------|------------------------------|------------------------------|
| equals    | status[equals]=2             | Equality (null/0/empty OK)   |
| exact     | dba[exact]=Acme Inc          | Exact match                  |
| greater   | created[greater]=20240601    | Greater than (date/number)   |
| less      | created[less]=20250801       | Less than (date/number)      |
| in        | status[in]=1,2,3             | In list (comma, no spaces)   |
| like      | dba[like]=Test%25            | Partial string (wildcard %25)|
| notlike   | dba[notlike]=%25Test%25      | Not like (wildcard %25)      |
| diff      | status[diff]=0               | Not equal                    |
| notin     | status[notin]=1,2            | Not in list                  |

## Field Types
- `created`: date (format: YYYYMMDD)
- `dba`: string
- `status`: integer


## Key Patterns & Examples
- Merchants created after June 2024: `created[greater]=20240601`
- Merchants created before 1st Aug 2025: `created[less]=20250801`
- Merchants with status 2: `status[equals]=2`
- Merchants where dba contains 'Test': `dba[like]=Test%25`
- Multiple values: `status[in]=1,2,3`
- Multiple search parameters (AND): `created[less]=20250801&entity[equals]=t1_ent_687e864cd3038063a6d6000`

  - This will return merchants created before 1st Aug 2025 and with the specified entity.

## Advanced Search
- Combine with and/or: `and[0][or][0][name][like]=%25jsmith%25`
- Hierarchical: `and[0][or][1][custom][like]=%25jsmith%25`

## Sorting
- `created[sort]=desc` (default)
- `created[sort]=asc`

## Collection Operators
- `totals: sum[]=total` (sum field in results)
- `totals: count[]=id` (count non-zero values)

## Expanding Related Resources
- `expand[merchant][]` (include full merchant object)
- `expand[id]` (only id field)

## Error Codes
- 200 OK: Success
- 400 Bad Request: Invalid request
- 401 Unauthorized: Invalid API key
- 429 Too Many Requests: Rate limit exceeded

## Rate Limiting
- 1,000 requests in 10 seconds
- 10-second block if exceeded

## Notes
- Date values must be in `YYYYMMDD` format (e.g., `20250801`)
- Only supported fields/operators are accepted
- Invalid formats (e.g., `created:<2025-08-01`) will result in errors
