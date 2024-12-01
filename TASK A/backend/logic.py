class Exercise:
    def __init__(self, number, name, implements, time, priority):
        self.number = number #1-18
        self.name = name 
        self.implements = implements 
        self.time = time  
        self.priority = priority #1 more important, 18 less

    def __repr__(self):
        return f"{self.name} (Time: {self.time}s, Priority: {self.priority})"

exercises = [
    Exercise(1, "Bird to Dog", ["Floor space"], 120, 5),
    Exercise(2, "Bridge", ["Floor space"], 60, 12),
    Exercise(3, "Cat and Cow", ["Floor space"], 60, 4),
    Exercise(4, "Child's Pose", ["Floor space"], 120, 3),
    Exercise(5, "Extension Lying", ["Floor space"], 60, 13),
    Exercise(6, "Extension Standing", ["None"], 120, 2),
    Exercise(7, "Flexion Lying", ["Floor space"], 120, 14),
    Exercise(8, "Flexion Sitting", ["Chair"], 120, 11),
    Exercise(9, "Flexion Standing", ["None"], 60, 10),
    Exercise(10, "Forward Bend Sitting", ["Floor space"], 120, 1),
    Exercise(11, "Hamstring Curl", ["None"], 120, 15),
    Exercise(12, "Hamstring Stretch", ["Floor space"], 120, 9),
    Exercise(13, "Hip Flexor Stretch", ["Floor space"], 120, 8),
    Exercise(14, "Knees to Chest", ["Floor space"], 60, 18),
    Exercise(15, "Periformis Stretch", ["Floor space"], 120, 7),
    Exercise(16, "Side Slide", ["None"], 120, 17),
    Exercise(17, "Spinal Twist", ["Floor space"], 120, 6),
    Exercise(18, "Wall Sit", ["Wall"], 60, 16)]

def filter_exercises(exercises, available_implements, available_time):
    filtered_exercises = [exercise for exercise in exercises #filter implements
        if all(implement in available_implements for implement in exercise.implements)] 
    filtered_exercises.sort(key=lambda x: x.priority) #filter by priority

    selected_exercises = []
    total_time = 0
    for exercise in filtered_exercises: #filter time
        if total_time + exercise.time <= available_time:
            selected_exercises.append(exercise)
            total_time += exercise.time
        else:
            break  
    return selected_exercises
