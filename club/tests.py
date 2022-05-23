from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Meeting_Minutes, Resource, Event
import datetime
from .forms import MeetingForm

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.title=Meeting(titlename='Lenovo Laptop')

    def test_titlestring(self):
        self.assertEqual(str(self.title), 'Lenovo Laptop')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), "meeting")

    


class NewMeetingForm(TestCase):
        #valid form data
    def test_meetingform(self):
        data={
            'meetingname':'surface',
            'meetingdate' : 'laptop',
            'meetingtime':'5:00 pm', 
            'meetinglocation': 'Seattle',
            'meetingagenda': 'retirement 41k',
             }

        
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)

    def test_MeetingForm_Invalid(self):
        data={
            'meetingname':'surface',
            'meetingdate' : 'laptop',
            'meetingtime':'5:00 pm', 
            'meetinglocation': 'Seattle',
            'meetingagenda': 'retirement 41k',
             }

        form=MeetingForm(data)
        self.assertFalse(form.is_valid)







        

        
