# __author__ = 'Anjan Kumar Devara"
from appium.webdriver.common.touch_action import TouchAction

from Base_Capabilities.Find_Elements import FindElements
from Locators.Android_Locators import *


class TestAndroidMessagesScreenR(FindElements):

    def click_contact_message(self, contactname):
        contact_user_names = self.find_elements_by_resource_id("com.bullitt.wave:id/contact_user_name")
        for contact_user_name in contact_user_names:
            username = contact_user_name.text
            if username == contactname:
                contact_user_name.click()
                break

    def verify_if_a_conversation_doesnot_exists(self, contactname):
        contact_names = []
        contact_user_names = self.find_elements_by_resource_id("com.bullitt.wave:id/contact_user_name")
        for contact_user_name in contact_user_names:
            username = contact_user_name.text
            contact_names.append(username)
            assert contactname not in contact_names


    def click_plus_button(self):
        self.find_element_by_resource_id(messages_screen.get("add_contacts").click())

    def click_sos_button(self):
        self.find_element_by_resource_id(messages_screen.get("sos_btn").click())

    def fetch_number_of_messages_selected(self):
        msg_count = self.find_element_by_resource_id(messages_screen.get("msg_count")).text
        return msg_count

    def satellite_button(self):
        main_satellite_bg = self.find_element_by_resource_id(messages_screen.get("main_satellite_bg"))
        return main_satellite_bg

    def message_textbox(self):
        message_txtbox = self.find_element_by_resource_id(messages_screen.get("text_message_input"))
        return message_txtbox

    def type_message(self, typemessage):
        message_box = self.message_textbox()
        message_box.click()
        message_box.clear()
        message_box.send_keys(typemessage)

    def fetch_recently_received_message(self):
        message_text_views = self.find_elements_by_resource_id(messages_screen.get("message_text_view"))
        recent_message = message_text_views[-1].text
        return recent_message

    def fetch_recently_sent_message(self):
        message_text_views = self.find_elements_by_resource_id(messages_screen.get("message_text_view"))
        recent_message = message_text_views[-1].text
        return recent_message

    def fetch_a_specific_message_by_its_index(self, message_position):
        message_text_views = self.find_elements_by_resource_id(messages_screen.get("message_text_view"))
        recent_message = message_text_views[message_position]
        return recent_message

    def send_button(self):
        sendButton = self.find_element_by_resource_id(messages_screen.get("sendButton"))
        return sendButton

    def send_button_state(self):
        button_state = self.send_button().get_attribute("enabled")
        return button_state

    def more(self):
        more_button = self.find_element_by_resource_id(messages_screen.get("more_options"))
        return more_button

    def click_save_bookmarks(self):
        self.more().click()
        self.find_element_by_resource_id(messages_screen.get("popup_bookmark")).click()

    def click_block_button_button(self):
        self.more().click()
        self.find_element_by_resource_id(messages_screen.get("popup_block")).click()

    def noblock(self):
        no_block = self.find_element_by_resource_id(messages_screen.get("no_block"))
        return no_block

    def select_noblock_text(self):
        no_block_txt = self.noblock().text
        return no_block_txt

    def verify_no_block_message(self):
        no_block_msg = self.find_element_by_resource_id(messages_screen.get("no_block_msg"))
        no_block_msg_txt = no_block_msg.text
        assert no_block_msg_txt == "Messages sent to you from this contact will be received over internet or satellite connections."

    def satellite_block(self):
        satellite_block = self.find_element_by_resource_id(messages_screen.get("satellite_block"))
        return satellite_block

    def satellite_block_text(self):
        satellite_block_text = self.satellite_block().text
        return satellite_block_text

    def verify_satellite_block_message(self):
        satellite_block_msg = self.find_element_by_resource_id(messages_screen.get("satellite_block_msg"))
        satellite_block_msg_txt = satellite_block_msg.text
        assert satellite_block_msg_txt == "Messages sent to you from this contact via satellite will not be received."

    def block_ok_button(self):
        self.find_element_by_resource_id(messages_screen.get("block_ok")).click()

    def verify_contact_blocked_state(self):
        assert self.find_element_by_resource_id(messages_screen.get("block_text")).text == ("(Fully blocked)")

    def fully_block(self):
        fully_block = self.find_element_by_resource_id(messages_screen.get("fully_block"))
        return fully_block

    def fully_block_text(self):
        fully_block_text = self.fully_block().text
        return fully_block_text

    def fully_block_block_message(self):
        fully_block_msg = self.find_element_by_resource_id(messages_screen.get("fully_block_msg"))
        fully_block_msg_txt = fully_block_msg.text
        assert fully_block_msg_txt == "Once blocked, the contact will not be able to send messages to you."

    def no_block_state(self):
        no_block_state = self.noblock().get_attribute("checked")
        return no_block_state

    def satellite_block_state(self):
        satellite_block_state = self.satellite_block().get_attribute("checked")
        return satellite_block_state

    def fully_block_state(self):
        fully_block_state = self.fully_block().get_attribute("checked")
        return fully_block_state

    def click_delete_button(self):
        self.find_element_by_resource_id(messages_screen.get("delete_img")).click()

    def click_pin_button(self):
        self.find_element_by_resource_id(messages_screen.get("pin_img")).click()

    def location_icon(self):
        location_icon = self.find_element_by_resource_id(messages_screen.get("location_icon"))
        return location_icon

    def geo_icon(self):
        geo_icon = self.find_element_by_resource_id(messages_screen.get("geo_icon"))
        return geo_icon

    def turn_on_location(self, geo_state):
        # geo_state = self.geo_icon().is_displayed()

        match (geo_state):
            case "true":
                if (self.geo_icon().is_displayed() == False):
                    login_screen.click()
            case "false":
                login_screen.click()
            case _:
                pass


    def select_conversation(self, contactname):
        contact_user_names = self.find_elements_by_resource_id("com.bullitt.wave:id/contact_user_name")
        for contact_user_name in contact_user_names:
            username = contact_user_name.text
            if username == contactname:
                self.longpress(contact_user_name)
                break

    def select_top_3_messages(self):
        el4 = self.find_elements_by_resource_id(messages_screen.get("contact_user_name"))
        for contacts in range(3):
            self.longpress(el4[contacts])

    def fethc_pin_icons_count(self, expectedpins):
        pin_conversation = self.find_elements_by_resource_id(messages_screen.get("pin_conversation"))
        pin_conversation_count = len(pin_conversation)
        assert pin_conversation_count == expectedpins


    def verify_pin_icons_disappeared(self):
        self.verify_element_not_displayed(messages_screen.get("pin_conversation"))

    def fetch_wave_notification(self, contactName):
        self.driver.open_notifications()

        titles = self.find_elements_by_resource_id("android:id/title")
        for title in titles:
            noti_text = title.text
            if(noti_text == contactName):
                title.click()
                break
            break

    def verify_delete_alert_title(self):
        delete_alert_title = self.find_element_by_resource_id(messages_screen.get("delete_alert_title")).text
        assert delete_alert_title == "Delete this conversation?"

    def verify_delete_alert_text(self):
        delete_alert_text = self.find_element_by_resource_id(messages_screen.get("delete_alert_message")).text
        print("Alert TEXT :: ", delete_alert_text)
        assert delete_alert_text == "All messages in this conversation will be removed from this device."

    def cancel_delete_action(self):
        self.verify_delete_alert_title()
        # self.verify_delete_alert_text()
        self.find_element_by_resource_id(messages_screen.get("delete_cancel")).click()


    def delete_action(self):
        self.verify_delete_alert_title()
        # self.verify_delete_alert_text()
        self.find_element_by_resource_id(messages_screen.get("delete")).click()

    def start_conversation_screen_message(self):
        start_conversation_text = self.find_element_by_resource_id(messages_screen.get("start_conversation_text"))
        return start_conversation_text

    def verify_blue_ticks_on_the_recently_sent_message(self):
        blueTicks = self.find_elements_by_resource_id("com.bullitt.wave:id/message_container")
        displayed = blueTicks[-1].find_element(AppiumBy.ID,"com.bullitt.wave:id/blueTick").get_attribute("displayed")
        assert displayed == "true"

    def tap_back_key(self):
        self.find_element_by_accessibility_id("Navigate up").click()


    def clear_notifications(self):
        self.driver.open_notifications()
        # TouchAction(self.driver).press(x=517, y=2251).move_to(x=501, y=818).release().perform()
        # clearAll = self.find_element_by_resource_id("com.android.systemui:id/dismiss_text")
        # clearAll.click()