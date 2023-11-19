from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import TextBox
from django.urls import reverse


class TextBoxSeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        # Create TextBox instances here, as you would in a normal TestCase
        TextBox.objects.create(content='Box AA', page_identifier='windows10', order=0)
        TextBox.objects.create(content='Box BB', page_identifier='windows10', order=1)
        # Create the rest of your TextBox instances...

    def test_text_box_ordering(self):
        # Navigate to the page that lists the TextBox instances
        self.selenium.get(self.live_server_url + reverse('windows10'))

        # Wait until the TextBox elements are loaded
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'text-box'))
        )

        # Fetch all elements with the class 'text-box'
        text_boxes = self.selenium.find_elements_by_class_name('text-box')

        # Extract text or another attribute that indicates order and compare
        contents = [box.text for box in text_boxes]
        self.assertTrue(contents == sorted(contents))

        # Add more specific tests, e.g., comparing the order of elements based on page_identifier, etc.

#class TextBoxModelTest(TestCase):
    #def setUp(self):
        # Create TextBox instances with the same 'order' value and different 'page_identifier' values
        #TextBox.objects.create(content='Box AA', page_identifier='pageA', order=0)
        #TextBox.objects.create(content='Box AB', page_identifier='pageA', order=1)
        #TextBox.objects.create(content='Box BA', page_identifier='pageB', order=0)
        #TextBox.objects.create(content='Box BB', page_identifier='pageB', order=1)
        #TextBox.objects.create(content='Box CA', page_identifier='pageC', order=0)
        #TextBox.objects.create(content='Box CB', page_identifier='pageC', order=1)

    #def test_ordering(self):
        # Fetch all TextBox instances
        #text_boxes = TextBox.objects.all()
        
        # The boxes should be ordered by 'order', then by 'id', then by 'page_identifier'
        #self.assertTrue(text_boxes[0].order <= text_boxes[1].order)
        #if text_boxes[0].order == text_boxes[1].order:
            #self.assertTrue(text_boxes[0].page_identifier <= text_boxes[1].page_identifier)

    #def test_page_identifier_ordering(self):
        # Fetch all TextBox instances with the same 'order' value
        #same_order_text_boxes = TextBox.objects.filter(order=2)
        
        # Convert QuerySet to a list and sort it by 'page_identifier' to test the ordering
        #sorted_by_page_identifier = sorted(same_order_text_boxes, key=lambda t: t.page_identifier)
        
        #self.assertEqual(list(same_order_text_boxes), sorted_by_page_identifier)