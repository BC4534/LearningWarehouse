import json

class StudentManagementSys:
    def __init__(self, file_path="studentai.json"):
        """
        初始化学生管理系统，加载数据文件
        :param file_path: 存储学生信息的 JSON 文件路径
        """
        self.file_path = file_path
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.students = json.load(f)
        except FileNotFoundError:
            self.students = {}

    def save_data(self):
        """
        将学生信息保存到 JSON 文件中
        """
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.students, f, ensure_ascii=False, indent=4)

    def enter_student_info(self):
        """
        录入学生信息和成绩
        """
        name = input("请输入学生姓名: ")
        if name in self.students:
            print("该学生数据已录入。")
            return

        student_id = input("请输入学生学号: ")
        student_class = input("请输入学生班级: ")

        scores = {}
        while True:
            course = input("请输入课程名称（输入 '结束' 完成录入）: ")
            if course == '结束':
                break
            while True:
                try:
                    score = int(input(f"请输入 {course} 的成绩: "))
                    if 0 <= score <= 100:
                        scores[course] = score
                        break
                    else:
                        print("成绩必须在 0 - 100 之间，请重新输入。")
                except ValueError:
                    print("输入无效，请输入一个有效的整数。")

        self.students[name] = {
            "student_id": student_id,
            "class": student_class,
            "scores": scores
        }
        self.save_data()
        print("学生数据录入成功。")

    def query_student_score_by_id(self):
        """
        根据学号查询学生的所有课程成绩
        """
        student_id = input("请输入要查询的学生学号: ")
        found = False
        for name, info in self.students.items():
            if info["student_id"] == student_id:
                found = True
                print(f"学生姓名: {name}, 学号: {student_id}, 班级: {info['class']}")
                for course, score in info["scores"].items():
                    print(f"{course} 成绩: {score}")
                break
        if not found:
            print("学号输入有误，系统中暂无该学生信息。")

    def query_score_by_course(self):
        """
        根据课程名称查询所有学生该课程的成绩
        """
        course = input("请输入要查询的课程名称: ")
        found = False
        for name, info in self.students.items():
            if course in info["scores"]:
                found = True
                print(f"{name} 的 {course} 成绩: {info['scores'][course]}")
        if not found:
            print("课程名称输入有误或该课程无成绩记录。")

    def calculate_student_avg_scores(self):
        """
        计算每个学生的平均成绩
        """
        for name, info in self.students.items():
            scores = info["scores"]
            if scores:
                avg_score = sum(scores.values()) / len(scores)
                print(f"{name} 的平均成绩: {avg_score:.2f}")
            else:
                print(f"{name} 暂无成绩记录。")

    def calculate_course_avg_score(self):
        """
        计算每门课程的平均成绩
        """
        course_scores = {}
        for info in self.students.values():
            for course, score in info["scores"].items():
                if course not in course_scores:
                    course_scores[course] = []
                course_scores[course].append(score)

        if not course_scores:
            print("暂无课程成绩记录。")
            return

        course = input("请输入要查询哪门课程的平均成绩: ")
        if course in course_scores:
            avg_score = sum(course_scores[course]) / len(course_scores[course])
            print(f"{course} 的平均成绩: {avg_score:.2f}")
        else:
            print("课程名称输入有误或该课程无成绩记录。")

    def sort_students_by_avg_score(self):
        """
        按照学生的平均成绩从高到低进行排序
        """
        student_avg_scores = []
        for name, info in self.students.items():
            scores = info["scores"]
            if scores:
                avg_score = sum(scores.values()) / len(scores)
                student_avg_scores.append((name, avg_score))

        if not student_avg_scores:
            print("暂无学生成绩记录。")
            return

        sorted_students = sorted(student_avg_scores, key=lambda x: x[1], reverse=True)
        for name, avg_score in sorted_students:
            print(f"{name}: 平均成绩 {avg_score:.2f}")

    def sort_students_by_course_score(self):
        """
        按照某门课程的成绩从高到低进行排序
        """
        course = input("请输入要查询的课程名称: ")
        student_course_scores = []
        for name, info in self.students.items():
            if course in info["scores"]:
                score = info["scores"][course]
                student_course_scores.append((name, score))

        if not student_course_scores:
            print("课程名称输入有误或该课程无成绩记录。")
            return

        sorted_students = sorted(student_course_scores, key=lambda x: x[1], reverse=True)
        for name, score in sorted_students:
            print(f"{name} 的 {course} 成绩: {score}")


def main():
    sms = StudentManagementSys()
    while True:
        print("------------------------")
        print("欢迎来到学生管理系统.....")
        print("学生信息录入请输入: 1")
        print("学号查询该学生的所有课程成绩请按 2")
        print("课程名称查询所有学生该课程的成绩 请按 3")
        print("计算每个学生的平均成绩 请按 4")
        print("计算每门课程的平均成绩 请按 5")
        print("按照学生的平均成绩从高到低进行排序 请按 6")
        print("按照某门课程的成绩从高到低进行排序 请按 7")
        print("退出 请按 8")
        operate = input()

        if operate == "1":
            sms.enter_student_info()
        elif operate == "2":
            sms.query_student_score_by_id()
        elif operate == "3":
            sms.query_score_by_course()
        elif operate == "4":
            sms.calculate_student_avg_scores()
        elif operate == "5":
            sms.calculate_course_avg_score()
        elif operate == "6":
            sms.sort_students_by_avg_score()
        elif operate == "7":
            sms.sort_students_by_course_score()
        elif operate == "8":
            print("退出系统成功，欢迎再来!!!")
            break
        else:
            print("输入无效，请输入 1 - 8 之间的数字。")


if __name__ == "__main__":
    main()