# todoList
西交2020春敏捷web开发课后作业
## 作业内容
#####
    1 渲染一个todo List
    2 可以添加新的 todo 事项
    3 可以区分已完成和未完成事项
    4 可以将未完成的事项标记为已完成

## 实现细节
##### 
    $ python 3.7
    $ django 2.2
    $ sqlite3数据库
使用了Restful API 
#### 一级路由
#####
    $ path('todo/',include('todo.urls'))
#### 二级路由
#####
    $ path('list/',views.index,name = "todolist")
    $ path('add/',views.add,name = 'add')
    $ path('select/<int:todo_id>/',views.select,name='select')
    $ path('delete/<int:todo_id>/',views.delete,name='delete')
    $ path('complete/<int:todo_id>/', views.complete, name = 'complete')
### 结果截图
##### 返回所有Todo任务,区分已完成和未完成的todo事项
![todolist](result/selectall.png)
  
##### 创建一个新的Todo任务  
![todolist](result/createtodo.png)
##### 执行结果
![todolist](result/createresult.png)

##### 将未完成的todo事项标记为已完成
![todolist](result/complete1.png)
##### 执行结果
![todolist](result/complete2.png)
