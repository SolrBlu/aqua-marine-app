def parse_aqua(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Simple parsing logic (could be more complex in a real scenario)
        for line in lines:
            if "Display MESSAGE" in line:
                message = line.split('"')[1]  # Extract the message between quotes
                return message
        return ""

def generate_nextjs_code(message):
    return f"""
function Home() {{
    return (
        <main>
            <h1>{message}</h1>
        </main>
    );
}}

export default Home;
"""

def write_nextjs_file(js_code, output_path):
    with open(output_path, 'w') as file:
        file.write(js_code)

# Path to your Aqua file
aqua_file_path = 'aqua-language/examples/HelloWorld.aqua'

# Path where the Next.js file should be created
nextjs_output_path = 'nextjs-app/src/app/page.js'

# Parsing the Aqua file
message = parse_aqua(aqua_file_path)

# Generating Next.js code
nextjs_code = generate_nextjs_code(message)

# Writing the Next.js file
write_nextjs_file(nextjs_code, nextjs_output_path)

print("Next.js file generated successfully.")
