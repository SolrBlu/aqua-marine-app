def parse_aqua(file_path):
    print("--- in: aqua_to_page_content.py ---")
    print(f"reading and translating: {file_path}")
    content = {"message": "", "page_url": "", "comments": ""}

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "Display MESSAGE" in line:
                content["message"] = line.split('"')[1]
            elif "PageUrl:" in line:
                content["page_url"] = line.split(':')[1].strip()
            elif "Comment:" in line:
                content["comments"] = line.split(':')[1]
    return content

def generate_nextjs_code(page_content):
    print(f"page_content: {page_content}")
    return f"""
function Home() {{
    return (
        <main>
            <h1>{page_content["message"]}</h1>
        </main>
    );
}}

export default Home;
"""

def write_nextjs_file(js_code, output_path):
    with open(output_path, 'w') as file:
        file.write(js_code)

# Path to your Aqua file
aqua_file_path = 'aqua-language/pages/HelloWorld.aqua'

# Path where the Next.js file should be created
nextjs_output_path = 'nextjs-app/src/app/page.js'

# Parsing the Aqua file
page_content = parse_aqua(aqua_file_path)

# Generating Next.js code
nextjs_code = generate_nextjs_code(page_content)

# Writing the Next.js file
write_nextjs_file(nextjs_code, nextjs_output_path)

print("Next.js file generated successfully.")
print("")
