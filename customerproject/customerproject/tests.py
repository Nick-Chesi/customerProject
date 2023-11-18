from django.test import TestCase
from .models import TextBox

class TextBoxModelTest(TestCase):
    def setUp(self):
        # Create TextBox instances with the same 'order' value and different 'page_identifier' values
        TextBox.objects.create(content='Box AA', page_identifier='pageA', order=0)
        TextBox.objects.create(content='Box AB', page_identifier='pageA', order=1)
        TextBox.objects.create(content='Box BA', page_identifier='pageB', order=0)
        TextBox.objects.create(content='Box BB', page_identifier='pageB', order=1)
        TextBox.objects.create(content='Box CA', page_identifier='pageC', order=0)
        TextBox.objects.create(content='Box CB', page_identifier='pageC', order=1)

    def test_ordering(self):
        # Fetch all TextBox instances
        text_boxes = TextBox.objects.all()
        
        # The boxes should be ordered by 'order', then by 'id', then by 'page_identifier'
        self.assertTrue(text_boxes[0].order <= text_boxes[1].order)
        if text_boxes[0].order == text_boxes[1].order:
            self.assertTrue(text_boxes[0].page_identifier <= text_boxes[1].page_identifier)

    def test_page_identifier_ordering(self):
        # Fetch all TextBox instances with the same 'order' value
        same_order_text_boxes = TextBox.objects.filter(order=2)
        
        # Convert QuerySet to a list and sort it by 'page_identifier' to test the ordering
        sorted_by_page_identifier = sorted(same_order_text_boxes, key=lambda t: t.page_identifier)
        
        self.assertEqual(list(same_order_text_boxes), sorted_by_page_identifier)