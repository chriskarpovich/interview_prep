"""
You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent
on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects
to be built. If there is no valid build order, return an error.
Ex: 
Input: 
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output:
    f, e, a, b, d, c
"""
import pytest

# it is a directed graph. we want to find the deepest node(s) with no outgoing directed edges

class NoValidBuildOrderError(Exception):
    pass
        


            

def test_determine_build_order():
    projects = ["a", "b", "c", "d", "e", "f", "g"]
    dependencies = [
        ("d", "g"),
        ("a", "e"),
        ("b", "e"),
        ("c", "a"),
        ("f", "a"),
        ("b", "a"),
        ("f", "c"),
        ("f", "b"),
    ]
    build_order = determine_build_order(projects, dependencies)
    print(build_order)
    for dependency, project in dependencies:
        assert build_order.index(dependency) < build_order.index(project)


def test_impossible_build_order():
    # projects = ["a", "b"]
    # dependencies = [("a", "b"), ("b", "a")]
    projects = ["a", "b", "c", "d", "e", "f", "g"]
    dependencies = [
        ("d", "g"),
        ("a", "e"),
        ("b", "e"),
        ("c", "a"),
        ("f", "a"),
        ("b", "a"),
        ("f", "c"),
        ("f", "b"),
        ("e", "c")
    ]
    with pytest.raises(NoValidBuildOrderError):
        build_order = determine_build_order(projects, dependencies)
        print(build_order)

if __name__ == "__main__":
    test_determine_build_order()
    test_impossible_build_order()



