"""(Incomplete) Tests for Place class."""
from place import Place


def test():#run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    # TODO: Write tests to show this initialisation works
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.is_visited
    print(new_place)

    # TODO: Add more tests, as appropriate, for each method
    # Test visit/unvisited marking
    print("Testing visit/unvisited: ")
    new_place.visit()
    assert new_place.is_visited
    print(new_place.is_visited)
    new_place.unvisited()
    assert not new_place.is_visited
    print(new_place.is_visited)

    # Test is_important method
    print("Testing is_important:")
    assert new_place.is_important() == 1
    print(new_place.is_important())
    return

# run_tests()
test()
