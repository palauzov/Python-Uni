class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age
    
    def worker_information(self):
        print(self.worker_num, self.fname, self.lname, self.work_experience_company, round(self.salary), self.age)

    def salary_bonus(self):
        if self.work_experience_company < 5:
           self.salary *= 1.005
        elif self.work_experience_company > 10:
           self.salary *= 1.02
        else:
           self.salary *= 1.015

def search_by_num(workers_list, worker_num):
    for i in range(len(workers_list)):
        if workers_list[i].worker_num == worker_num:
            return True
        
    return False

def search_by_name_expereince(workers_list, fname, work_experience_company):
    l1 = []
    for i in range(len(workers_list)):
       if workers_list[i].fname == fname and workers_list[i].work_experience_company == work_experience_company:
           l1.append(workers_list[i])
    return l1

def add_worker(workers_list, worker):
    workers_list.append(worker)
        
def remove_worker(worker_num):
     for i in range(len(workers_list)):
         if workers_list[i].worker_num == worker_num:
             workers_list.remove(workers_list[i])
             return "Information deleted!!!"
         
     return "Wrong worker num!!!"





workers_list = []
n = int(input("Number of workers: "))
for i in range(n):
    info = input("Worker: ").split(" ")
    w = Worker(int(info[0]), info[1], info[2], int(info[3]), float(info[4]), int(info[5]))
    workers_list.append(w)

worker = workers_list[0]

worker.salary_bonus()
worker.worker_information()
print(search_by_num(workers_list, 2))
print(search_by_name_expereince(workers_list, "Pesho", 10))
print(remove_worker(1))
print(workers_list)




