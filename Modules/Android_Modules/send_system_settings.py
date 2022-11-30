import time

from Base_Capabilities.Find_Elements import FindElements
from Locators.Android_Locators import *


class TestBlockedContactsA(FindElements):

    def click_settings_in_nav_bar(self):
        nav_settings = self.find_element_by_resource_id(nav_bar.get("nav_settings"))
        nav_settings.click()

    def click_blocked_contacts_option(self):
        blockedcontacts = self.find_element_by_resource_id(blocked_contacts.get("blocked_contacts"))
        blockedcontacts.click()

    def click_fully_blocked_tab(self):
        fully_blocked = self.find_element_by_accessibility_id(blocked_contacts.get("fully_blocked"))
        fully_blocked.click()

    def unblock_contact_from_settings(self, contactname):
        blocked_contact_names = self.find_elements_by_resource_id(blocked_contacts.get("blocked_contact_name"))
        unblock_buttons = self.find_elements_by_resource_id(blocked_contacts.get("unblock_text"))

        blocked_contact_names_count = len(blocked_contact_names)
        for i in range(blocked_contact_names_count):
            blocked_contact_name = blocked_contact_names[i].text
            if(blocked_contact_name == contactname):
                unblock_buttons[i].click()
                break
            break

    def block_alert_title(self, blockedcontact):
        alert_title = self.find_element_by_resource_id(block_alert_dialog.get("alert_title")).text
        final_title = blockedcontact + alert_title[-18:]
        assert final_title == alert_title

    def block_receiver_alert_message(self, blockedcontact):
        alert_message = self.find_element_by_resource_id(block_alert_dialog.get("alert_message")).text
        final_message = blockedcontact + alert_message[-67:]
        assert final_message == alert_message

    def block_sender_alert_message(self):
        time.sleep(5)
        alert_message = self.find_element_by_resource_id(block_alert_dialog.get("alert_message")).text
        assert alert_message == "The user you are trying to send messages has blocked you from his/her contact list."

    def click_block_alert_cancel_button(self, blockedcontact):
        self.block_alert_title(blockedcontact)
        self.block_receiver_alert_message(blockedcontact)
        self.find_element_by_resource_id(block_alert_dialog.get("cancel_button")).click()

    def click_block_alert_unblock_button(self, blockedcontact):
        self.block_alert_title(blockedcontact)
        self.block_receiver_alert_message(blockedcontact)
        self.find_element_by_resource_id(block_alert_dialog.get("unblock_button")).click()

    def click_block_alert_ok_button(self, blockedcontact):
        # self.block_alert_title(blockedcontact)
        # self.block_sender_alert_message()
        time.sleep(5)
        ok_button = self.find_element_by_resource_id(block_alert_dialog.get("ok_button"))
        ok_button.click()

