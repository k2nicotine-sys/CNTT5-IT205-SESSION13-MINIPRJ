manager_info = {
"staff" : [],
"id_now": 101
}
while True :
    choice = input(
        """
QUẢN LÝ NHÂN SỰ - STAFF MANAGER

1. Thêm nhân viên mới
2. Danh sách nhân viên
3. Tìm kiem nhan viên (theo mã)
4. Xóa nhân viên khỏi hệ thông
5. Thoat chưong trinh
"""
)  
    match choice :
        case "1":
            while True:
                name = input("Vui lòng nhập tên: ")
                if name != "":
                    break
                print("Tên không được để trống")
            while True:
                        try:
                            salary = float(input("Vui lòng nhập mức lương: "))
                            if salary > 0:
                                break
                            print("Lương phải lớn hơn 0")
                        except:
                            print("Vui lòng nhập số hợp lệ")
                            employed = {
                        "id": manager_info["id_now"],
                        "name_staff": name,
                        "salary_staff": salary
                    }
                        manager_info["staff"].append(employed)
                        print(f"Thêm nhân viên thành công! ID: {employed['id']}")
                        manager_info["id_now"] += 1 

        case "2" :
            if len(manager_info["staff"]) == 0:
                print("Chưa có dữ liệu nhân sự!")

            for employee in manager_info["staff"]:
                print(
                f"{employee['id']}"
                f"{employee['name_staff']}"
                f"{employee['salary_staff']}"
            )
        case "5" :
            print("thoát chương trình")
            break 
       

