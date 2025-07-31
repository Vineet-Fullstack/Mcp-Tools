from mcp_instance import mcp

# --- Utility function to extract fields and types from a resource schema ---
import re
import yaml

def get_resource_fields_and_types(resource_func):
    """
    Given a resource function (decorated with @mcp.resource),
    returns a dict of field names to {type, description} from the schema.
    """
    schema_str = resource_func()
    # Replace escaped newlines with real newlines for YAML parsing
    schema_str = schema_str.replace('\\n', '\n')
    # Remove leading/trailing whitespace
    schema_str = schema_str.strip()
    # Find the 'properties:' section and parse as YAML
    match = re.search(r'(properties:.*)', schema_str, re.DOTALL)
    if not match:
        return {}
    yaml_str = match.group(1)
    # Some schemas may have 'title:' and 'type:' after properties, so only parse properties
    # Try to cut off at the next 'title:' or 'type:'
    yaml_str = re.split(r'\ntitle:|\ntype:', yaml_str)[0]
    try:
        props = yaml.safe_load(yaml_str)
        properties = props.get('properties', props)  # sometimes top-level is already properties
        result = {}
        for field, meta in properties.items():
            result[field] = {
                'type': meta.get('type', 'object'),
                'description': meta.get('description', '')
            }
        return result
    except Exception as e:
        return {'error': str(e)}

@mcp.resource("schema://{schemaName}/fields")
def get_resource_fields_and_types_by_name(schemaName: str):
    """
    Returns the fields and types for a given schema resource by name.
    """
    resource_func = mcp.resources.get(f"schema://{schemaName}")
    if not resource_func:
        return {"error": f"Resource schema://{schemaName} not found"}
    return get_resource_fields_and_types(resource_func)
