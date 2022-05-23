from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime

# Create your tests here.
class MeetingTest(TestCase)
    def setUp(self):
        self.title=Meeting(titlename='Lenovo Laptop')

    def test_titlestring(self):
        self.assertEqual(str(self.title), 'Lenovo Laptop')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table) "meeting"

    
class MeetingTest(TestCase):
    def setup(self):
        self.title= Meeting(titlename='Laptop')
        self.user= Username (username='user1')
        self.meeting= Meeting(meetingname='Lenovo',productype=self.type, user=self.user, dateentered=datetime.date(2022,5,22),price=1200.99,product url='http://www.lenovo.com', description="lenovo laptop")

    def test_string(self):
        self.assertEqual(str(self.product)), 'Lenovo')

    def test_discount(self):
        dis = self.meeting.price * .05
        self.assertEqual(self.meeting.discountamount(),disc)

    def test_discountamount(self):
        disc=self.meeting.price *  (1)
        self.assertEqual(self.meeting.discountPrice(),disc)



        

        
