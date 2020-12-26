#You are given a list of projects and a list of dependencies 
# (which is a list of pairs of projects, where the second project is dependent on the first project). 
# All of a project's dependencies must be built before the project is. 
# Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

# Build Order

# projects a,b,c,d,e,f
# dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph


project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
customGraph = createGraph(project, dependencies)

def getDependant(graph): #helper function to find dependant nodes 
    projects = set()
    for project in graph:
        projects = projects.union(set(graph[project]))
    return projects

def nonDependant(projects, graph): #helper function to find independant nodes
    nonProject = set()
    for project in graph:
        if not project in projects:
            nonProject.add(project)
    return nonProject
dependant = getDependant(customGraph)
print(customGraph)
print(dependant)
print(nonDependant(dependant, customGraph))


def findBuildOrder(projects, dependencies):
    buildOrder = []
    projectGraph = createGraph(projects, dependencies)
    while projectGraph:
        projectDependant = getDependant(projectGraph)
        projectNonDependant = nonDependant(projectDependant, projectGraph)
        if len(projectNonDependant) == 0 and projectGraph: #if we find a cycle
            raise ValueError('There is a cycle in build order')
        for independentProjects in projectNonDependant:
            buildOrder.append(independentProjects) #we append independant nodes
            del projectGraph[independentProjects]  #and delete them from the dependancy graph
            #now there will be new independant nodes, and the function will continue until we have our build order
    return buildOrder
print(findBuildOrder(project, dependencies))
