# Getting necessary header and footer data
header_file = open("page_bases/header.html", "r")
header_data = header_file.read()
header_file.close()

footer_file = open("page_bases/footer.html", "r")
footer_data = footer_file.read()
footer_file.close()

try:
    # Getting file contents
    index_file = open("page_bases/index.html", "r")
    index_data = index_file.read()
    index_file.close()

    # Adding header and footer
    index_data = index_data.replace("<!-- Heading section -->", header_data)
    index_data = index_data.replace("<!-- Footer section -->", footer_data)

    # Generating file
    index_file = open("page_gens/index.html", "w")
    index_file.write(index_data)
    index_file.close()
except FileNotFoundError:
    print("Could not find index page base.")

try:
    # Getting file contents
    projects_file = open("page_bases/projects.html", "r")
    projects_data = projects_file.read()
    projects_file.close()

    # Adding header and footer
    projects_data = projects_data.replace("<!-- Heading section -->", header_data)
    projects_data = projects_data.replace("<!-- Footer section -->", footer_data)

    # Generating file
    projects_file = open("page_gens/projects.html", "w")
    projects_file.write(projects_data)
    projects_file.close()
except FileNotFoundError:
    print("Could not find projects page base.")

try:
    # Getting file contents
    contact_file = open("page_bases/contact.html", "r")
    contact_data = contact_file.read()
    contact_file.close()

    # Adding header and footer
    contact_data = contact_data.replace("<!-- Heading section -->", header_data)
    contact_data = contact_data.replace("<!-- Footer section -->", footer_data)

    # Generating file
    contact_file = open("page_gens/contact.html", "w")
    contact_file.write(contact_data)
    contact_file.close()
except FileNotFoundError:
    print("Could not find contact page base.")
