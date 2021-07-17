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

def determine_build_order(projects, dependencies):
    root_nodes = []
    non_roots = [x[0] for x in dependencies]
    root_nodes = [x for x in projects if x not in non_roots]
    orders = []

    def get_children(node):
        children = []
        for dependency in dependencies:
            if dependency[1] == node:
                children.append(dependency[0])
        return children

    def DFS(node):
        # visit node
        # check first if node has already been built, and if so raise appropriate exception
        if node in order:
            raise NoValidBuildOrderError("No valid build order exists")
        # mark node as visited
        visited.append(node)
        # get children and search them if not visited
        children = get_children(node)
        for child in children:
            if child not in visited:
                DFS(child)
        order.append(node)

    visited = []

    for root in root_nodes:
        # DFS
        order = []
        DFS(root)
        orders.extend(order)

    # check if valid graph
    if set(orders) != set(projects):
        raise NoValidBuildOrderError("No valid build order exists")
    return orders

def determine_build_order_concise(projects, dependencies):
    dependency_tree = {p: set() for p in projects}
    build_order = []
    unbuilt_projects = set(projects)
    for dependency, project in dependencies:
        dependency_tree[project].add(dependency)

    while unbuilt_projects:
        something_built = False
        for project in list(unbuilt_projects):
            dependencies = dependency_tree[project]
            # check if any dependencies of the project are still unbuilt. if not, build the project
            if not unbuilt_projects.intersection(dependencies):
                build_order.append(project)
                # remove the project from being unbuilt
                unbuilt_projects.remove(project)
                something_built = True
        # if nothing was built in this iteration, it means nothing can be built without a conflict.
        if not something_built:
            raise NoValidBuildOrderError("No valid build order exists")

    return build_order

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



