import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestTodo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_checkall(self):
        '''
        测试是否正确渲染所有代办事项
        :return:
        '''
        driver = self.driver
        driver.get('http://127.0.0.1:8000/todo/list')
        todolist = driver.find_elements_by_name('todo')
        assert len(todolist)==6
    def test_addTodo(self):
        '''
        测试新建一个todo任务
        :return:
        '''
        driver = self.driver
        driver.get('http://127.0.0.1:8000/todo/list')
        old_todo_length = len(driver.find_elements_by_name('todo'))
        add_button = driver.find_element_by_id('createTodo')
        add_button.click()
        driver.find_element_by_id('todoid').send_keys('7')
        time.sleep(1)
        driver.find_element_by_id('content').send_keys('创建selenium自动测试计划')
        time.sleep(1)
        driver.find_element_by_id('createtime').send_keys('2020/4/2')
        time.sleep(1)
        driver.find_element_by_tag_name('button').click()
        new_todo_length = len(driver.find_elements_by_name('todo'))
        assert new_todo_length==old_todo_length+1
    def test_complete(self):
        '''
        测试将id为7的未完成事项标记为已完成
        :return:
        '''
        driver = self.driver
        driver.get('http://127.0.0.1:8000/todo/list')
        old_noComplete_len = len(driver.find_elements_by_class_name('noComplete'))
        old_isComplete_len = len(driver.find_elements_by_class_name('isComplete'))
        driver.find_element_by_id('noComplete7').click()
        time.sleep(1)
        driver.find_element_by_id('doComplete7').click()
        time.sleep(1)
        new_noComplete_len = len(driver.find_elements_by_class_name('noComplete'))
        new_isComplete_len = len(driver.find_elements_by_class_name('isComplete'))
        assert new_noComplete_len==old_noComplete_len-1
        assert new_isComplete_len == old_isComplete_len+1
    def tearDown(self):
        time.sleep(10)
        self.driver.close()
