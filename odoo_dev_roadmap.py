# Odoo development roadmap

# 1. Create a new addon module
# - Create a new module directory for the module
# - Eg: mkdir library/

# 2. Create a new application
# - Create a new application(and its basic structure) inside the module directory
# - Using scaffold command
# - Eg: odoo-bin scaffold library_app library

# 3. Add Automated Tests(to follow TDD)(tests/)
# - Create a new test directory
# - Create tests for the model and its methods
# - Test create, read, write, and unlink operations and methods
# - In fact, It should fail at this point
# - As the model and its methods are not implemented yet
# - Eg: library/library_app/tests/test_library_book.py

# 4. Implement the model layer(models/)
# - Implement the model with its fields
# - Eg: library/library_app/models/library_book.py

# 5. Security Groups(Setting up Access Security)(security/)
# i. Create security groups and rules for the model
#   - (Mainly User and Manager groups)
#   - Eg: library/library_app/security/library_security.xml
# ii. Create Access Controls for the security groups
#   - Wheather the group can create, read, write, and delete records of the model
#   - Eg: library/library_app/security/ir.model.access.csv
# iii. Assign users to the security groups
#  - Eg: library/library_app/data/res_groups_data.xml(not sure about this example)

# 6. Implement the view layer(back-end views)(views/)
# - Create menu items for the application
# - Eg: library/library_app/views/library_menu.xml
# - Odoo generates simple views(like form and tree views)
# - for the model
# - Modify and extend the views as needed
# - Eg: library/library_app/views/book_view.xml(or separately: book_list_view.xml, book_form_view.xml, book_search_view.xml, etc.)

# 7. Implement the business logic layer
# - Add methods to the model
# - Eg: library/library_app/models/library_book.py
#     - (Methods like _check_isbn, button_check_isbn, etc.)

# 8. Implement the website ui(front-end views)(controllers/ and views/)
# - i. Create controllers for routing
#       - Eg: library/library_app/controllers/main.py
# - ii. Create templates using QWeb
#       - Eg: library/library_app/views/book_list_template.xml




