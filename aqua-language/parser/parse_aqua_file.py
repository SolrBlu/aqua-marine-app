def parse_aqua(file_path, component_name):
    content = {
        "component_name": component_name,
        "message": "",
        "page_url": "",
        "comments": ""
    }

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # print(f"{line}")
            if "Display MESSAGE:" in line:
                content["message"] = line.split('"')[1]
            elif "PageUrl:" in line:
                content["page_url"] = line.split(':')[1].strip()
            elif "Title:" in line:
                content["title"] = line.split(':')[1]
            elif "Comment:" in line:
                content["comments"] = line.split(':')[1]
    return content