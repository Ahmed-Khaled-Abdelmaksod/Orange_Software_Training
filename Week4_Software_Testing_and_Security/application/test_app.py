from app_management import app_management 

# partitioning Testing 

# title length > 10 && length < 30 (valid input)
def test_addition_valid_title_length():
    test_app = app_management()
    test_app.add_task("buy milk from supermarket","Go to supermarket","09-12-2024")
    assert len(test_app.get_tasks()) == 1

# invalid title
def test_addition_empty_title():
    test_app = app_management()

    test_app.add_task("","Go to supermarket","09-12-2024")
    assert len(test_app.get_tasks()) == 0

################################################################
# Boundary Testing

# title length > 10 && length < 30
#try title with small length(<10) (length = 10)
def test_addition_valid_title_length_10():
    test_app = app_management()
    test_app.add_task("buy  milk ","Go to supermarket","09-12-2024")
    assert len(test_app.get_tasks()) == 1

# title length > 10 && length < 30
#try title with small length(<10) (length = 30)
def test_addition_valid_title_length_30():
    test_app = app_management()
    test_app.add_task("buy milk from supermarket 2lsa","Go to supermarket","09-12-2024")
    assert len(test_app.get_tasks()) == 1

# title length > 10 && length < 30
#try title with small length(<10) (length = 9)
def test_addition_invalid_title_length():
    test_app = app_management()
    test_app.add_task("buy milk ","Go to supermarket","09-12-2024")
    assert len(test_app.get_tasks()) == 0

# title length > 10 && length < 30
#try title with small length(<10) (length = 31)
def test_addition_invalid_title_length1():
    test_app = app_management()
    test_app.add_task("buy milk from supermarket 2l sa","Go to supermarket","09-12-2024")
    assert len(test_app.get_tasks()) == 0

##################################################################################
# FSM Testing
# Test case to ensure that the value of the status changed
def test_completion():
    test_app = app_management()
    test_app.add_task("buy milk from supermarket","Go to supermarket","09-12-2024")
    test_app.complete_task("buy milk from supermarket")
    assert test_app.get_tasks()[0].status == True

##################################################################################

# ensure that deletion done sucessfully
def test_deletion_test1():
    test_app = app_management()
    test_app.add_task("buy milk from supermarket","Go to supermarket","09-12-2024")
    test_app.delete_task("buy milk from supermarket")
    assert len(test_app.get_tasks()) == 0

# ensure that the wanted task deleted sucessfully
def test_deletion_test2():
    test_app = app_management()
    test_app.add_task("buy milk from supermarket","Go to supermarket","09-12-2024")
    test_app.add_task("buy milk from supermarket2","Go to supermarket","09-12-2024")
    test_app.delete_task("buy milk from supermarket")
    assert test_app.get_tasks()[0].title == "buy milk from supermarket2"