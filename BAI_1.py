
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# chèn đơn hàng hỏa tốc vào đầu danh sách vị trí index

delivery_orders.insert(0, "GE000")


#  'GE002' đã chuyển sang vị trí số 2 
delivery_orders[2] = "GE002-UPDATED"

#Xóa trực tiếp bằng tên phần tử (Khuyên dùng trong trường hợp này)
delivery_orders.remove("GE003-CANCEL")

# GE003-CANCEL" đang ở vị trí số 3


transferred_order = delivery_orders.pop()

# In kết quả
print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)