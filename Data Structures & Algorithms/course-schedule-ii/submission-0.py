class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [i for i in range(numCourses)]
        dependencies = defaultdict(list)
        for p in prerequisites:
            dependencies[p[0]].append(p[1])
        schedule = []
        while courses:
            added = False
            for c in courses.copy():
                if all(d in schedule for d in dependencies[c]):
                    courses.remove(c)
                    schedule.append(c)
                    added = True
            if not added:
                return []
        return schedule
