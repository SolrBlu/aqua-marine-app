def formatComponentName(component_name):
    result = component_name[0].upper()
    capitalize_next = False

    for char in component_name[1:]:
        if char in ['-', '_']:
            capitalize_next = True
            continue

        if capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char
    return result

def generate_nextjs_code(page_content):
    # print(f"page_content: {page_content}")
    component_name = formatComponentName(page_content["component_name"])
    return f"""
function {component_name}() {{
    return (
        <main>
            <h1>{page_content["message"]}</h1>
        </main>
    );
}}

export default {component_name};
"""