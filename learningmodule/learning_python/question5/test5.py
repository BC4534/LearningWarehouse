import json


class StudentManagementSys():

    # {'张三': {'student_id': '001', 'class': '一班', 'score': {'数学': 90, '语文': 85, '英语': 92}}}
    def get_data(self):
        with open('student.json', 'r', encoding='utf-8') as f:
            loads = json.load(f)
            return loads

    def dump_data(self, data):
        with open('student.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # 学生信息录入
    def enter_student_info(self):
        name = input("请输入学生姓名:")
        student_id = input("请输入学生学号:")
        student_class = input("请输入学生班级:")
        math_score = int(input("请输入数学成绩:"))
        chinese_score = int(input("请输入语文成绩:"))
        english_score = int(input("请输入英文成绩:"))
        all_student_data = self.get_data()
        name_list = all_student_data.keys()
        if name in name_list:
            print("该学生数据已录入")
        else:
            all_student_data[name] = {'student_id': student_id, 'class': student_class,
                                      'score': {'数学': math_score, "语文": chinese_score, '英语': english_score}}

        self.dump_data(all_student_data)

    # 查询
    def query_student_score_info_by_id(self):
        # name = input("请输入要查询的学生姓名:")
        student_name = None
        student_id = input("请输入要查询的学生学号:")
        all_student_data = self.get_data()
        for name in all_student_data.keys():
            if all_student_data[name]["student_id"] == student_id:
                student_name = name
        try:
            student_id = all_student_data[student_name]["student_id"]
            student_class = all_student_data[student_name]["class"]
            math_score = all_student_data[student_name]["score"]["数学"]
            chinese_score = all_student_data[student_name]["score"]["语文"]
            english_score = all_student_data[student_name]["score"]["英语"]
            # print(f"学生姓名{student_name},学号{student_id},班级{student_class},数学成绩{math_score},语文成绩{chinese_score},英语成绩{english_score}")
            print(
                f"学生姓名{student_name},学号{student_id},班级{student_class},数学成绩{math_score},语文成绩{chinese_score},英语成绩{english_score}")
            return f"学生姓名{student_name},学号{student_id},班级{student_class},数学成绩{math_score},语文成绩{chinese_score},英语成绩{english_score}"
        except:
            print("学号输入有误,系统中暂无该学生信息!")

    def query_score_by_course(self):
        course = input("请输入要查询的课程名称:")
        all_student_data = self.get_data()
        try:
            for name in all_student_data.keys():
                score = all_student_data[name]["score"][course]
                print(f"{name}的{course}成绩是{score}")
        except:
            print("课程名称输入有误")

    # 统计每个学生的平均成绩
    # def _student_avg_grade(self,name,math_score,chinese_score,english_score):
    #     avg_g =  (math_score+chinese_score+english_score)/3
    #     print(f"{name}的平均成绩是{avg_g}")
    def student_avg_grade(self):
        avg_dict = {}
        all_student_data = self.get_data()
        for name in all_student_data.keys():
            math_score = all_student_data[name]["score"]["数学"]
            chinese_score = all_student_data[name]["score"]["语文"]
            english_score = all_student_data[name]["score"]["英语"]
            # self._student_avg_grade(name,math_score,chinese_score,english_score)
            avg_g = (math_score + chinese_score + english_score) / 3
            print(f"{name}的平均成绩是{avg_g}")
            avg_dict[name] = avg_g
        return avg_dict

    # 计算没门课的平均成绩
    def avg_grade_by_course(self):
        course = input("请输入要查询哪门课程的平均成绩:")
        all_student_data = self.get_data()
        num = len(all_student_data.keys())
        sum_score = 0
        try:
            for name in all_student_data.keys():
                sum_score += all_student_data[name]["score"][course]
            print(f"{course}的平均成绩是{sum_score / num}")
        except:
            print('课程名称输入有误!!!')

    def get_all_score(self):

        avg_dict = self.student_avg_grade()
        avg_list = self.student_avg_grade().values()
        sorted_avg_list = sorted(avg_list, reverse=True)
        for each in sorted_avg_list:
            for name in avg_dict.keys():
                if avg_dict[name] == each:
                    print(f'{name},平均成绩{each}')

    def sort_by_course_grades(self):
        course = input("请要查询的课程名称")
        sorted_dict = {}
        all_student_data = self.get_data()
        for name in all_student_data.keys():
            socre = all_student_data[name]["score"][course]
            sorted_dict[socre] = name
        for each in sorted(sorted_dict.keys(), reverse=True):
            print(f"{sorted_dict[each]}的{course}{each}")
def main():
    while True:
        print("------------------------")
        print("欢迎来到学生管理系统.....")
        print("学生信息录入请输入:1")
        print("学号查询该学生的所有课程成绩请按2")
        print("课程名称查询所有学生该课程的成绩 请按3")
        print("计算每个学生的平均成绩。请按4")
        print("计算每门课程的平均成绩。请按5")
        print("按照学生的平均成绩从高到低进行排序。请按6")
        print("可以按照某门课程的成绩从高到低进行排序。请按7")
        print("退出。请按8")
        operate = input()
        sms = StudentManagementSys()
        if operate == "1":
            sms.enter_student_info()
            print("学生数据录入成功!!!")
        elif operate =="2":
            sms.query_student_score_info_by_id()
        elif operate =="3":
            sms.query_score_by_course()
        elif operate =="4":
            sms.student_avg_grade()
        elif operate =="5":
            sms.avg_grade_by_course()
        elif operate =="6":
            sms.get_all_score()
        elif operate =="7":
            sms.sort_by_course_grades()
        elif operate =="8":
            print("退出系统成功,欢迎再来!!!")
            break




if __name__ == '__main__':
    main()

